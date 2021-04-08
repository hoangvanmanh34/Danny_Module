from pysnmp.hlapi import *

def Unlock_DUT(DUT_IP,strCMD):
    print("Unlock Factory Mode")
    strResult = []
    errorIndication, errorStatus, errorIndex, varBinds = next(
        setCmd(SnmpEngine(),
               CommunityData('public', mpModel=1),
               UdpTransportTarget((DUT_IP, 161)),
               ContextData(),
               #ObjectType(ObjectIdentity('1.3.6.1.4.1.4413.2.99.1.1.1.2.1.2.1'), OctetString('username')),
               ObjectType(ObjectIdentity(strCMD), OctetString('password'))
               #ObjectType(ObjectIdentity('1.3.6.1.4.1.4684.80.1.6.0'), Integer(2))  # open session
               )
    )
    for varBind in varBinds:
        #print(varBind)
        strResult.append(str(varBind))
        return strResult

def Check_Info(DUT_IP,strCMD):
    print("Get Info")
    strResult=[]
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData('public'),
               UdpTransportTarget((DUT_IP, 161)),
               ContextData(),
               #ObjectType(ObjectIdentity('1.3.6.1.4.1.4413.2.99.1.1.1.2.1.2.1')),
               ObjectType(ObjectIdentity(strCMD))
               )
    )
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            #print(varBind)
            strResult.append(str(varBind))
            return strResult

def Send_CMD(DUT_IP,strCMD,iValue):
    print("Set Command")
    strResult = []
    errorIndication, errorStatus, errorIndex, varBinds = next(
        setCmd(SnmpEngine(),
               CommunityData('public', mpModel=1),
               UdpTransportTarget((DUT_IP, 161)),
               ContextData(),
               #ObjectType(ObjectIdentity('1.3.6.1.4.1.4413.2.99.1.1.1.2.1.2.1'), OctetString('password')),
               #ObjectType(ObjectIdentity('1.3.6.1.4.1.4684.80.1.6.0'), Integer(1)),
               ObjectType(ObjectIdentity(strCMD), Integer(iValue))
               )
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            #print(varBind)
            strResult.append(str(varBind))
            return strResult


#print(Unlock_DUT('192.168.100.1','1.3.6.1.4.1.4413.2.99.1.1.1.2.1.2.1'))
#print(Check_Info('192.168.100.1','1.3.6.1.4.1.4413.2.99.1.1.2.1.4.1.2.1'))