import os
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
print (trackList)
musicSelect = int(input("Select a track: "))
while musicSelect > (trackNumber - 1) or musicSelect < 0:
    print("Number out of range!")
    musicSelect = int(input("Select a track: "))
