import paramiko
import telnetlib
import time
import sys
import os
import glob
import re
import datetime
import subprocess



client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

buffer = ""
#conn=None

def Login_DUT(ip, port, username, password, response):
    global conn
    buffer = ""
    try:
        client.connect(ip, port, username, password, timeout=20)
    except Exception as e:
        print('Login FAIL')
        print(e)
        return False, 'Login FAIL'
    conn = client.invoke_shell()
    time.sleep(1)
    for i in range(0, 100):
        buffer = buffer + conn.recv(4096).decode(errors='ignore')
        print(buffer)
        if response in buffer:
            return True, buffer
        else:
            time.sleep(0.1)
    return False, buffer


def Send_Command(cmd, delay=2, expect="#"):
    conn.send(cmd + '\n')
    buffer = b''
    buf = ''
    #time.sleep(delay)
    for i in range(0, 900):
        buffer = (buffer) + conn.recv(4096)  # .decode(errors='ignore')
        # print(buffer)
        for j in buffer.split(b'\r\n'):
            #print(j.decode())
            buf += j.decode()+'\n'
        if expect in str(buffer):
            return True, buf
        else:
            time.sleep(0.1)
    return False, buf


def Close():
     client.close()

#Login_DUT("192.168.10.1",22,"root","root","#")
#print(Send_Command("ethctl eth1 media-type",1))