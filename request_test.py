# coding=utf-8
import requests
from io import BytesIO, StringIO


reponse_url = requests.get('http://jst.train.going-link.com/images/newUI/navbar_userhead_44px.png?v=1.0')
print(reponse_url.headers)
# print(reponse_url.content.decode())
# print(reponse_url.text)
f = BytesIO(reponse_url.content)


