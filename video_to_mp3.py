import os
import subprocess

files = os.listdir('videos')

for file in files:
    tutorial_number = file.split(" #")[1].split('.')[0]
    file_name = file.split(" ｜ ")[0]
    print(tutorial_number, ":", file_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])
    
    # subprocess.run(["ffmpeg", "-i", f"videos/sample.mp4", f"audios/sample.mp3"])     #just for creating sample.mp3