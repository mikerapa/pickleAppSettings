from shutil import copyfile
import pickle
import os 
import re
import sys

class AppSettings:
    LastKnowAPKVersion = 0

def saveSettings(appsettings):
    pickle.dump(appsettings, open("appsettings.pickle", "wb"))

def loadSettings():
    try:
        return pickle.load(open("appsettings.pickle", "rb"))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        print("Application settings file was not found. Using default values. ")
        return AppSettings()
            # do nothing

# Uset the values from the pickle
app = loadSettings()
print(f"LastKnownAPKVersion {app.LastKnowAPKVersion}")

app.LastKnowAPKVersion = int(app.LastKnowAPKVersion)+1
# Save app settings
saveSettings(app)