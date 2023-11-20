import os  

userPath = os.path.expanduser("~")
paths = [userPath + "/AppData/Local/Temp", userPath + "/Desktop/UOC"]
print(paths)
print (os.listdir(paths[1]))
#print (os.path.expanduser("~"))