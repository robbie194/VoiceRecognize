Voice recognize and speak with a simple ui

Just run ui_main.py directly is ok

1. Packages that need to be installed:
  speech_recognition
  vosk
  pyttsx3

2. You need to go to https://alphacephei.com/vosk/models to download English and Chinese offline packages
My current demo uses the smallest model, so the recognition effect is limited.
After downloading, change ui_main.py to your local path:
cn_model_path
en_model_path
Do not change the name of the model casually, because Chinese and English models are distinguished by whether the name contains "cn" and "en"

3. There are requirements for the recording file format, preferably wav files (verified, stable), other formats can be converted to this format first
When naming the recording file, you must also include "cn" and "en" to distinguish which Chinese and English model to call.
