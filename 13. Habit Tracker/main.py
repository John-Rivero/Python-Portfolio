import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

USERNAME = "johnrivero19"
TOKEN = os.getenv("TOKEN")


#********************CREATE PIXELA ACCOUNT**************************
PIXELA_USER_ENDPOINTS = "https://pixe.la/v1/users"
user_parameters = \
    {
        "token" : TOKEN,
        "username" : USERNAME,
        "agreeTermsOfService" : 'yes',
        "notMinor" : "yes",
        
    }

#response = requests.post(url=PIXELA_USER_ENDPOINTS, json=user_parameters)
#print(response.text)


#************************CREATE PIXELA GRAPHS*************************************
PIXELA_GRAPH_ENDPOINTS = f"{PIXELA_USER_ENDPOINTS}/{USERNAME}/graphs"
graph_parameters = \
    {
        "id" : "graph1992",
        'name' : "Workout Graph",
        "unit" : "mins",
        "type" : "int",
        "color" : "shibafu"
    }
    
headers = \
    {
        "X-USER-TOKEN" : TOKEN
    }

#response2 = requests.post(url=PIXELA_GRAPH_ENDPOINTS, json=graph_parameters, headers=headers)
#print(response2.text)

#*****************************POST A VALUE TO THE GRAPH***********************************
PIXELA_POST_VALUE = f"{PIXELA_USER_ENDPOINTS}/{USERNAME}/graphs/graph1992"
current_date = datetime.now()
formatted_date = current_date.strftime("%Y%m%d")

post_parameters = \
    {
        "date" : formatted_date,
        "quantity" : "2",

    }

# response3 = requests.post(url=PIXELA_POST_VALUE, json=post_parameters, headers=headers)
# print(response3.text)


#**************************UPDATE THE GRAPH******************************************
minutes_count = str(input("How many minutes did you workout today? "))


PIXELA_UPDATE = f"{PIXELA_USER_ENDPOINTS}/{USERNAME}/graphs/graph1992/{formatted_date}"

update_parameter = \
    {
        "quantity" : minutes_count
    }
    
response4 = requests.put(url=PIXELA_UPDATE, json=update_parameter, headers=headers)
print(response4.text)