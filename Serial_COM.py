import serial
import time

class Serial_COM():
    def __init__(self, fixture):
        self.ser = None
        self.Fixture_COM = fixture

    def Open_COM(self):
        try:
            self.ser = serial.Serial(self.Fixture_COM)
            print(self.ser.name)
            time.sleep(0.2)
            self.ser.flush()
            # self.ser.open()
            # self.ser.set_input_flow_control(enable=False)
            # self.ser.set_output_flow_control(enable=False)
            print('COM opened')
        except Exception as e:
            print('Open COM fail')
            print(e)

    def Close_COM(self):
        try:
            self.ser.flush()
            time.sleep(0.2)
            self.ser.close()
        except:
            print('close com fail')
        return True

    def Get_in(self):
        data_de = ''
        if not self.ser.is_open:
            print('re-open com')
            self.Open_COM()
        # time.sleep(0.1)
        # self.ser.flush()
        time.sleep(0.1)
        data_de = self.ser.read_all().strip()
        # time.sleep(0.1)
        self.ser.flush()
        if data_de != b'':
            print(self.ser.name)
            print('Fixture:' + str(data_de))
        return data_de

    def Send_COM(self, scmd):
        try:
            print(scmd)
            end = '\x0d\x0a'
            self.ser.write(scmd.encode() + end.encode())  # +'\r\n')#
        except Exception as e:
            print('send to com fail')
            print(e)