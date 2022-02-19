# If you want to buy, please contact the following information.
# LINE:chuan.9209

import requests, json

class QRlogin:

    def __init__(self):
        self.HOST = "http://chuan-ldts.com.tw"
        self.LOGIN_QR = "/LoginQR"
        self.CREATE_NEW_PROGRAM = "/CreateNewProgram"
        self.GET_QRCODE = "/getQRcode"
        self.GET_PINCODE = "/getPinCode"
        self.GET_AUTHTOKEN = "/getAuthToken"

        self.JSON = {
            "username": "",                   # Insert your username
            "password": "",                   # Insert your password
            "device": "CHROME",               # Insert your Device. ex. CHROME, IOS, LITE, MAC
            "system_name": "Chuan.LoginQR"    # Insert your systemName
        }

    def CreateNewProgram(self):
        resp = requests.post(url=self.HOST+self.LOGIN_QR+self.CREATE_NEW_PROGRAM, json=self.JSON)
        response = resp.json()
        if response["LOGIN_STATUS"] == True:
            return response["LOGIN_CODE"]
        else:
            return response["REASON"]

    def getQRcode(self, code):
        self.JSON["code"] = code
        resp = requests.post(url=self.HOST+self.LOGIN_QR+self.GET_QRCODE, json=self.JSON)
        response = resp.json()
        if response["GET_STATUS"] == True:
            return response["QRCODE"]
        else:
            return response["REASON"]
    
    def getPinCode(self, code):
        self.JSON["code"] = code
        resp = requests.post(url=self.HOST+self.LOGIN_QR+self.GET_PINCODE, json=self.JSON)
        response = resp.json()
        if response["GET_STATUS"] == True:
            return response["PINCODE"]
        else:
            return response["REASON"]

    def getAuthToken(self, code):
        self.JSON["code"] = code
        resp = requests.post(url=self.HOST+self.LOGIN_QR+self.GET_AUTHTOKEN, json=self.JSON)
        response = resp.json()
        if response["GET_STATUS"] == True:
            return response["AUTH_TOKEN"]
        else:
            return response["REASON"]

if __name__ == "__main__":
    qrlog = QRlogin()
    code = qrlog.CreateNewProgram()
    qr = qrlog.getQRcode(code)
    print(qr)
    pin = qrlog.getPinCode(code)
    print(pin)
    token = qrlog.getAuthToken(code)
    print(token)
    