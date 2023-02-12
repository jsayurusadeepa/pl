import requests
import pandas as pd
from fastapi import FastAPI
app = FastAPI()
endpoint = "https://dc0c7b7d-7fbd-4b52-9d73-ad40481e374f-dev.e1-us-east-azure.choreoapis.dev/qvaq/ordsgeneratedapiforpl/1.0.0/stud"
endpoint1 = 'http://localhost:8081/marks'
headers = {'Authorization':'Bearer eyJ4NXQiOiJZV1kxTm1Sa1pHSTVNekU0T0RCbFpEUmlNV0k0WldKbE5qRXhaV1ZpWmpFek1tTm1ORFUzWVEiLCJraWQiOiJNV1E1TldVd1lXWmlNbU16WlRJek16ZG1NekJoTVdNNFlqUXlNalZoTldNNE5qaGtNR1JtTnpGbE1HSTNaRGxtWW1Rek5tRXlNemhoWWpCaU5tWmhZd19SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0ZDUyNWZkZC04N2MzLTRiOTMtODMwMy0xYjk3YTZkZWViOWYiLCJhdXQiOiJBUFBMSUNBVElPTiIsImF1ZCI6Ik5EeFNDdDBmOGdyX3ZrdzZseWQ2X3JubjM4UWEiLCJuYmYiOjE2NzYyMjMwNzYsImF6cCI6Ik5EeFNDdDBmOGdyX3ZrdzZseWQ2X3JubjM4UWEiLCJzY29wZSI6ImRlZmF1bHQiLCJvcmdhbml6YXRpb24iOnsidXVpZCI6ImRjMGM3YjdkLTdmYmQtNGI1Mi05ZDczLWFkNDA0ODFlMzc0ZiJ9LCJpc3MiOiJodHRwczpcL1wvc3RzLmNob3Jlby5kZXY6NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjc2MjI2Njc2LCJpYXQiOjE2NzYyMjMwNzYsImp0aSI6IjE0MmY3NjIyLWFiNGUtNGU0NS04OWU2LTRlOGQ5N2EyMWNlMiJ9.GAcAdZLQDcRSmbscixyeryE40sUiDqX81hwzZtAPqFjEIE7GeDQUVvt7ye-_apqLy2MOscKITsvImXPinijHkv9J5CazPgte6AfeoNdLua9JkhOQCXtQWZLj2x60xI1LPAoo28eiz4aU25Gtu74uqJkyneAdcQF5QMyz1ZWxB-rhcfz7l_rwxkIZ-wGK2LG-ADhmQArLAIl-PInNnZtG6mJSRHEAIR7UoMvij9de1SxwKGbFCUwafbGrnopkTgso1BMCuCGCnrZtEwdc2r8sZHbHkRIr9TYkVPXsG3o2uESGZY4dHakrS-Q01gDn88Q_cET7Wx2ROMyPMTdLFXVQNJh4JmelcnP2ZvFMZ6DmX6_JCY4eva17I34iBDOc1riSTf4awycHGzHl8yK5UibLYTPyyTHy3t_w7IS-XPYBb7LmYybtItgl4NU9leZXmhK7IwY6_tRpRCqUkRb5Hyb7k_Ah8Ka4VCpswVsQVKobfDVL6-5WkINJobO6qGCTub6yb-_N7K-JrDHUECnRZn5B9w33Rvyv6UREnRUUqMdc07fB9YyBosdwNOybvvrxQcgulv5a748AiI5FszD9LF8fPiLamEU86LO3P8fOa70aN439sKDHGjqdDT-QsvlnwY9FlCbQ7AwsrlqyNGAxPVQAS_UGa_W6qUedzMUswM0VymQ'}
r = requests.get(endpoint, headers=headers)
@app.get("/")
def hello_world():
    r1 = requests.post(endpoint1, r.json()['items'])
    return {"Message":r1.json()}