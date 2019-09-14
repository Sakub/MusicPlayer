import os
import pygame
from mutagen.mp3 import MP3
import time, sys
trackList = []
trackNumber = 0

def check():
    global trackNumber
    path="Music"
    for file in os.listdir(path):
        if file.endswith(".mp3"):
            print (trackNumber,". ", file, sep="")
            trackList.append(file)
            trackNumber += 1


print("Welcome in the music player!")
print("List of tracks you have:")
check()
musicSelect = int(input("Select a track: "))
while musicSelect > (trackNumber - 1) or musicSelect < 0:
    print("Number out of range!")
    musicSelect = int(input("Select a track: "))
pygame.mixer.init()
pygame.mixer.music.load("./Music/"+trackList[musicSelect])
pygame.mixer.music.play()
song = MP3("./Music/"+trackList[musicSelect])
songLength = song.info.length

print("...")
print("Now playing: ", trackList[musicSelect])
print("...")
print("Duration: ", round((songLength / 60), 2) - 0.22)
duration = songLength
while duration > 0:
    duration -= 1
    time.sleep(1)
while True:
    try:
        musicSelect += 1
        pygame.mixer.music.load("./Music/"+trackList[musicSelect])
    except IndexError:
        musicSelect = 0
        pygame.mixer.music.load("./Music/"+trackList[musicSelect])
    finally:
        pygame.mixer.music.play()
        song = MP3("./Music/"+trackList[musicSelect])
        songLength = song.info.length
        
        print("...")
        print("Now playing: ", trackList[musicSelect])
        print("...")
        print("Duration: ", round((songLength / 60), 2) - 0.22)
        duration = songLength
        while duration > 0:
            duration -= 1
            time.sleep(1)
        