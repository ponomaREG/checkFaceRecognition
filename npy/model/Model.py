import os
import glob
import numpy as np
import cv2
import tensorflow as tf
from numpy import load, save
import pickle

from .fr_utils import *
from .inception_blocks_v2 import *
from keras import backend as K


class Model:

    def __init__(self):
        self.FRmodel = None

    def triplet_loss(self, y_true, y_pred, alpha=0.3):
        anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]

        pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor,
                                                       positive)), axis=-1)
        neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor,
                                                       negative)), axis=-1)
        basic_loss = tf.add(tf.subtract(pos_dist, neg_dist), alpha)
        loss = tf.reduce_sum(tf.maximum(basic_loss, 0.0))

        return loss


    def init(self):
        print("Initialization...")
        K.set_image_data_format('channels_first')
        # if(os.path.exists(os.path.join(os.environ["STATIC_FOLDER"],"model.sav"))):
        #self.FRmodel = pickle.load(open(os.path.join(os.environ["STATIC_FOLDER"],"model.sav"),'rb'))
        # else:
        self.FRmodel = faceRecoModel(input_shape=(3, 96, 96))
        self.FRmodel.compile(optimizer='adam', loss=self.triplet_loss, metrics=['accuracy'])
        load_weights_from_FaceNet(self.FRmodel)
            # pickle.dump(self.FRmodel,open(os.path.join(os.environ["STATIC_FOLDER"],"model.sav"),'wb'))
        print("End of initialization")

    def prepare_database(self):
        database = {}
        for file in glob.glob("arrays/*"):
            identity = os.path.splitext(os.path.basename(file))[0]

            database[identity] = load(file)
        return database


    def encPhoto(self,file):
        enc = img_path_to_encoding(file, self.FRmodel)
        return enc


    def who_is_it(self, image, model=None, database=None):
        if database is None:
            database = self.prepare_database()
        if model is None:
            model = self.FRmodel
        encoding = img_to_encoding(image, model)
        min_dist = 100
        identity = None
        for (name, db_enc) in database.items():
            dist = np.linalg.norm(db_enc - encoding)
            if (dist <= 0.52):
                print('distance for %s is %s' % (name, dist))
            if dist < min_dist:
                min_dist = dist
                identity = name

        if min_dist > 0.52:
            return None
        else:
            return identity