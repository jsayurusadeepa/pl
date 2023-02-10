import requests
import pandas as pd
from fastapi import FastAPI
app = FastAPI()
endpoint = "https://dc0c7b7d-7fbd-4b52-9d73-ad40481e374f-dev.e1-us-east-azure.choreoapis.dev/qvaq/ordsgeneratedapiforpl/1.0.0/stud"
headers = {'Authorization': 'Bearer eyJ4NXQiOiJZV1kxTm1Sa1pHSTVNekU0T0RCbFpEUmlNV0k0WldKbE5qRXhaV1ZpWmpFek1tTm1ORFUzWVEiLCJraWQiOiJNV1E1TldVd1lXWmlNbU16WlRJek16ZG1NekJoTVdNNFlqUXlNalZoTldNNE5qaGtNR1JtTnpGbE1HSTNaRGxtWW1Rek5tRXlNemhoWWpCaU5tWmhZd19SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0ZDUyNWZkZC04N2MzLTRiOTMtODMwMy0xYjk3YTZkZWViOWYiLCJhdXQiOiJBUFBMSUNBVElPTiIsImF1ZCI6IkpwVE9Pb0pxbWlUNHY2RnlyRjlaMzBmRklOUWEiLCJuYmYiOjE2NzYwNTM1NDcsImF6cCI6IkpwVE9Pb0pxbWlUNHY2RnlyRjlaMzBmRklOUWEiLCJzY29wZSI6ImRlZmF1bHQiLCJvcmdhbml6YXRpb24iOnsidXVpZCI6ImRjMGM3YjdkLTdmYmQtNGI1Mi05ZDczLWFkNDA0ODFlMzc0ZiJ9LCJpc3MiOiJodHRwczpcL1wvc3RzLmNob3Jlby5kZXY6NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjc2MDU3MTQ3LCJpYXQiOjE2NzYwNTM1NDcsImp0aSI6ImYxOGZmMzhjLTY0MjktNDU3Zi1hYmNjLWYwZmVlMDAzOTlkZCJ9.JePhMED_7A-zQNd38xOrSi6NH8f92CWnHxO0p25Tv26BwPRLF7ml0ovyX19HU3suf0P0fP8iCLKgRJrke1LEArq60uKqd3d44I7w0lmpPy5U_SUUlAZFv80y_DnPy68ZcQzGroUIZCYJCMF8FoSczA0f8FzxtT4yGmaJWnBsh2v6ImWSIbZMcJ_eQPfd1zTVqQdxUE2L9ZD0PfiWJIWMOAhIn_De_DhCvI5lrs5W5BWF4EFiY6skc6tYFnIu8BCKiUyMPwKkgT1HVwog7zw3mrn-9IKhxTU92Kv8JUK_bWaTjdhFko3dlZkBLqwQUED2u2L4xPMKFFXUobLcpgI0fD-g0D-JPMF9uZcnXdna-b9jCcq6kCjYBjX4JVHR6g7u37KannEU5X2pgshqnwcXcwa6avvS7pjFXGiy3SmhWH-tiwovntcCeODJ6CxYvB2MDSZ_VPXQU4yR5zNXJiT15pSpVfik0EiJUXBFMFaCYHmgsR7q4pu46uSDVD_rgoslynFJbMDwTuWNkE3MgHjoPLugOE-C7NlsCMr4gX_GFX9DAo843n3tzjXCEHDTv2jm4SWcJxHJEKVyhWDn7QE3rYc2G_xr4eD84V8uTP47cejbtM1osTPC7kOH2UMHShZv2Dhx3fFqdqgvk3pzZDiFADVB0U5ojyQzgiCppmB3QRc'}
r = requests.get(endpoint, headers=headers)
@app.get("/")
def hello_world():
    df = pd.DataFrame(r.json()['items'])
    return df.to_html()