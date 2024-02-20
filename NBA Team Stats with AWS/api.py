import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


#API CALL for team information
url = "https://api-nba-v1.p.rapidapi.com/teams"

headers = {
	"X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
	"X-RapidAPI-Host": os.getenv("X-RapidAPI-Host")
}

response = requests.get(url, headers=headers)
value = response.json()
################################################################################
 
 
#PRETTIFY JASON OUTPUT FILE
pretty_json = json.dumps(value, indent=4) # 4 spaces for indentation
#print(pretty_json)
#################################################################################





##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

