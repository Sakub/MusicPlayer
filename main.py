import os
trackList = []
trackNumber = 0

def check():
    global trackNumber
    path="Music"
    for file in os.listdir(path):
        if file.endswith(".mp3"):
            print (trackNumber,". ", file, sep="")
            trackNumber += 1


print("Welcome in the music player!")
print("List of tracks you have:")
check()
