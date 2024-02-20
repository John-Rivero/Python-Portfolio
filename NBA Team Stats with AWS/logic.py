from api import *
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from io import BytesIO
import psycopg2


#CHECK TO SEE IF THE TEAM IS WITHIN THE LIST
nba_teams = [
    "Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "Los Angeles Clippers",
    "Los Angeles Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizards"
]


#Place everything on a list
team_list_name = []
team_list_city = []
team_logo = []
team_id = []



for teams in value['response']:
    #print(teams)
    if teams['name'] in nba_teams:
        team_id.append(teams['id'])
        
        team_list_name.append(teams['name'])
        
        team_list_city.append(teams['city'])
    
        team_logo.append(teams['logo'])
        
        
teams_list = [list(group) for group in zip(team_id, team_list_name, team_list_city, team_logo)]   



nba_teams_counter = {
"Atlanta Hawks"         : 0,
"Boston Celtics"        : 0,
"Brooklyn Nets"         : 0,
"Charlotte Hornets"     : 0,
"Chicago Bulls"         : 0,
"Cleveland Cavaliers"   : 0,
"Dallas Mavericks"      : 0,
"Denver Nuggets"        : 0,
"Detroit Pistons"       : 0,
"Golden State Warriors" : 0,
"Houston Rockets"       : 0,
"Indiana Pacers"        : 0,
"Los Angeles Clippers"  : 0,
"Los Angeles Lakers"    : 0,
"Memphis Grizzlies"     : 0,
"Miami Heat"            : 0,
"Milwaukee Bucks"       : 0,
"Minnesota Timberwolves": 0,
"New Orleans Pelicans"  : 0,
"New York Knicks"       : 0,
"Oklahoma City Thunder" : 0,
"Orlando Magic"         : 0,
"Philadelphia 76ers"    : 0,
"Phoenix Suns"          : 0,
"Portland Trail Blazers": 0,
"Sacramento Kings"      : 0,
"San Antonio Spurs"     : 0,
"Toronto Raptors"       : 0,
"Utah Jazz"             : 0,
"Washington Wizards"    : 0}



def display_nba_stats(self):

    #Display the current text selection in the comboBox
    selected_index = self.comboBox.currentText()
    #print(selected_index)
    
    
    
    #Iterate through them teams_list
    for teams in teams_list:
        #print(teams)
        
        
        #Display the Team stats
        if selected_index in teams:
            
            #print(selected_index)
            
            teamID = teams[0]
            
            
            ######################################################
            ######################################################
            ######################################################
            ######################################################
            
            
            #API CALL TO GET TEAMS STATISTIC
            url = "https://api-nba-v1.p.rapidapi.com/teams/statistics"

            headers = {
                "X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
                "X-RapidAPI-Host": os.getenv("X-RapidAPI-Host")
            }
            
            querystring = {'id' : {teamID} , 'season' : '2023'}

            response = requests.get(url, headers=headers, params=querystring)
            value = response.json()
    
    
            ######################################################
            ######################################################
            ######################################################
            ######################################################
    
    
            #Retrieve team stats
            teams_games = value['response'][0]['games']
            team_poits = value['response'][0]['points']
            team_assist = value['response'][0]['assists']
            team_steals = value['response'][0]['steals']
            team_blocks = value['response'][0]['blocks']
            team_totReb = value['response'][0]['totReb']

    
    
            #Turn the stats into a Dataframe
            data = {
                
                "Games" : [teams_games],
                "Points" : [team_poits],
                "Assists" : [team_assist],
                "Steals" : [team_steals],
                "Blocks" : [team_blocks],
                "Rebounds" : [team_totReb]
                
                
                
            }

            team_dataframe = pd.DataFrame(data)
            #print(team_dataframe)
            
            
            # Convert the DataFrame to HTML
            html_table = team_dataframe.to_html(index=False)
            table_style = """
                            <style>
                            table {
                                width: 100%;
                                border-collapse: collapse;
                                border-radius: 20px;
                                overflow: hidden;
                                font-size: 21px;
                            }
                            th {
                                background-color: rgb(0, 0, 0);
                                color: white;
                                font-weight: bold;
                                
                                border-radius: 20px;
                                padding: 10px;
                            }
                            td {
                                padding: 5px;
                            }
                            tr:nth-child(even) td {
                                background-color: rgb(0, 0, 0);
                            }
                            tr:nth-child(odd) td {
                                background-color: white;
                            }
                            </style>
                            """
            styled_html_table = f'{table_style}{html_table}'  
            self.textEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
            self.textEdit.setHtml(styled_html_table)


        ######################################################
        ######################################################
        ######################################################
        ######################################################


        #Display team logo
        if selected_index in teams:
            print(selected_index)
            
            team_logo = teams[3]
            #print(team_logo)
            url = team_logo
            response = requests.get(url)
            image_pixmap = QPixmap()
            image_pixmap.loadFromData(response.content)
            self.NBA_Logo.setPixmap(image_pixmap)


        ######################################################
        ######################################################
        ######################################################
        ######################################################

    
    
    db_name = os.getenv("db_name")
    db_user = os.getenv("db_user")
    db_password = os.getenv("db_password")
    db_host = os.getenv("db_host")
    db_port = os.getenv("db_port")
    
    
    # Establish a connection to the database
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print("Connected to the database.")
        
        # Create a cursor object
        cur = conn.cursor()
        
        update_statement = """
        UPDATE public.nbalogs
        SET nbateam_logs = nbateam_logs + 1
        WHERE nbateam_name = %s;
        """
        
        # Execute the update statement
        cur.execute(update_statement,(selected_index,))

        # Commit the transaction
        conn.commit()

        print("Updated the value successfully.")
        
        # Close the cursor and connection
        cur.close()
        conn.close()

    except Exception as e:
        print(f"An error occurred: {e}")