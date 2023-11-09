import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


#Connect to AWS Database
db_endpoint = "my-db-instance.c4xofzuspizi.us-east-1.rds.amazonaws.com"
db_user = "postgres"
db_password = os.getenv("database_password")
db_name = "initial_db"


conn = psycopg2.connect(
    host=db_endpoint,
    database=db_name,
    user=db_user,
    password=db_password
)

cursor = conn.cursor()

cursor.execute('SELECT * FROM "public"."airports" LIMIT 1000 ')

rows = cursor.fetchall()




#Retrieve IATA Code
def retrieve_iata():
    list = []
    for row in rows:
        list.append(row[4])
    return list

    
    
#Retrieve Airport Names
def retrieve_airportname():
    list = []
    for row in rows:
        list.append(row[1])
    return list
