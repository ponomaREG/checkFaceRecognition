import os
import glob
import cv2
import chardet
import base64

class Helper:
    def __init__(self,path):
        self._path = path

    def clean(self):
        counter = 0
        for file in glob.glob(os.path.join(os.environ["IMAGE_FOLDER"],"*.*")):
            self.encode(file)
            counter += 1
            print(counter)


    def encode(self,filepath):
        dirname = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        filenameWithoutExt = filename.split(".")[0]
        ext = filename.split(".")[1]
        base = base64.b64encode(bytes(str(filenameWithoutExt),"cp1251"))
        newfilename = os.path.join(dirname,str(base,"utf-8")+"."+ext)
        os.rename(filepath,newfilename)

    def decode(self,filepath):
        dirname = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        filenameWithoutExt = filename.split(".")[0]
        ext = filename.split(".")[1]
        base = base64.b64decode(bytes(str(filenameWithoutExt),"utf-8"))
        newfilename = os.path.join(dirname,str(base,"cp1251")+"."+ext)
        os.rename(filepath,newfilename)
