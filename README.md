# API_BASED_BASIC_ASSISTANT


This project is a simple Python script that connects a Google Generative AI model with a free Text-to-Speech (TTS) engine. The goal is to take a user’s text input, generate an AI response, and convert that response into spoken audio.

It’s lightweight, beginner-friendly, and uses completely free tools end-to-end.


✨*What This Script Does

•	Takes input from the user

•	Sends it to a Google Generative AI model

•	Receives the model’s response

•	Converts that response into speech using a free TTS API

•	Plays the generated audio locally





📦 *Requirements*

#Install the necessary Python packages:

pip install google-generativeai requests

#Install the audio player used for playback:

sudo apt install mpg123




🔧 Setup Instructions

1. Add your Google API key
2. Choose your model
3. Add your base context




🗣️ Text-to-Speech Info

The script uses StreamElements’ free TTS API:
	
•	No API key required
	
•	Fast responses
	
•	Voice can be changed (default: Joanna)
	
•	Audio is saved as model_voice.mp3 and played using mpg123




📜 License

Free to modify and use, including in personal or educational projects.
