import requests
import os
class Downloader:
    def __init__(self,path):
        self.image_path = path
        self.__template_url = "http://карта-онлайн.рф/uploads/photos/stud/{}"

    def download(self,photo_id):
        url = self.__template_url.format(photo_id)
        #print(url)
        response = requests.get(url, stream=True)
        if not response.ok:
            #print(response)
            return False

        handle = open(os.path.join(self.image_path,photo_id),'wb')

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
        return True

