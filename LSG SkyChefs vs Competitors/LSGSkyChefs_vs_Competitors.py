import pandas as pd


file = pd.read_csv("Company Analysis.csv")




#SORT REVENUE 
sort_revenue = file.sort_values(by='Revenue', ascending=False)

# Define a custom formatting function
def format_revenue(revenue):
    return '${:,.2f}'.format(revenue)

# Apply the formatting function to the "Revenue" column
sort_revenue['Revenue'] = sort_revenue['Revenue'].apply(format_revenue)

# Display the sorted dataframe with formatted revenue
print(sort_revenue)




#SORT EMPLOYEES
sort_employees = file.sort_values(by='Employees', ascending=False)
print(sort_employees)



#SORT Founding Date
sort_FoundingDate = file.sort_values(by='Founding Date', ascending=False)
print(sort_FoundingDate)