#coding=utf-8
import requests
#查询发布会接口
url = "http://127.0.0.1:8000/api/get_event_list/"
r = requests.get(url, params={'eid':'14'})

result = r.json()
print r.json()

#断言接口返回值
assert result['status'] ==200
assert result['message'] == "success"
assert result['data']['name'] =="xiaomi14"
#assert result['data']['address'] =="北京"

print('hello world')
