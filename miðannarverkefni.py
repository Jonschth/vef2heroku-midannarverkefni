from sys import argv
import bottle
from bottle import *
bottle.debug(True)
import json
from bottle import route, run , template, static_file
import requests

main_api = "http://apis.is/petrol"

def felaga_dict(dict, felag):
    nytt_dict={}
    for r in dict:
        if dict[r][0]==felag:
            nytt_dict.update({r:[dict[r][0],dict[r][1]]})
    return nytt_dict


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


#taka gögnin úr json

mydict_bensin={}
mydict_disel={}
fjoldi_bensinstodva=len(gogn["results"])
listi_soluadilar=[]


for r in range(fjoldi_bensinstodva):
    lina=gogn["results"][r]
    mydict_bensin.update({lina["name"]:[lina["company"],lina["bensin95"]]})
    mydict_disel.update({lina["name"]:[lina["company"],lina["diesel"]]})
    if lina["company"] not in listi_soluadilar:
        listi_soluadilar.append(lina["company"])


#raða dictionary eftir verðinu

def besta_verd(mydict_bensin,mydict_disel):
    new_bensin=sorted(mydict_bensin.items(), key=lambda t:t[1])
    mydict_bensin={}
    for i  in range(len(new_bensin)):
        mydict_bensin.update({new_bensin[i][0]:[new_bensin[i][1][0],new_bensin[i][1][1]]})
    besta_verd={new_bensin[0][0]:[new_bensin[0][1][0],new_bensin[0][1][1]]}


    new_disel=sorted(mydict_disel.items(),  key=lambda t:t[1])
    mydict_disel={}
    for i in range(len(new_disel)):
        mydict_disel.update({new_disel[i][0]:[new_disel[i][1][0],new_disel[i][1][1]]})
    besta_verd.update({new_disel[0][0]+"_d":[new_disel[0][1][0],new_disel[0][1][1]]})
    print(new_disel[0][0])
    return besta_verd




# dagsetningin sóot
ar=gogn["timestampPriceCheck"][0:4]
man=gogn["timestampPriceCheck"][5:7]
da=gogn["timestampPriceCheck"][8:10]

fjöldi = 2



@route('/')
def serve_homepage():
    return template('disp_table',sa=listi_soluadilar,rows_1 = mydict_bensin,
                    rows_2=  mydict_disel, cases = fjöldi, dagsetning = dags(ar,man,da),
                    besta=besta_verd(mydict_bensin,mydict_disel))


@route('/<felag>')
def serve_felag(felag):
    return template('felaga_table',fjoldi_st=len(felaga_dict(mydict_bensin,felag)),rows_1 = felaga_dict(mydict_bensin,felag),
                    rows_2=  felaga_dict(mydict_disel,felag), cases = fjöldi, dagsetning = dags(ar,man,da))












@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./')


run(host="localhost", port=8080, debug=True)



