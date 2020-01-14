# search_express
# created by yub at 2019/12/17
import requests, json, hashlib


# def search(num):
#     url1 = 'http://www.kuaidi100.com/autonumber/auto？num={}&key={}'  # 提取公司信息的URL
#     com = requests.get(url1.format(num))  # 拼接快递单号到URL，并调用单号
#     if com.status_code == 200:
#         inf = json.loads(com.content.decode('utf-8'))
#         print(inf)
# customer = '794630540E9D7EF77AFB4EE3363E4BF0'
# key = 'QkSaLiuf7128'
# str = customer + key
# print(str)
# str1 = str.encode('utf-8')
# print(str1)
# m = hashlib.md5()
# m.update(str1)
# str_md5_1 = m.hexdigest()
# str_md5 = hashlib.md5(str1).hexdigest()
# print(str_md5)
# print(str_md5_1.upper())


# search(71134378777965)
url = 'http://www.kuaidi100.com/autonumber/auto？num={71134378777965}&key={QkSaLiuf7128}'
com = requests.get(url)  # 拼接快递单号到URL，并调用单号
# if com.status_code == 200:
inf = json.loads(com.content.decode('utf-8'))
print(inf)