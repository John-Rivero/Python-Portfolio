from bs4 import BeautifulSoup
import requests
import numpy as np
import csv


def nbaplayers(website):
    
    #Request to access the website
    response = requests.get(website)
    webpage = response.text

    #Activate BeautifulSoup
    soup = BeautifulSoup(webpage, 'html.parser')

    #Players
    players_list = []
    players001 = soup.find_all(name = 'a')
    for players in players001:
        players_list.append(players.getText())
        
    players_list = players_list[0:80:2]
    return players_list

def nbaplayers_salary(website):
    
    #Request to access the website
    response = requests.get(website)
    webpage = response.text

    #Activate BeautifulSoup
    soup = BeautifulSoup(webpage, 'html.parser')

    #Players Salary
    players_salary = []
    playerssalary001 = soup.find_all(name = 'td', style = 'text-align:right;')
    for playersSal in playerssalary001:
        playersSal2 = (playersSal.getText())
        
        if playersSal2 != 'SALARY':
            players_salary.append(playersSal2)
            
    return players_salary

#Season 2022
nba_players_2022 = nbaplayers('http://www.espn.com/nba/salaries/_/year/2022')
nba_players_2022_salary = nbaplayers_salary('http://www.espn.com/nba/salaries/_/year/2022')
Season_2022 = np.column_stack((nba_players_2022, nba_players_2022_salary))
print(Season_2022)

with open('2022Season.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Players", "Salary"])
    for row in Season_2022:
        player = row[0]
        salary = int(row[1].replace('$','').replace(',',''))
        writer.writerow([player, salary])
file.close()


#Season 2023
nba_players_2023 = nbaplayers('http://www.espn.com/nba/salaries')
nba_players_2023_salary = nbaplayers_salary('http://www.espn.com/nba/salaries')
Season_2023 = np.column_stack((nba_players_2023, nba_players_2023_salary))
print(Season_2022)

with open('2023Season.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Players", "Salary"])
    for row in Season_2023:
        player = row[0]
        salary = int(row[1].replace('$','').replace(',',''))
        writer.writerow([player, salary])
file.close()

