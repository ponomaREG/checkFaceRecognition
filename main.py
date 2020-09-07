import os
import time
import math
from src.config import Config
from src.cleaner.Helper import Helper as HelpCleaner
import cv2
from src.npy.NpyMaker import NpyHelper
from src.dbHelper.DbHelper import Helper
from src.downloader.DownloaderPhotoFromMetroSite import Downloader
from src.thread.Mainer import Thr



def configure():
    conf = Config()
    conf.configure()
    conf.create()
    conf.checkDB()


configure()
# helper = HelpCleaner(os.environ["IMAGE_FOLDER"])
# helper.clean()
# print(os.environ["ROOT_PROJECT"])


# path = os.path.join(os.environ["STATIC_FOLDER"],"3513989488.jpg")
# ph = cv2.imread(path)
# cv2.imshow("photo",ph)
# cv2.waitKey()

npy = NpyHelper(os.environ["NPY_FOLDER"])
npy.transformAllIn(os.environ["IMAGE_FOLDER"])


#
# counter = 0
# counter_success = 0
#
# downloader = Downloader(os.environ["IMAGE_FOLDER"])
#
# db_students = Helper(os.environ["PATH_TO_DB"])
# db_students.connect()
# db_students.execute("select * from cards_order where person_id in(select id from cards_students order by clc_birthdate desc)")

# for i in range(100):
#     thr = Thr(downloader,db_students,100,i)
#     thr.start()
#size = db_students.size()
# for i in range(size):
#     photo = db_students.getAt(i)[3]
#     if downloader.download(photo) is False:
#         print("BAD RESPONSE!\n")
#         time.sleep(0.5)
#     else:
#         counter_success+=1
#     counter +=1
#     print("Complete {} %, Number:{}, Success:{}, PercentOfSuccessResults:{}".format(round(counter/size,3),i,counter_success,round(counter_success/(i+1),2)))
#
# db_students.close()

