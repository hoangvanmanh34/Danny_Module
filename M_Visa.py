import time
import pyvisa

class M_Visa:
    def __init__(self):
        self.Powermeter_inst = None
        self.Counter_inst = None
        self.visa_dll = 'c:/windows/system32/visa32.dll'
        print('Request to c:/windows/system32/visa32.dll')

    def Init_PowerMeter(self, Power_Meter_Addr, Conn_Type = "Ethernet"):
        cmd_list = [["SWE1:TIME 0.000045",0], ["OUTP:TRIG:STAT ON",0], ["TRIG:SOUR INT1",0], ["AVER:COUN:AUTO OFF",0],
                    ["AVER:COUN 16",0], ["FREQ 2.437GHz",0], ["AVER:SDET ON",0]]
        Log_Test = ''
        try:
            rm = pyvisa.ResourceManager(self.visa_dll)
            if Conn_Type == "GPIB":
                self.Powermeter_inst = rm.open_resource("GPIB0::" + Power_Meter_Addr + "::INSTR")
            else:
                self.Powermeter_inst = rm.open_resource(("TCPIP0::" + Power_Meter_Addr + "::inst0::INSTR"))
            for cmd in cmd_list:
                self.Powermeter_inst.write(cmd[0])
                Log_Test += cmd[0]
                time.sleep(cmd[1])
            print('********************************')
            print('init pass')
            Log_Test += 'power meter init pass\n'
            return True, Log_Test
        except Exception as e:
            Log_Test += "Exception:" + str(e) + '\n'
            return False, Log_Test

    def Get_Power(self, get_time=3):
        Log_Test = ''
        data = None
        cmd_list = [['INIT:CONT OFF',0.5], ['INIT:CONT ON',1]]
        cmd_get_pwr = 'FETC:POW:AC?'
        power = []
        try:
            for cmd in cmd_list:
                self.Powermeter_inst.write(cmd[0])
                Log_Test += cmd[0]
                time.sleep(cmd[1])
            for i in range(get_time):
                daaa = self.Powermeter_inst.query(cmd_get_pwr)
                time.sleep(0.5)
                power.append(float(daaa.split(',')[0]))
            print(power)
            for i in range(get_time):
                data += power[i]
            data = (data / get_time)
            print('********************************')
            print(str(round(data, 2)))
            return True, Log_Test, round(data, 2)
        except Exception as e:
            Log_Test += "Exception:" + str(e) + '\n'
            return False, Log_Test, round(data, 2)

    def Init_Counter(self,Counter_Addr, Conn_Type = "Ethernet"):
        cmd_list = [['*RST',0], ['*CLS',0], ['INP:IMP 50',0]]
        Log_Test = ''
        try:
            rm = pyvisa.ResourceManager(self.visa_dll)
            if self.Conn_Type == "GPIB":
                self.Counter_inst = rm.open_resource("GPIB0::" + self.Counter_Addr + "::INSTR")
            else:
                self.Counter_inst = rm.open_resource(("TCPIP0::" + self.Counter_IP + "::inst0::INSTR"))
            for cmd in cmd_list:
                self.Counter_inst.write(cmd[0])
                Log_Test += cmd[0]
                time.sleep(cmd[1])
            print('********************************')
            print('init pass')
            Log_Test += 'counter meter init pass\n'
            return True, Log_Test
        except Exception as e:
            Log_Test += 'counter meter init fail\n'
            return False, Log_Test

    def Get_Frequency(self):
        Log_Test = ''
        freq = None
        try:
            time.sleep(2)
            freq = 0
            for i in range(3):
                freq = self.Counter_inst.query(':MEASure:FREQuency? (@2)')
                time.sleep(0.5)
            freq = float(freq.split('\n')[0])
            print('********************************')
            print(freq)
            return True, Log_Test, freq
        except Exception as e:
            Log_Test += "Exception:" + str(e) + '\n'
            return False, Log_Test, freq