import requests


r = requests.get('http://www.zhiguyichuan.com')
print(r.status_code)
print(r.text)