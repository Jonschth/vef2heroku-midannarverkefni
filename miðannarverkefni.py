import json
from bottle import route, run , template, static_file
import requests

main_api = "http://apis.is/petrol"

def dags(ar,man,da):
    if man == "01":
        manstr="januar"
    elif man == "02":
        manstr="febrúar"
    elif man == "03":
        manstr="mars"
    elif man == "04":
        manstr="apríl"
    elif man == "05":
        manstr="mai"
    elif man == "06":
        manstr="juni"
    elif man == "07":
        manstr="juli"
    elif man == "08":
        manstr="agust"
    elif man == "09":
        manstr="september"
    elif man == "10":
        manstr="október"
    elif man == "11":
        manstr="nóvember"
    elif man == "12":
        manstr="desember"
    return  da+"."+manstr+" "+ar



def GetInfo():
    url = main_api
    json_data = requests.get(url).json()
    return json_data

gogn=GetInfo()




mydict_bensin={}
mydict_disel={}


for r in range(19):
    lina=gogn["results"][r]
    mydict_bensin.update({lina["name"]:[lina["company"],lina["bensin95"]]})
    mydict_disel.update({lina["name"]:[lina["company"],lina["diesel"]]})


ar=gogn["timestampPriceCheck"][0:4]
man=gogn["timestampPriceCheck"][5:7]
da=gogn["timestampPriceCheck"][8:10]
print(dags(ar,man,da))


fjöldi = 2



@route('/')
def serve_homepage():
    return template('disp_table',rows_1 = mydict_bensin, rows_2=  mydict_disel, cases = fjöldi, dagsetning = dags(ar,man,da))

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./')



run(host="localhost", port=8080, debug=True)


