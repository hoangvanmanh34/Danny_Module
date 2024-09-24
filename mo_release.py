import sys
import requests
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class App:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        #print(self.kwargs)
        self.url = 'https://ap-cns.myfiinet.com:6443/MESAPI/api/MES/CallAPI'
        #'https://ap-cns.myfiinet.com:6443/MESAPI/api/MES/CallAPI'#---P06------
        #'http://10.228.110.120:8080/mesapi/api/mes/CallAPI'#---DV------
        if str(self.kwargs["API_TYPE"]) == '0':
            self.get_MO_release()
        elif str(self.kwargs["API_TYPE"]) == '1':
            self.get_Allpart_Information()
        elif str(self.kwargs["API_TYPE"]) == '2':
            self.station_Start_Mo()
        elif str(self.kwargs["API_TYPE"]) == '3':
            self.station_Input()
        elif str(self.kwargs["API_TYPE"]) == '4':
            self.station_Copyic()
        elif str(self.kwargs["API_TYPE"]) == '5':
            self.station_Oba()
        

    def get_MO_release(self):
        in_data = {
                "DATE":self.kwargs["DATE"]
            }
        
        data = {
                "IN_IP" : self.kwargs["IN_IP"], 
                "IN_DB" : self.kwargs["IN_DB"], 
                "IN_SP" : self.kwargs["IN_SP"], 
                "IN_EVENT" : self.kwargs["IN_EVENT"], 
                #"IN_DATA" : self.kwargs["IN_DATA"]
                "IN_DATA" : str(in_data)
            }
        #print('=============MO_RELEASE==============')
        #print(data)

        headers = {
                'Content-Type': 'application-json',
                'Authorization': 'Bear access_token'
            }

        response = requests.post(self.url, json = data, verify=False)#headers=headers

        print(response.text)
        
    def get_Allpart_Information(self):
        
        in_data = {
                "TR_SN":self.kwargs["TR_SN"]
            }
        data = {
                #"IN_IP" : self.kwargs["IN_IP"], 
                "IN_DB" : self.kwargs["IN_DB"], 
                "IN_SP" : self.kwargs["IN_SP"], 
                "IN_EVENT" : self.kwargs["IN_EVENT"], 
                "IN_DATA" : str(in_data)
            }

        #print(data)

        headers = {
                'Content-Type': 'application-json',
                'Authorization': 'Bear access_token'
            }

        response = requests.post(self.url, json = data, verify=False)#headers=headers

        print(response.text)
        
    def station_Start_Mo(self):
        
        in_data = {"MO":self.kwargs["MO"],
                   "MO_COPYIC":self.kwargs["MO_COPYIC"],
                    "MODEL_NAME":self.kwargs["MODEL_NAME"]
                   }

        data = { 
		    "IN_DB" : self.kwargs["IN_DB"], 
		    "IN_SP" : self.kwargs["IN_SP"], 
		    "IN_EVENT" : self.kwargs["IN_EVENT"], 
		    "IN_DATA" : str(in_data)
		}

        #print(data)

        headers = {
                'Content-Type': 'application-json',
                'Authorization': 'Bear access_token'
            }

        response = requests.post(self.url, json = data, verify=False)#headers=headers

        print(response.text)    
        
    def station_Input(self):

        
        in_data = {"TR_SN":self.kwargs["TR_SN"],
                    "MO_COPYIC":self.kwargs["MO_COPYIC"],
		    "MODEL_NAME":self.kwargs["MODEL_NAME"],
		    "P_SN":self.kwargs["P_SN"],
		    "VENDOR_CODE":self.kwargs["VENDOR_CODE"],
		    "QTY":self.kwargs["QTY"],
		    "MARKING":self.kwargs["MARKING"],
		    "SITE":self.kwargs["SITE"],
		    "MACHINE_ID":self.kwargs["MACHINE_ID"],
		    "CHECK_SUM":self.kwargs["CHECK_SUM"]}

        data = { 
		    "IN_DB" : self.kwargs["IN_DB"], 
		    "IN_SP" : self.kwargs["IN_SP"], 
		    "IN_EVENT" : self.kwargs["IN_EVENT"], 
		    "IN_DATA" : str(in_data)
		}

        #print(data)

        headers = {
                'Content-Type': 'application-json',
                'Authorization': 'Bear access_token'
            }

        response = requests.post(self.url, json = data, verify=False)#headers=headers

        print(response.text)
        
    def station_Copyic(self):

        in_data = {"TR_SN":self.kwargs["TR_SN"],
                   "CHECK_SUM":self.kwargs["CHECK_SUM"],
                    "MACHINE_ID":self.kwargs["MACHINE_ID"]
                   }

        data = { 
		    "IN_DB" : self.kwargs["IN_DB"], 
		    "IN_SP" : self.kwargs["IN_SP"], 
		    "IN_EVENT" : self.kwargs["IN_EVENT"], 
		    "IN_DATA" : str(in_data)
		}

        #print(data)

        headers = {
                'Content-Type': 'application-json',
                'Authorization': 'Bear access_token'
            }

        response = requests.post(self.url, json = data, verify=False)#headers=headers

        print(response.text)
        
    def station_Oba(self):

        
        in_data = {"TR_SN":self.kwargs["TR_SN"],
                   "CHECK_SUM":self.kwargs["CHECK_SUM"],
                    "EMP_NO":self.kwargs["EMP_NO"],
                    "ERROR_CODE":self.kwargs["ERROR_CODE"]
                   }

        data = { 
		    "IN_DB" : self.kwargs["IN_DB"], 
		    "IN_SP" : self.kwargs["IN_SP"], 
		    "IN_EVENT" : self.kwargs["IN_EVENT"], 
		    "IN_DATA" : str(in_data)
		}

        #print(data)

        headers = {
                'Content-Type': 'application-json',
                'Authorization': 'Bear access_token'
            }

        response = requests.post(self.url, json = data, verify=False)#headers=headers

        print(response.text)

def parse_args(args):
    kwargs = {}
    for arg in args:
        if '=' in arg:
            key, value = arg.strip().split('=', 1)
            kwargs[key] = value
    return kwargs

def main():
    if len(sys.argv)<4:
        sys.exit(1)
    #print(sys.argv)
    kwargs = parse_args(sys.argv[1:])
    app = App(**kwargs)

if __name__ == "__main__":
    main()
    '''
    app = App(API_TYPE = 0,
              IN_IP = '10.228.30.184',
              IN_DB = "SFC",
              IN_SP = "SFIS1.COPYIC",
              IN_EVENT = "GET_MO_RELEASED",
              IN_DATA = "{'DATE':'14092024'}",
              DATE = "14092024",
              MO = "",
              MO_COPYIC = "",
              MODEL_NAME = "",
              TR_SN = "",
              CHECK_SUM = "",
              MACHINE_ID = "")
    '''

    '''
API_TYPE=0 IN_IP='10.228.30.184' IN_DB="SFC" IN_SP="SFIS1.COPYIC" IN_EVENT="GET_MO_RELEASED" IN_DATA="{'DATE':'14092024'}" DATE="14092024",
              MO = "",
              MO_COPYIC = "",
              MODEL_NAME = "",
              TR_SN = "",
              CHECK_SUM = "",
              MACHINE_ID = ""
              '''


