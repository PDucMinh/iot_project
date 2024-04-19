import sys
from Adafruit_IO import MQTTClient
import time
import random
import tensorflow.python as tf
import uart as ua
# import keras as kr
import sever as sv
import numpy as np
from uart import *

AIO_FEED_IDs = ["aiot.temp" , "aiot.fan", "aiot.door", "aiot.humid"]
AIO_USERNAME = "PDomus"
AIO_KEY = "aio_vMlF59TMj7Peq5BAaCvF2INcQlTZ"
client = MQTTClient(AIO_USERNAME , AIO_KEY)

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)
    

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " feed_id id: " + feed_id)
    if feed_id == "aiot.fan":
        if payload == "1":
            writeSerial("F:1")
        elif payload == "0":
            writeSerial("F:0")
    elif feed_id == "aiot.door":
        if payload == "1":
            writeSerial("D:1")
        elif payload == "0":
            writeSerial("D:0")
    elif feed_id == "aiot.light":
        if  payload == "1":
            writeSerial("L:1")
        elif payload == "0":    
            writeSerial("L:0")


def connect_sever():
    client.on_connect = connected
    client.on_disconnect = disconnected
    client.on_message = message
    client.on_subscribe = subscribe
    client.connect()
    client.loop_background()

def publishData(topic, data):
    if (client.publish(topic, data)):
        print("Data publishing: " + topic + " value: " + data)
    # counter = 10
    # while True:
    #     counter = counter - 1
    #     if counter <= 0:
    #         counter = 10
    #         #TO DO
    #         print("Data is publishing")
    #         temp = random.randint(-50, 80)
    #         client.publish("sensor1", temp)


    #     time.sleep(1)
    #     pass

