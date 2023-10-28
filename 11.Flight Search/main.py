import requests
import os
from dotenv import load_dotenv
load_dotenv()


app_api = os.getenv("KIWI_API")


kiwi = "https://api.tequila.kiwi.com/locations/id"

# cityFrom = input("Where are you coming from? ")
# cityTo = input("Where are you going to? ")
# fromDate = input("When are you leaving? ")


params = {
    "id" : "PRG"
}
header = {
    
    "apikey" : app_api
    
}

response = requests.get(url=kiwi, headers=header, params=params)
print(response.json())