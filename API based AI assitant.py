import google.generativeai as genai

#adding tts here
import requests
import subprocess
import urllib.parse

def Model_speak(text):
    # Free StreamElements voice
    voice = "Joanna"
    encoded = urllib.parse.quote(text)
    url = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={encoded}"

    print(f"[MODEL] Speaking: {text}")
    response = requests.get(url)
    print("voice response generated..")

    if response.status_code == 200:
        with open("model_voice.mp3", "wb") as f:
            f.write(response.content)
        subprocess.run(["mpg123", "model_voice.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("done..")
    else:
        print(" Voice generation failed. Check your internet connection.")

#Google LLM API
genai.configure(api_key="YOUR_API_KEY_HERE")

model = genai.GenerativeModel("MODEL NAME HERE")

#Prompting and context inserting
raw_prompt ="Add Base Context Here"
prompt= input("Enter your query: ")
full_prompt = raw_prompt + prompt
response = model.generate_content(full_prompt)
Model_speak(response.text)
