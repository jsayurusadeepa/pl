import requests
import pandas as pd
from fastapi import FastAPI
app = FastAPI()
endpoint = "https://dc0c7b7d-7fbd-4b52-9d73-ad40481e374f-dev.e1-us-east-azure.choreoapis.dev/qvaq/ordsgeneratedapiforpl/1.0.0/stud"
endpoint1 = 'http://localhost:8081/marks'
headers = {'Authorization':'Bearer eyJ4NXQiOiJZV1kxTm1Sa1pHSTVNekU0T0RCbFpEUmlNV0k0WldKbE5qRXhaV1ZpWmpFek1tTm1ORFUzWVEiLCJraWQiOiJNV1E1TldVd1lXWmlNbU16WlRJek16ZG1NekJoTVdNNFlqUXlNalZoTldNNE5qaGtNR1JtTnpGbE1HSTNaRGxtWW1Rek5tRXlNemhoWWpCaU5tWmhZd19SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0ZDUyNWZkZC04N2MzLTRiOTMtODMwMy0xYjk3YTZkZWViOWYiLCJhdXQiOiJBUFBMSUNBVElPTiIsImF1ZCI6Ik5EeFNDdDBmOGdyX3ZrdzZseWQ2X3JubjM4UWEiLCJuYmYiOjE2NzYyNTE2NzIsImF6cCI6Ik5EeFNDdDBmOGdyX3ZrdzZseWQ2X3JubjM4UWEiLCJzY29wZSI6ImRlZmF1bHQiLCJvcmdhbml6YXRpb24iOnsidXVpZCI6ImRjMGM3YjdkLTdmYmQtNGI1Mi05ZDczLWFkNDA0ODFlMzc0ZiJ9LCJpc3MiOiJodHRwczpcL1wvc3RzLmNob3Jlby5kZXY6NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjc2MjU1MjcyLCJpYXQiOjE2NzYyNTE2NzIsImp0aSI6ImM0NzRjMzYxLWRhZjUtNDEyZi04NDdjLTcxMjA5ZDM1MWJiMiJ9.f_VanVDk4IQCiKexl4fR333cM4tk7Z_lRsVsUAp7W3szOL17QasshQMPR8xGHONoZUEt-66xUZ3M5ExeJjY6jV25LI55oDJPGrhr8Tv20f18Mqj9w6sXJ8dXY6SINAUng1TLh4TYSfFmF205qLU3eKF7_PBzWQOjjvIjef-zVjA27BNtfozWkWudR3LaeLqGztlbauPh9X0t9hXZ6V3Yb7zhy59GH26BmtgfMO8WuPaCEKIxlLvW2e9nTUTXHRgE37Px3vhBIHpDL1N3HQtbdWuKN1WJugFNsMZuGRaHk-Qd5kmfABBcenC1jMtUCd1bwajHH7LoMPucPDpZ3SimejVfnyCZeIPbeWmmb_L_pgvGc_QLMzYPkXQOTqBf155MBNe5zgYeU5ir8BF5iFrKRHJEvQ2wGxY40YNezZPSdgs1L2EZPI6EG5kC9AUD3lXMeU47vPvgd122gKiR19_VGLyksPVPV1Kv5nBVMffTbLvf61bQ8LSxLhkgSDWZJrOSSWLTEx9yjZ8wLvQrtVqmiN86FQspiGtFPHuU6u5s2L8xGUmcTrrHYIouq4jz9hcL8VuGgZMTu5bNCM6qo24mETQAu8fj_ZSryXpjN917bqbz2xPMCPNQyTSyhR3hbtrjcCZPysWx9ECYJofceyyf9Z_Pt_cICe1oWS_jM59YpjU'}
url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}
payload = {"pl_stud_id":"10045","pl_stud_name":"TF1HQ0ENMV","pl_student_marks":87.06113000085513}
@app.get("/")
def hello_world():
    r1 = requests.post(endpoint1, json=payload)
    return {"Message":"OK"}