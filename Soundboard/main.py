from soundboards import SOUNDBOARD_URL
import playsound
import time
import keyboard
import threading

def play_sound(character: str):
    if(SOUNDBOARD_URL.get(character) != None):
        playsound.playsound(f"https://www.myinstants.com/media/sounds/{SOUNDBOARD_URL[character]}")
    

while True:
    threading.Thread(target=play_sound, args=(keyboard.read_key())).start()
    time.sleep(0.2)