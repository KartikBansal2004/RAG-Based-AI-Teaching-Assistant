import requests
import os
import json
import pandas as pd
import numpy as np
import ollama
from sklearn.metrics.pairwise import cosine_similarity
import joblib
    
joblib_file = 'df_with_embeddings.joblib'     # change this to 'jsons_with_embeddings.csv' if you want to read the csv file from the current directory instead of sample_jsons folder
df = joblib.load(joblib_file)

def create_embedding(text_list):
    r = requests.post(
        'http://localhost:11434/api/embed',
        json={
            'model': 'mxbai-embed-large',
            'input': text_list
        }
    )
    embedding  = r.json()["embeddings"]
    return embedding

def inference(prompt):
    r = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'llama3.2',
            'prompt': prompt,
            'stream': False
        }
    )
    response = r.json()
    return response


incoming_query = input("Enter your question: ")
question_embedding = create_embedding([incoming_query])[0]

similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()
print(similarities)
top_results = 3
max_indx = similarities.argsort()[::-1][0:top_results]
print(max_indx)
new_df = df.loc[max_indx]
print(new_df[['title', 'number', 'text']])

prompt = f'''You are a helpful assistant for the course. Here are some video subtitle chunks containing video title, video number, start time in seconds, end time in seconds, the text at that time:

{new_df[['title', 'number', 'text', 'start', 'end']].to_json(orient = 'records')}
----------------------------------
"{incoming_query}"
User asked this question related to the video chunks, you have to answer in a human way (dont mention the above format, its just for you) where and how much content is taught in which video (in which video and at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the course.
'''

response = inference(prompt)['response']
print(response)

with open('prompt.txt', 'w') as f:
    f.write(prompt)
    
with open('response.txt', 'w') as g:
    g.write(response)