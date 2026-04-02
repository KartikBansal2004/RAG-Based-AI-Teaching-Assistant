import whisper
import os
import json

model = whisper.load_model("large-v2")

# Currently I'm using around 20 second sample audio to save time. 
# Now making a program for sample.mp3, because the proper program made after it won't work on sample            
            
            
audios = 'sample.mp3'            
for audio in audios:
    number = 'sample'
    title = 'sample'
    print(number,":", title)

    result = model.transcribe(audio = 'audios/sample.mp3',    
                                language = 'hi',
                                task = 'translate', 
                                word_timestamps = False)            
    
    

    chunks = []
    for segment in result['segments']:
        chunks.append({'number' : number, 'title':title, 'start':segment['start'], 'end':segment['end'], 'text' : segment['text']})
        
    chunks_with_metadata = {'chunks':chunks, 'text':result['text']}
    
    with open(f'sample_json/{audio}.json', 'w') as f:
        json.dump(chunks_with_metadata, f)

#SOMEHOW, SAMPLE WENT ON AN INFINITE LOOP. WILL FIX IT LATER! OR JUST REMOVE number & text FROM THE APPEND BECAUSE THEY ARE NOT AT ALL NEEDED IN SAMPLE, BUT THE TASK IS DONE
            
            
            
            



# For the proper large format audios, the code is as follows:

# audios = os.listdir('audios')

# for audio in audios:
#     if ('_' in audio):
#         number = audio.split('_')[0]
#         title = audio.split('_')[1][:-4]       # used []:-4] to remove .mp3 from the end
#         print(number,":", title)

        
#         result = model.transcribe(audio = f'audios/{audio}',      
#                                   language = 'hi',
#                                   task = 'translate', 
#                                   word_timestamps = False)
        
#         chunks = []
#         for segment in result['segments']:
#             chunks.append({'number' : number, 'title':title, 'start':segment['start'], 'end':segment['end'], 'text' : segment['text']})
            
#         chunks_with_metadata = {'chunks':chunks, 'text':result['text']}
        
#         with open(f'json/{audio}.json', 'w') as f:
#             json.dump(chunks_with_metadata, f)
            
# json folder is now filled with the json texts for the pracitce purposes