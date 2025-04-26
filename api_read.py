"""
#dlt credentials
site:https://app.exchangerate-api.com/dashboard
uid:ot.madhura@gmail.com
pwd:ot.madhura
"""
import dlt
from dlt.sources.helpers import requests
import requests
import pandas as pd
import json
from datetime import date
from datetime import datetime
from uuid import uuid4


key = 'd85dce6e02862ef7d7c8f7a4'

# api call
url = f'https://v6.exchangerate-api.com/v6/{key}/pair/USD/INR'
print (url)

# Make a request
response = requests.get(url)
print (response)
data = response.json()
print (data)

data = data['conversion_rate']
print (data)