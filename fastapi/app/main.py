import requests
import pandas as pd
from fastapi import FastAPI
app = FastAPI()
endpoint = "https://dc0c7b7d-7fbd-4b52-9d73-ad40481e374f-dev.e1-us-east-azure.choreoapis.dev/qvaq/ordsgeneratedapiforpl/1.0.0/stud"
endpoint1 = 'http://localhost:8081/marks'
headers = {'Authorization':'Bearer eyJ4NXQiOiJZV1kxTm1Sa1pHSTVNekU0T0RCbFpEUmlNV0k0WldKbE5qRXhaV1ZpWmpFek1tTm1ORFUzWVEiLCJraWQiOiJNV1E1TldVd1lXWmlNbU16WlRJek16ZG1NekJoTVdNNFlqUXlNalZoTldNNE5qaGtNR1JtTnpGbE1HSTNaRGxtWW1Rek5tRXlNemhoWWpCaU5tWmhZd19SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0ZDUyNWZkZC04N2MzLTRiOTMtODMwMy0xYjk3YTZkZWViOWYiLCJhdXQiOiJBUFBMSUNBVElPTiIsImF1ZCI6Ik5EeFNDdDBmOGdyX3ZrdzZseWQ2X3JubjM4UWEiLCJuYmYiOjE2NzYyMTc2NTEsImF6cCI6Ik5EeFNDdDBmOGdyX3ZrdzZseWQ2X3JubjM4UWEiLCJzY29wZSI6ImRlZmF1bHQiLCJvcmdhbml6YXRpb24iOnsidXVpZCI6ImRjMGM3YjdkLTdmYmQtNGI1Mi05ZDczLWFkNDA0ODFlMzc0ZiJ9LCJpc3MiOiJodHRwczpcL1wvc3RzLmNob3Jlby5kZXY6NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjc2MjIxMjUxLCJpYXQiOjE2NzYyMTc2NTEsImp0aSI6IjkxMjBjNGI1LTk2YjktNGEzZi1iYmY4LTQ2OThhMjBlNGFiYSJ9.eu1HIY12caRcq9er0cx_B9Q1SdbQwSKMih3cNRK4uErBiKlo1AjIRK2ENYW9nPZ6l7smLuf8aeJiombDQAqRdDji-PddXz0IiWhVtZNtEt7ElRG7geLCQbuUtQa3cSIKWAXLW86WSF2UihjLoMM1S9NT9qDSC7SMecvDp9B6cLcrUqXkJipV7drknFDuS6_3QSE_MDBXkccgBSnFhQMaH5goaVcT0k65ww-453-13ZrK3MyywNh2h6WLBHoZBrg7Z2EWNDZ0uhrQ1iI64FTczgAuF4aKtQWBtfzKzqpfLsKvjs_S-wGlhDR5S3z2MYozvDNzoCcv1jzTYHAIUCT-VSrV-_L_zBoLER4WIayPGwamVIrJK3ljBiQ7Z8dZy4OCXVkDHRrzvE6y8sWlAkaf_RaZOUWdywZVL6YpfSRKDLyBfRD6yYKf0dWUGnNJ16HQtdgwC4dyf5WlHok95aHVl1g9vQlUOyIq41mjGeekUzfHc4womSVa20iu53D8TnGwhd0kAmMp7DkE_W9fWUTdjxaANH_ni5ibttKZB3zE4tSvMsA6o5k0TS6kYMaObQRIzkJNWFHG4EZ_YsPGGGOtvIlObWPzV0O8hGEY2dPTKKXl8wz69Jc48vyp4LnN8AlXBbjCE6CbIiNdZHHrK-U0NP_bCK9CAqZRumWEooQNnCw'}
r = requests.get(endpoint, headers=headers)
r1 = requests.post(endpoint1, {"id":"23123", "name":"Lemonade", "marks":18.98}, headers={})
@app.get("/")
def hello_world():
    return {"Message":"OK..."}