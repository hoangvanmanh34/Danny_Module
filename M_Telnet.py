import time
import telnetlib

def Login_DUT(ipAddr, iport, iUserName, iPassword, iTimeout, strExpect):
    global tn
    try:
        tn = telnetlib.Telnet(ipAddr, port=iport, timeout=iTimeout)
        # res=tn.read_until(str(Login_Flag).encode(),iTimeout).decode('ascii')
        time.sleep(0.5)
        tn.write(iUserName.encode('ascii') + b"\r\n")
        time.sleep(0.5)
        # res = tn.read_until(b'Password :', iTimeout).decode('ascii')
        # if res.find('Password')>=0:
        # tn.read_until(b"Password: ")
        tn.write(iPassword.encode('ascii') + b"\r\n")
        time.sleep(2)
        res = tn.read_until(strExpect.encode('ascii'), iTimeout).decode('ascii')
        return True, res
    except Exception as e:
        return False, str(e)

def Send_Command(strCMD, iTimeout, strExpect):
    try:
        tn.write(strCMD.encode())
        # time.sleep(2)
        res = tn.read_until(strExpect.encode(), iTimeout)#.decode(errors="ignore")
        return True, res
    except Exception as e:
        return False, str(e)

#print(Login_DUT('192.168.1.254', 'superman','superman', 1, '=>'))
#print(Send_Command("env get var _MACADDR",1,"{superman}=>"))