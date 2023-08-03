import json

import pytest
import requests
import  re

class TestBwtc:

    def setup(self):
        print("用例执行")

    def teardown(self):
        print("执行完成")
    ID=""
    deviceId=""
    def test_login(self):
         # 发送get请求
        url = "http://dev.bewatec.com.cn:28000/api/Auth/login"
        data = {
            "username": "18386110564",
            "secret": "shangHONG1234"
        }
        rep = requests.request("post",url, json=data)
        print(rep.json())
        print(rep)
        token = rep.json()['data']['token']
        global authorized
        authorized="Bearer"+" "+token
    def test_passset(self):
        url = "http://dev.bewatec.com.cn:28000/api/User/password/set"
        data = {
        "secret": "shangHONG1234"
     }
        headers = {"Content-Type": "application/json",
                   "accept": "text / plain",
                   "Authorization": authorized
               }
        rep = requests.request("put",url, json=data, headers=headers)
        print(rep)
        print(authorized)
        print(rep.text)
    def  test_addDevice(self):
        url="http://dev.bewatec.com.cn:28000/api/DeviceInfo"
        data={
               "uri": "105221014168",
               "deviceType": 10004
               }
        headers = {"Content-Type": "application/json",
                   "accept": "text / plain",
                   "Authorization": authorized
                   }
        req=requests.request("post",url,json=data,headers=headers)
        print(req)
        print(req.text)
    def test_udpDevice(self):
        url="http://dev.bewatec.com.cn:28000/api/DeviceInfo"
        data={
            "id":"00000000-0000-0000-0000-000000000000",
            "name": "string"
        }
        headers={
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("post",url,json=data,headers=headers)
        print(res)
    def test_delDevice(self):
        url="http://dev.bewatec.com.cn:28000/api/DeviceInfo"
        data={
            "id":"00000000-0000-0000-0000-000000000000"
        }
        headers={
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res = requests.request("delete",url,json=data,headers=headers)
        print(res)
    def test_getDeices(self):
        url="http://dev.bewatec.com.cn:28000/api/DeviceInfo"
        data={
            "deviceid":"00000000-0000-0000-0000-000000000000"
        }
        headers = {
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("get",url,json=data,headers=headers)
        print(res)
    def test_getOtaVersion(self):

        url="http://dev.bewatec.com.cn:28000/api/Ota/devicetype/10004/lastversion"
        headers={"Content-Type": "application/json",
                 "accept": "text / plain",
                 "Authorization": authorized
                 }
        res=requests.request("get",url,headers=headers)
        print(res)
    def test_otaSenji(self):
        url="http://dev.bewatec.com.cn:28000/api/Ota/upgrade"
        data={
            "uri": "string",
            "version": "string"
        }
        headers={
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("post",url,json=data,headers=headers)
        print(res)
    def test_devCommand(self):
        url="http://dev.bewatec.com.cn:28000/api/Ota/105221014168/command"
        data={
            "height": 0,
            "weight": 0,
            "posture": {
                "mode": 0,
                "alternateInterval": 0
            },
            "turnOver": {
                "mode": 0,
                "alternateInterval": 0
            }
        }
        headers={
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("post",url, json=data,headers=headers)
        print(res)
    def test_sleepData(self):
        url="http://dev.bewatec.com.cn:28000/api/SleepReport/105221014064/sleepdata"
        data={
            "data":""
        }
        headers={
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.get(url,json=data,headers=headers)
        print(res)
    def test_sleepReport(self):
        url="http://dev.bewatec.com.cn:28000/api/SleepReport/105221014064/report"
        data={
            "date":""
        }
        headers={
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.get(url,json=data,headers=headers)
        print(res)
    def test_sleepDate(self):
        url="http://dev.bewatec.com.cn:28000/api/SleepReport/105221014064/date"
        headers={
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.get(url,headers=headers)
        print(res)

    def test_passSet(self):
        url="http://dev.bewatec.com.cn:28000/api/User/password/set"
        data={
            "secret": "string"
        }
        headers={
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.put(url,json=data,headers=headers)
        print(res)
    def test_passUdp(self):
        url="http://dev.bewatec.com.cn:28000/api/User/password/upd"
        data={
             "oldSecret": "string",
             "secret": "string"
             }
        heasers={
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("put",url,json=data,headers=heasers)
        print(res)
    def test_userInfoSet(self):
        url="http://dev.bewatec.com.cn:28000/api/User/userInfo/set"
        data={
              "birthDay": "2023-04-20",
              "sex": 0,
              "height": 0,
              "weight": 0,
              "province": "string",
              "city": "string",
              "timeZone": 0
             }
        headers={
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.put(url,json=data,headers=headers)
        print(res)
    def test_userInfoUpd(self):
        url="http://dev.bewatec.com.cn:28000/api/User/userInfo/upd"
        data={
            "birthDay": "2023-04-20",
            "sex": 0,
            "height": 0,
            "weight": 0,
            "timeZone": 0
            }
        headers={
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.put(url,json=data,headers=headers)
        print(res)
    def test_getUserInfo(self):
        url="http://dev.bewatec.com.cn:28000/api/User"
        headers={
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("get",url,headers=headers)
        print(res)
    def test_displaynameUpd(self):
        url="http://dev.bewatec.com.cn:28000/api/User/displayName"
        data={
            "displayName": "string"
        }
        headers={
            "Content-Type": "application/json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("put",url,json=data,headers=headers)
        print(res)
    def test_register(self):
        url="http://dev.bewatec.com.cn:28000/api/Auth/register"
        data={
                "username": "string",
                "secret": "string"
            }
        headers={
            "accept": "text / plain",
            "Content-Type": "application/json-patch+json"
        }
        res = requests.request("post",url, json=data, headers=headers)
        print(res)
        print(res.text)
    def test_deviceAdd(self):     #设备添加
        url="http://dev.bewatec.com.cn:28000/api/DeviceInfo"
        data={
                "uri": "string",
                "deviceType": 0
            }
        headers={
            "Content-Type": "application/json-patch+json",
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("post",url,json=data,headers=headers)
        print(res)
        print(res.text)
    def test_groupList(self):
        url="http://dev.bewatec.com.cn:28000/api/Group/list"
        headers={
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("get",url,headers=headers)
        print(res)
        print(res.json())
        TestBwtc.ID=re.search('id":"(.*?)",',res.text)[1]
        print(TestBwtc.ID)
    def test_groupInfo(self):
        url="http://dev.bewatec.com.cn:28000/api/Group?Id="+TestBwtc.ID
        headers = {
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("get",url,headers=headers)
        print(res)
        print(res.text)

    def test_deviceLidtofGroup(self):               #分组设备
        url="http://dev.bewatec.com.cn:28000/api/Group/"+TestBwtc.ID+"/deviceList"
        headers = {
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("get",url,headers=headers)
        TestBwtc.deviceId = re.search('id":"(.*?)",',res.text)[1]
        print(res)
        print(res.text)

    def test_udpGroup(self):         #修改分组
        url=url="http://dev.bewatec.com.cn:28000/api/Group?Id="+TestBwtc.ID
        data={
            "name": "string"
             }
        headers = {
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("put",url,json=data,headers=headers)
        print(res.text)

    def test_statisticsCount(self):          #首页各类预警信息
        url="http://dev.bewatec.com.cn:28000/api/Warn/statisticsCount"
        headers = {
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("get",url,headers=headers)
        print(res.text)

    def test_warnList(self):      #获取预警列表
        url="http://dev.bewatec.com.cn:28000/api/Warn/list?page=1&size=10"
        headers = {
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("get",url,headers=headers)
        print(res.text)

    def test_warnView(self):         #获取图标
        url="http://dev.bewatec.com.cn:28000/api/Warn/chart/" \
            "88dd2092-08c1-4e78-859a-d12188b7ea84/2023-05-23%200%3A00%3A00%2B08%3A00"
        headers = {
            "accept": "text / plain",
            "Authorization": authorized
        }
        res = requests.request("get",url, headers=headers)
        print(res.text)

    def test_shareUser(self):          #获取分享设备的用户数
        url="http://dev.bewatec.com.cn:28000/api/Share/device/0b6"+TestBwtc.deviceId+"/shareUser"
        headers = {
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("get",url,headers=headers)
        print(res.text)

    def test_shareDevice(self):        #分享设备
        url="http://dev.bewatec.com.cn:28000/api/Share/device/"+TestBwtc.deviceId+"/shareUser"
        headers = {
            "accept": "text / plain",
            "Authorization": authorized
        }
        res=requests.request("post",url,headers=headers)
        print(res.text)

    def test_delShareUser(self):        #删除设备的分享用户
        url="http://dev.bewatec.com.cn:28000/api/Share/device/"+TestBwtc.deviceId+"/shareUser?"

        headers = {
            "accept": "text / plain",
            "Content-Type": "application/json-patch+json",
            "Authorization": authorized
        }
        res=requests.request("delete",url,headers=headers)
        print(res.text)
