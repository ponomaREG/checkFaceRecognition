import threading
import time

class Thr(threading.Thread):
    def __init__(self,downloader,dbHelper,step,beginPosition):
        threading.Thread.__init__(self)
        self._downloader = downloader
        self._dbHelper = dbHelper
        self._step = step
        self._beginPosition = beginPosition
        self._counter = 0
        self._counter_success = 0
        self._size = self._dbHelper.size()

    def megaLogginSystem(self,iterat):
        print("Thread:{} //Percent:{}, Number:{}, Success:{}, PercentOfSuccessResults:{}".format(self._beginPosition,
                                                                                      round(self._counter/self._size,3),
                                                                                      iterat,
                                                                                      self._counter_success,
                                                                                      round(self._counter_success/self._counter,2)))


    def run(self) -> None:
        for i in range(self._beginPosition,self._size,self._step):
            photo = self._dbHelper.getAt(i)[3]
            if self._downloader.download(photo) is False:
                time.sleep(0.5)
            else:
                self._counter_success+=1
            self._counter +=1
            self.megaLogginSystem(i)