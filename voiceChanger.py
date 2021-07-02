# importing the SpeechRecognition library in python
import speech_recognition as sr
# importing gTTS to use the google text to speech service
from gtts import gTTS
# importing OS to run smoothly
import os
# To easily play audio and record audio, through python
import pyaudio

"""
Briefing:
This is a voice changer which extracts voice/audio through a microphone,
and changes the human voice as a robotic or computerized voice.

Note: US English is the language used to input audio/voice.
"""

# All the messages will be stored in voiceAudio
voiceAudio = ""

# creating an infinite loop to capture all audio/ voice messages
while True:
    # Creating a variable to the Recognizer class
    recognize = sr.Recognizer()

    # Using the microphone as our audio source here
    with sr.Microphone() as audioSource:

        try:
            # Creating a variable which will store the voice/audio which will be input through the microphone
            audioVoice = recognize.listen(audioSource)

            # Extracting the words entered by the microphone through audio/voice as text using the google service
            extractedText = recognize.recognize_google(audioVoice)

            # To check the text corrected extracted
            print(extractedText)

            # If the user needs to stop the process say stop (can change to any word other than "stop",to stop)
            if extractedText == "stop":
                print("\nThe process has stopped...\nYou can check the saved audio file now !\n")
                break
            # storing the voice entered by the microphone as text while the process in running
            voiceAudio = voiceAudio+str(extractedText)

        except:
            # If user wont say anything as voice/audio
            print("Hello are you there ?... Say something...")


# Converting the extracted text as an audio file (with the use of google text to speech service)
# Also setting the language to English and making the audio NOT slow
textAudioConversion = gTTS(text=voiceAudio, lang='en', slow=False)

# Finally Saving the Audio file
textAudioConversion.save("VoiceAudio Changer.mp3")











