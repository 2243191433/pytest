import json
import random
import threading

import paho.mqtt.client as mqtt
import time

import redis as redis

client = mqtt.Client()

kwargs = {
    'host': 'dev.bewatec.com.cn',
    'port': 16379,
    'password': 'Bewatec@2022',
    'decode_responses': True,
    'retry_on_timeout': 3,
    'max_connections': 2048
}

pool = redis.ConnectionPool(**kwargs)

redis_client = redis.Redis(connection_pool=pool)


def on_connect(userdata, flags, rc):
    print("Connected with result code: " + str(rc))


def on_message(userdata, msg):
    print(msg.topic + " " + str(msg.payload))


wait_period = 2
send_count = 20
device_count = 2000


def onTask():
    for iter_num in range(device_count, 0, -1):
        test = threading.Thread(target=single_compare, args=(iter_num,))
        test.start()


# 开启多线程
def initialize():
    username_list = ["backend"]
    password = "5PibfhEhmoNXZcK2"
    client.username_pw_set(username_list[0], password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('dev.bewatec.com.cn', 31883, 600)


def single_compare(iter_num):
    pass_count = 0
    index = 0
    while (1):
        index = index + 1
        data = {
            "time": int(round(time.time() * 1000)),
            "heart": random.randrange(1, 100),
            "breath": random.randrange(1, 100),
            "move": 4,
            "state": 3
        }
        if iter_num < 10:
            ury = ('0' + str(iter_num))
        else:
            ury = str(iter_num)
        uri = '1052303300' + ury
        type = '10004'
        mqtt_data = json.dumps(data)
        client.publish('iot/up/type/' + type + '/uri/' + uri + '/data', mqtt_data, 0)
        time.sleep(wait_period)

        keys = redis_client.keys()

        key = 'device:' + type + ':' + uri + ':data'
        raw = redis_client.get(key)
        if raw == mqtt_data.replace(" ", ""):
            pass_count = pass_count + 1
        if send_count == index:
            print(pass_count / send_count)
            break


if __name__ == '__main__':
    initialize()
    onTask()
