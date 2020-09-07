import os

class Config:
    def configure(self):
        os.environ["ROOT_PROJECT"] = os.path.dirname(os.getcwd())
        os.environ["STATIC_FOLDER"] = os.path.join(os.environ["ROOT_PROJECT"],"static")
        os.environ["IMAGE_FOLDER"] = os.path.join(os.environ["STATIC_FOLDER"],"images")
        os.environ["NPY_FOLDER"] = os.path.join(os.environ["STATIC_FOLDER"],"npy")
        os.environ["PATH_TO_DB"] = os.path.join(os.environ["STATIC_FOLDER"],"db.db")
        os.environ["WEIGHTS_PATH"] = os.path.join(os.environ["STATIC_FOLDER"],"weights")

    def create(self):
        try:
            os.makedirs(os.environ["IMAGE_FOLDER"])
            os.makedirs(os.environ["NPY_FOLDER"])
        except FileExistsError:
            pass

    def checkDB(self):
        if os.path.exists(os.environ["PATH_TO_DB"]):
            return True
        else:
            raise FileNotFoundError


