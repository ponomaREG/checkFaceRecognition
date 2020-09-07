import glob
import os
from .model.Model import Model
from numpy import save

class NpyHelper:
    def __init__(self,path):
        self._folder_npy_path = path
        self._model = Model()
        self._model.init()

    def transformAllIn(self,folder_path):
        for file in glob.glob(os.path.join(folder_path,'*.*')):
            self.transformPhoto(file)


    def transformPhoto(self,path_to_image):
        identity = os.path.splitext(os.path.basename(path_to_image))[0]
        enc = self._model.encPhoto(path_to_image)
        save(os.path.join(self._folder_npy_path,identity+".npy"),enc)