import smtplib
import datetime as dt
import random as rd
import pandas as pd


#IMPORTANT_NOTE: Please make sure to change the my_email and password to your specification LINEs 74 & 75
#IMPORTANT_NOTE: You need to place the appropriate email and birthda on the "birthdays.csv"
#IMPORTANT_NOTE: You need to change the name of the sender withing letter_1, letter_2, and letter_3

#Read CSV File and create a dataframe
data = pd.read_csv("birthdays.csv")
dataframe = pd.DataFrame(data)


#datetime
date_now = dt.datetime.now()


#for loop range for the amount of lines in birthday.csv
number_of_lines_CSV = len(dataframe)
for n in range (number_of_lines_CSV):
    print(n)
    csvfiledate = \
    {
        "year" : dataframe['year'][n],
        "month" : dataframe['month'][n],
        "day" : dataframe['day'][n]
    }
    print(csvfiledate)

    today = \
    {
        "year" : date_now.year,
        "month" : date_now.month,
        "day" : date_now.day
    }
    print(today)
    
    #determine whether today's date matches with the birth_date1
    if today == csvfiledate:
        print('success')
        
        #read letter files
        name = dataframe['name'][0]
        with open("letter_1.txt") as openfile:
            file = openfile.read()
            updated_content = file.replace('Dear [NAME],', f'Dear {name},' )
            print(updated_content)
            
        with open("letter_2.txt") as openfile:
            file = openfile.read()
            updated_content2 = file.replace('Dear [NAME],', f'Dear {name},' )
            print(updated_content2)
            
        with open("letter_3.txt") as openfile:
            file = openfile.read()
            updated_content3 = file.replace('Dear [NAME],', f'Dear {name},' )
            print(updated_content3)
            
        #choose randomly between 3 different letters
        random_letter = rd.choice([updated_content, updated_content2, updated_content3])
        
        
        
        #read quote text files and choose a random line
        with open("quotes.txt") as openfile:
            file = openfile.readlines()
            random_value = rd.randint(0, 101)
            message = f'Subject:Happy Birthday\n\n{random_letter}\n\n{file[random_value]}'

            
        #username and password for the email sender
        my_email = "PUT YOUR EMAIL HERE"
        password = 'PUT YOUR PASSWORD HERE'
            
        #open connection to send email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls( )
            connection.login(user=my_email, password=password)
            target_email = dataframe['email'][n]
            connection.sendmail(from_addr=my_email, to_addrs=target_email,\
                msg=message)


