import requests
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()


app_api = os.getenv("KIWI_API")

kiwi = "https://api.tequila.kiwi.com/locations/id"


params = {
    "id" : "PRG"
}
header = {
    
    "apikey" : app_api
    
}

response = requests.get(url=kiwi, headers=header, params=params)
#print(response.json())





def identifyPrice(self, index):
    selectedFrom_city = self.locationFrom.currentText()
    selectedTo_city = self.locationTo.currentText()
    
    df = pd.DataFrame(selectedFrom_city, selectedTo_city)
    
    print(df)
    
    