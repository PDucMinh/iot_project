import sys
from Adafruit_IO import MQTTClient
import time
import random
import tensorflow.python as tf
# import keras as kr
import numpy as np
AIO_FEED_IDs = ["button1" , "button2"]
AIO_USERNAME = "PDucMinh"
AIO_KEY = "aio_RNvu55w4zziM0fErHzAoZTOdCiuC"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)
    

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " feed id: " + feed_id)

def connect_sever():
    client = MQTTClient(AIO_USERNAME , AIO_KEY)
    client.on_connect = connected
    client.on_disconnect = disconnected
    client.on_message = message
    client.on_subscribe = subscribe
    client.connect()
    client.loop_background()

    counter = 10
    while True:
        counter = counter - 1
        if counter <= 0:
            counter = 10
            #TO DO
            print("Data is publishing")
            temp = random.randint(-50, 80)
            client.publish("sensor1", temp)


        time.sleep(1)
        pass

