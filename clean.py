import os , shutil

userPath = os.path.expanduser("~")
paths = [userPath + "/AppData/Local/Temp", "C:/Windows/Prefetch", userPath + "/temp"]

for path in paths:
    try:
        for file in os.listdir(path):
            filePath = os.path.join(path, file)
            try:
                if os.path.isfile(filePath):
                    os.remove(filePath)
                elif os.path.isdir(filePath):
                    os.chmod(filePath, 0o777)
                    shutil.rmtree(filePath)
            except Exception as e:
                print(f"Couldn't delete {filePath}: {e}")
    except Exception as e:
        print(f"Error deleting content from {path}: {e}") 