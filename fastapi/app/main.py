from fastapi import FastAPI

    app = FastAPI()
    endpoint = "https://dc0c7b7d-7fbd-4b52-9d73-ad40481e374f-dev.e1-us-east-azure.choreoapis.dev/qvaq/ordsgeneratedapiforpl/1.0.0/stud"
    
	api_response = requests.get(endpoint,headers={'Authorization': 'Bearer eyJ4NXQiOiJZV1kxTm1Sa1pHSTVNekU0T0RCbFpEUmlNV0k0WldKbE5qRXhaV1ZpWmpFek1tTm1ORFUzWVEiLCJraWQiOiJNV1E1TldVd1lXWmlNbU16WlRJek16ZG1NekJoTVdNNFlqUXlNalZoTldNNE5qaGtNR1JtTnpGbE1HSTNaRGxtWW1Rek5tRXlNemhoWWpCaU5tWmhZd19SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0ZDUyNWZkZC04N2MzLTRiOTMtODMwMy0xYjk3YTZkZWViOWYiLCJhdXQiOiJBUFBMSUNBVElPTiIsImF1ZCI6IkpwVE9Pb0pxbWlUNHY2RnlyRjlaMzBmRklOUWEiLCJuYmYiOjE2NzU4NDU2OTgsImF6cCI6IkpwVE9Pb0pxbWlUNHY2RnlyRjlaMzBmRklOUWEiLCJzY29wZSI6ImRlZmF1bHQiLCJvcmdhbml6YXRpb24iOnsidXVpZCI6ImRjMGM3YjdkLTdmYmQtNGI1Mi05ZDczLWFkNDA0ODFlMzc0ZiJ9LCJpc3MiOiJodHRwczpcL1wvc3RzLmNob3Jlby5kZXY6NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjc1ODQ5Mjk4LCJpYXQiOjE2NzU4NDU2OTgsImp0aSI6IjgzOWM5NGI1LTIyNTctNDUxZC1iZmIwLWZjMzEyMTI5NDVhOCJ9.Ao5teg0uppO95WpJGZmtFjnzCoRwJjiK9nVkeRrY4-E26o_3ObasVqgAugON4NS0Gle7YvJNLZzGskk7dk8EHSln1i2Ll5jzFN1j7hSp3uuJNxBLPPqfxR2mb2hIDpESh_ZpeuOL4pNcbjlBCFH88zsNmQLyQ20JF9vEQxmIBgyUMHqI6vbEoFl5JT9YplRtbk5FX6nNVqP4nA2IxJ0Valj3qzYYh6CuweLOTx0-DnFYjFnk6gNoXM7SdbzhL8NUH8GhCwJwqccUJNczJqBzIwkcorPx5Q0gYleNMthqE4lOIyinVhq469pp5MLMH3dOqMPYzWRRcZpffJHzQrD4Ii86_lRqOoONFsSv_AWccaBG7sWRtCByLkYMXQGkwAcfvb-EmqoRp_g1qozT8Cx4k8r5WoFOHqLIeCZNHsCZeJvYzYf2OaYBJmyJk9rf8lNP9_w46fekoWKp58P_YascNPJWJI1HWWS4nnwKZqZW7mlsZhLDSBAUq__PbDFwYNwt3LhXib6xg3kJkHKfs3WwFoQsxt3CPa1RY5dRbCpYixV0TgpeNlLHEiRQd3sVzynW2es62gnPGEKWcjHGGzWbtfMp4Y3-TrZovOKfwwh6yQkbeNdwGyDsG6j60pAU_FD1tkdA8YSwWZ7Y8rtCBIUArKGVzS4vtPKSA3d5f1oU1EQ'})

@app.get("/")
def hello_world():
    return {"message": "OK..."}
