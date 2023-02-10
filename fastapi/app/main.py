import requests
from fastapi import FastAPI
app = FastAPI()
endpoint = "https://dc0c7b7d-7fbd-4b52-9d73-ad40481e374f-dev.e1-us-east-azure.choreoapis.dev/qvaq/ordsgeneratedapiforpl/1.0.0/stud"
headers = {'Authorization': 'Bearer eyJ4NXQiOiJZV1kxTm1Sa1pHSTVNekU0T0RCbFpEUmlNV0k0WldKbE5qRXhaV1ZpWmpFek1tTm1ORFUzWVEiLCJraWQiOiJNV1E1TldVd1lXWmlNbU16WlRJek16ZG1NekJoTVdNNFlqUXlNalZoTldNNE5qaGtNR1JtTnpGbE1HSTNaRGxtWW1Rek5tRXlNemhoWWpCaU5tWmhZd19SUzI1NiIsImFsZyI6IlJTMjU2In0'}
r = requests.get(endpoint, headers=headers)
@app.get("/")
def hello_world():
    return {"message": r.json()}