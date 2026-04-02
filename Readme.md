# How to use this RAG AI Teaching assistant on your own data
## Step 1 - Collect your videos
Move all your video files to the videos folder

## Step 2 - Convert to mp3
Convert all the video files to mp3 by ruunning video_to_mp3

## Step 3 - Convert mp3 to json 
Convert all the mp3 files to json by ruunning mp3_to_jsons

## Step 4 - Convert the json files to Vectors
Use the file final_preprocessing to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

## Step 5 - Prompt generation and feeding to LLM
Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it to the LLM

## Models I used for practice reference:
You can also refer to the Ollama's GitHub for choosing your own preferred models: https://github.com/ollama/ollama/blob/main/docs/api.md  
### --> Model used for Embedding: mxbai-embed-large
### --> Model used for Inference: llama3.2
