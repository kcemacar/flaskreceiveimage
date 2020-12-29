import requests
import base64
import time
import os

class Image:
    def __init__(self, file_name):
        self.fname = file_name

    def encode(self):
        with open(self.fname, 'rb') as f:
            self.im_b64 = base64.b64encode(f.read()) #bytes into ASCII characters (we have 64 characters that represent numbers)

    def post(self,url):
        self.url = url
        self.payload = {'id': '123', 'type': ('jpg','png'), 'box': [0, 0, 100, 100], 'image': self.im_b64}
        self.r = requests.post(self.url,data=self.payload)
        # requests.post(url, data={key: value}, json={key: value}, args)
        print(self.r)
        
arr =os.listdir("resource")
print (arr)


for image in arr:
    print(image)
    time.sleep(2)
    img = Image("resource/"+image)
    img.encode()
    img.post("ipadress")
