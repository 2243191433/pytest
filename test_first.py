import requests as requests

requests.get()
rep = requests.request()
# 返回字符串
print(rep.text)
print(rep.status_code)  # 状态码
# 返回字典格式
print(rep.content)
# 返回json
print(rep.json)
# 返回状态信息
print(rep.reason)
# 返回cookie信息
print(rep.cookies)
# 返回编码格式
print(rep.encoding)
# 返回响应头
print(rep.headers)
