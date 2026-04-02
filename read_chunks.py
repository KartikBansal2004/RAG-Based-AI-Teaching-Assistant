import requests
import os
import json
import pandas as pd
import ollama
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib

    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings


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

jsons = os.listdir('sample_jsons')                            # change this to 'jsons' if you want to read from the jsons folder instead of sample_jsons
my_dicts = []
chunk_id = 0

for json_file in jsons:
    with open(f'sample_jsons/{json_file}') as f:              # change this to f'jsons/{json_file}' if you want to read from the jsons folder instead of sample_jsons
        content = json.load(f)
        
    print(f"Creating Embeddings for {json_file}")
    embeddings = [create_embedding(c['text']) for c in content['chunks']]

    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)
        
    #break                                                     # use break if you want to just test for one json file, remove this later to run for all json files
# print(my_dicts)

df = pd.DataFrame.from_records(my_dicts)
joblib.dump(df, 'df_with_embeddings.joblib')     # saving the dataframe with embeddings as a joblib file for later use in pull_match_chunks.py

incoming_query = input("Enter your question: ")
question_embedding = create_embedding([incoming_query])[0]

similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()
print(similarities)
top_results = 3
max_indx = similarities.argsort()[::-1][0:top_results]
print(max_indx)
new_df = df.iloc[max_indx]
print(new_df[['title', 'number', 'text']])