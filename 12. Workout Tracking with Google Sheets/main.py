import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

app_id = os.getenv("APP_ID")
app_keys = os.getenv("APP_KEYS")

query = input('What workout did you do? ')
user_weight = 72.5748
user_height = 167.64
user_age = 30



#******************Nutritionix************
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    'x-app-id' : app_id,
    'x-app-key' : app_keys
}

parameter = {
    'query' : query,
    'gender' : 'Male',
    'weight_kg' : user_weight,
    'height_cm' : user_height,
    'age' : user_age,
    
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=parameter, headers=header)
print(response.json())