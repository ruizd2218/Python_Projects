import os
import shutil
import sys
import subprocess
from tkinter import filedialog
import datetime as dt

def chooseSource(self):
    src = filedialog.askdirectory()
    self.sourcePath.insert(0, src)

def chooseDest(self):
    dest = filedialog.askdirectory()
    self.destPath.insert(0, dest)
 
def MoveFiles(self):
    src = self.sourcePath.get()
    dest = self.destPath.get()
    
    fileList = os.listdir(src)
    pastTime = dt.datetime.now() - dt.timedelta(hours=24)
    
    for i in fileList:
        abspath = os.path.join(src,i).replace("\\", "/")
        mTime = os.path.getmtime(abspath)
        mTimeR = dt.datetime.fromtimestamp(mTime)

        if mTimeR > pastTime:
            shutil.move(abspath, dest)
