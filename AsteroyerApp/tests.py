from django.test import TestCase
import requests
from datetime import date

apiKey = "DEMO_KEY" 

today = date.today().strftime("%Y-%m-%d")

url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&api_key={apiKey}"

r = requests.get(url)  
data = r.json()

print(data)
