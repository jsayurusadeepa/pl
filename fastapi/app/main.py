import requests
from fastapi import FastAPI
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt
import base64
from flask import Flask
from matplotlib.figure import Figure
app = Flask(__name__)
endpoint = "https://dc0c7b7d-7fbd-4b52-9d73-ad40481e374f-dev.e1-us-east-azure.choreoapis.dev/qvaq/ordsgeneratedapiforpl/1.0.0/stud"
headers = {'Authorization': 'Bearer eyJ4NXQiOiJZV1kxTm1Sa1pHSTVNekU0T0RCbFpEUmlNV0k0WldKbE5qRXhaV1ZpWmpFek1tTm1ORFUzWVEiLCJraWQiOiJNV1E1TldVd1lXWmlNbU16WlRJek16ZG1NekJoTVdNNFlqUXlNalZoTldNNE5qaGtNR1JtTnpGbE1HSTNaRGxtWW1Rek5tRXlNemhoWWpCaU5tWmhZd19SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0ZDUyNWZkZC04N2MzLTRiOTMtODMwMy0xYjk3YTZkZWViOWYiLCJhdXQiOiJBUFBMSUNBVElPTiIsImF1ZCI6Ik5EeFNDdDBmOGdyX3ZrdzZseWQ2X3JubjM4UWEiLCJuYmYiOjE2NzYwNDIxNDUsImF6cCI6Ik5EeFNDdDBmOGdyX3ZrdzZseWQ2X3JubjM4UWEiLCJzY29wZSI6ImRlZmF1bHQiLCJvcmdhbml6YXRpb24iOnsidXVpZCI6ImRjMGM3YjdkLTdmYmQtNGI1Mi05ZDczLWFkNDA0ODFlMzc0ZiJ9LCJpc3MiOiJodHRwczpcL1wvc3RzLmNob3Jlby5kZXY6NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjoxNjc2MDQ1NzQ1LCJpYXQiOjE2NzYwNDIxNDUsImp0aSI6IjY3MTIxZGRlLWE0OGMtNGIzYy04OGViLTk3NDQ2MDhiNTk1MSJ9.oA7S-JCLWNpWwDwCA1fbcsFyBhhWWsrWkblsAS8j-QPflHoDb9JJKuvSFqnQhyhR1DxLJdvhPo3uCZjPwuz5y7Y25A7kTAAvGYmPNzK3dXoO_zfu3Z5yYV4QzuWl2IJ0TW54TCzh-Nvpzon25Gu2StD-3KePavGIWjt9Xhu5IwPdkMYWBsBoTawvzLeNaG_NjXK-WEVATvsvK4KNxSP2boterNENkrS4zCJLQbBY6fqlDb20hk02HvsRfwnDoy8E1XUc2FouQUUJQNJ0FSc9Rdr-1lmwZq-r9u2TQz43zlE5bp9sCc1bwzgxGNXrwUDko-T1eeLf32CG_lPVUeFFzDG4R326X_ZosTwn-xswN-52MrWanXtgpzwdZ71wroTVSpzgBkSGVwdX63xpIrI6tk_qitWRSjTzv-kA0bh7e1CKMqzrNVXEpUzmLRb259RhYmD-_Se1govF2tL1BSmTe7dIs_tVTlUFp84i776ispYznLlP_IwqPaGdqGDaYudj03__cmOw1fEBWX5Xm9nv7zPkJZwhPA5b5RpEjnqTaNvc0-DlKCPaxJxfUeGb6z2xskUpWCZ8BhebDIBYhWNLEWeWtJEmG8BvzdxEyaDsYXiubWc5XeFY-6BCwedxXrNqxASRusP_1kpwAfMWmN8RyZz3CqYefW7sUtc82agJEC0'}
r = requests.get(endpoint, headers=headers)
@app.route("/")
def hello_world():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"