import requests
session = requests.Session()
print(session.cookies.get_dict())
login_data = {
    "txtNRIC": "857G04072001",
    "txtpassword": "123456",
    "ca": "true",
    "btnLogin": "ACCESS+TO+BOOKING+SYSTEM"
}

homepage = session.post("http://www.bbdc.sg/bbdc/bbdc_web/header2.asp", login_data)
# homepage = session.get("https://info.bbdc.sg/members-login")
print(homepage.request.headers)
print(homepage.text)

# for k in homepage.cookies:
#     print(k.name, k.value)
# print(homepage.text)
