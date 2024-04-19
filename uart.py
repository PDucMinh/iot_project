import serial.tools.list_ports
import sys
import time
import sever as sv
# socat -d -d pty,raw,echo=0 pty,raw,echo=0
def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        # print(port, "\n")
        strPort = str(port)
        print(strPort)
        if "com0com" in strPort:
        # if "USB" in strPort:
        # if "usbserial" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    # print(commPort)
    return commPort
    # pass
    # return "COM6"
    # return "/dev/pts/5"
    # pass

# if getPort() != "None":
ser = serial.Serial( port=getPort(), baudrate=9600)
print(ser)

def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    for i in range(len(splitData)):
        if splitData[i] == "H":
            print("Humid recieve: "+ splitData[i+1])
            sv.publishData("aiot.humid", splitData[i+1])
        elif splitData[i] == "T":
            print("Temp recieve: "+ splitData[i+1])
            sv.publishData("aiot.temp", splitData[i+1])
        
mess = ""
def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        # print(mess)
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]
# def onReceive():
#     feed, payload = sv.message()
#     if feed == "aiot.fan":
#         if payload == "1":
#             writeSerial("F:1#")
#         elif payload == "0":
#             writeSerial("F:0#")
#     elif feed == "aiot.door":
#         if payload == "1":
#             writeSerial("D:1#")
#         elif payload == "0":
#             writeSerial("D:0#")
#     elif feed == "aiot.light":
#         if  payload == "1":
#             writeSerial("L:1#")
#         elif payload == "0":    
#             writeSerial("L:0#")
def writeSerial(data):
    ser.write(str(data).encode("utf-8"))
    # print(data)