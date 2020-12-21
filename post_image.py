import requests
import base64
with open('volv.jpg', 'rb') as f:
    im_b64 = base64.b64encode(f.read()) #bytes into ASCII characters (we have 64 characters that represent numbers)

payload = {'id': '123', 'type': 'jpg', 'box': [0, 0, 100, 100], 'image': im_b64}

r = requests.post("http://",data=payload)
# requests.post(url, data={key: value}, json={key: value}, args)
print(r)