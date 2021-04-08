def loop_time():
    import time
    for i in range(0,5):
        print(i)
        time.sleep(1)

def Open_COM():
    import serial
    ser = serial.Serial('COM1')
    print(ser.name)

def PyInit_draft():
    loop_time()