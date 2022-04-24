import os
import logging
from requests import Session
from bs4 import BeautifulSoup as bs
from http.client import HTTPConnection

def debug_requests_on():
    '''Switches on logging of the requests module.'''
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

def get_accid(raw):
    soup = bs(raw.text, "html.parser")
    data = soup.find_all("td", attrs={"width":"50%",
                                      "class":"bluetxt"})
    acc_id = ''
    for x in data:
        if x.get_text().isdecimal():
            acc_id = x.get_text()
    return acc_id

def get_months(raw):
    soup = bs(raw.text, "html.parser")
    data = soup.find_all("input", attrs={"type":"checkbox",
                                         "name":"Month",
                                         "id":"checkMonth"})
    months_lst=[]
    for x in data:
        months_lst.append(x["value"])
    return months_lst

def raw_output():
    session_lst = []
    day_lst = []
    for x in range(1, 54):
        session_lst.append(str(x))
    for i in range(1, 8):
        day_lst.append(str(i))

    with Session() as s:
        login_data = {
            "txtNRIC": os.environ.get("USERNAME"),
            "txtpassword": os.environ.get("PASSWORD"),
            "ca": "true",
            "btnLogin": "ACCESS+TO+BOOKING+SYSTEM"
        }

        site = s.post("http://www.bbdc.sg/bbdc/bbdc_web/header2.asp", data=login_data)
        raw_accid = s.get("http://www.bbdc.sg/bbdc/b-default.asp")
        acc_id = get_accid(raw_accid)
        s.post("http://www.bbdc.sg/bbdc/b-selectTPDSModule.asp", data={"optTest":"3", "btnSubmit":"Submit"})
        raw_months = s.get("http://www.bbdc.sg/bbdc/b-TPDSBooking.asp")
        months = get_months(raw_months)
        form_data = {"accId": acc_id,
                     "Month": months[:4],
                     "Session": session_lst,
                     "allSes": "on",
                     "Day": day_lst,
                     "allDay": "",
                     "defPEVenue": "1",
                     "optVenue": "1"}
        avail = s.post("http://www.bbdc.sg/bbdc/b-TPDSBooking1.asp", data=form_data)
        # with open("index.html", "w") as f:
        #     f.write(avail.text)
        return avail.text

def parse_soup(soup):
    data = soup.find_all("td", attrs={"align":"center",
                                       "bgcolor":"white",
                                        "class":"txtbold"})

    available_list = []
    for x in data:
        raw = x["onmouseover"].split(",")
        available_list.append([raw[2].replace('"','')[1:],raw[4].replace('"',''),raw[5].replace('"','')])

    formatted_list = {}
    for x in available_list:
        if x[0] not in formatted_list:
            formatted_list[x[0]] = f'{x[1]} - {x[2]}'
        else: formatted_list[x[0]] += f'\n{x[1]} - {x[2]}'
    return formatted_list

def obtain_dates():
    debug_requests_on()
    raw_dates = raw_output()
    soup = bs(raw_dates, "html.parser")
    date_list = parse_soup(soup)
    return date_list