import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = ""

# Read all files from directory `.input`
files = os.listdir("input")

# Loop through all files
for file in files:
    f = open(f"input/{file}", "rb")
    try:
        transcript = openai.Audio.transcribe("whisper-1", file=f)
        # Write transcript to file
        with open("output/" + file + ".txt", "w") as text_file:
            text_file.write(transcript["text"])
    except Exception as e:
        print(f"Error transcribing file {file}: {e}")
    finally:
        f.close()
