import os
trackList = []
trackNumber = 0

def check():
    path="./Music/"
    for file in os.listdir(path):
        if file.endswith("*.mp3"):
            print (os.path.join(path, file))


print("Welcome in the music player!")
print("List of tracks you have:")
check()
