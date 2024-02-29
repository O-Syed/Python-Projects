import requests
import numpy as np
import pandas as pd

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
frame = r.json()['data']

df_list = frame.split(",")

agedf = [int(i.replace("age=","")) for i in df_list if "age" in i]
keydf = [i.replace("key=","") for i in df_list if "key" in i]
df = pd.DataFrame({"key" : keydf, "age" : agedf})
result = df[df.age >= 50].count().values[0]
print(result)
