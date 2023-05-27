import pandas as pd
import requests


df = pd.read_csv("uszips.csv")
df = df[["zip", "state_name", "city","lat","lng"]]
df = df.rename(columns={"zip":"post_code_zip","state_name":"state"})
df = df.astype({"post_code_zip":"str","lat":"float","lng":"float"})
df = df.to_json(orient="records")

requests.post(url="http://localhost:8000/api/v1/location-list/", data=df, headers={"Content-Type":"application/json; charset=utf-8"})