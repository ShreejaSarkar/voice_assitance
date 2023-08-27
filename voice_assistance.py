import speech_recognition as sr
from gtts import gTTS
import os
import pygame  # Add this import

# Initialize pygame
pygame.init()

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen_to_user():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("I'm sorry, I couldn't request results. Check your internet connection.")
        return ""

def respond_to_user(response):
    if response:
        tts = gTTS(text=response, lang='en')
        tts.save("response.mp3")

        # Play audio using pygame
        pygame.mixer.music.load("response.mp3")
        pygame.mixer.music.play()
        pygame.event.wait()

def main():
    while True:
        user_command = listen_to_user()

        if "hello" in user_command:
            respond_to_user("Hello! How can I assist you today?")
        elif "goodbye" in user_command:
            respond_to_user("Goodbye! Have a great day!")
            break
        else:
            respond_to_user("I didn't understand that command. Please try again.")

if __name__ == "__main__":
    main()
