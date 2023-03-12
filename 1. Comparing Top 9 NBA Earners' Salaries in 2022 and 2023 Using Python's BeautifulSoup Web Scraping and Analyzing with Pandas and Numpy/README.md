## Title: Top 5 Countries with the Best Investment Potential: An Analysis of GDP and Inflation Rates in SQL and Visualization in Tableau

## Author: John Rivero

## Date: February 17, 2023

[Tableau Dashboard](https://public.tableau.com/app/profile/john.r6470/viz/Top10countrieswiththehighestGDPforinvestmentopportunitiesDashboard_/Dashboard1)

[Tableau Story Presentation to Stakeholder](https://public.tableau.com/app/profile/john.r6470/viz/Top10countrieswiththehighestGDPforinvestmentopportunitiesStory_/Story1)


## The case study follows the six step data analysis process.

 [Ask](#1-Ask)

 [Prepare](#2-Prepare)

 [Process](#3-Process)

 [Analyze](#4-Analyze)

 [Share](#5-Share)

 [Act](#6-Act)


## Scenario

- An investor named Josh McDonald who is looking to expand his investment portfolio and is interested in investing in countries with a strong history of Gross Domestic Product (GDP) growth for the past 10 years. He has decided to use data analytic to identify which countries are the best to invest based on their 10 years GDP history.


## 1. Ask

 - Task: Evaluate the Gross Domestic Product (GDP) data and inflation rate for the past 10 years to determine the top 5 out of 10 most favorable countries for investment.

 - Primary Stakeholder: Josh McDonald


## 2. Prepare

- Data Source 1: (GDP) 61 years (1960 to 2021) from [The World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)
               The GDP dataset has 1 CSV file, 65 Columns, and 271 Rows.

![2  GDP Spreadsheet Image](https://user-images.githubusercontent.com/81208412/219589204-fb67187a-70e5-4823-a29a-8165da4acaa7.jpg)


- Data Source 2: (Inflation) 61 years (1960 to 2021) from [The World Bank](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG)
               The Inflation dataset has 1 CSV file, 65 Columns, and 271 Rows.

![2  Inflation Spreadsheet Image](https://user-images.githubusercontent.com/81208412/219589224-48e4bad4-e664-418f-ade6-faea432308c3.jpg)


## 3. Process

- The CSV files containing GDP and inflation data have been extensively cleaned and are now prepared for import into an SQL server for further analysis.

![2  GDP Processed Image](https://user-images.githubusercontent.com/81208412/219591776-81e8f5b6-1acd-40bc-a64d-d3a4631c9f2f.jpg)

![2  Inflation Processed Image](https://user-images.githubusercontent.com/81208412/219591804-b046cd5c-70dc-4ea0-8504-e64a9b78598f.jpg)


- Tables have been created for both inflation and GDP data to facilitate the import of the cleaned CSV files.

![3  Create GDP Table](https://user-images.githubusercontent.com/81208412/219590392-a0a8ad2d-d2be-430d-af65-6019a8a277b2.jpg)

![3  Create Inflation Table](https://user-images.githubusercontent.com/81208412/219590422-f0128f1f-43a6-44c9-827d-2e6ac33312b8.jpg)


## 4. Analyze

- An SQL query is used to identify the top 10 countries with the highest combined GDP over a 10-year period, as well as the average inflation rate during that same time frame.

![1  Analyze 10 highest total gdp](https://user-images.githubusercontent.com/81208412/219596265-bf9a2eb8-543b-4634-98ab-519407eac566.jpg)

Based on the result of the query, the United States is the most attractive country for investment, with a combined GDP of $209 trillion over a 10-year period and an average inflation rate of 2.20%. China ranks second, with a total GDP of $131.35 trillion and an average inflation rate of 2.61%, followed by Japan in third place with a total GDP of $57.12 trillion and an average inflation rate of 0.51%. Germany comes in fourth place with a GDP of $41.43 trillion and an average inflation rate of 1.58%. Lastly, the country with the best investment potential is the United Kingdom, with a GDP of $31.12 trillion and an inflation rate of 2.16%.


## 5. Share

[GDP and Inflation Analysis Dashboard](https://public.tableau.com/app/profile/john.r6470/viz/Top10countrieswiththehighestGDPforinvestmentopportunitiesDashboard_/Dashboard1)

![Dashboard 1](https://user-images.githubusercontent.com/81208412/219598626-c8beecb5-1553-4256-9f6a-640414c91e94.png)


[10 countries with the greatest combined GDP over a period of 10 years presentation in Tableau](https://public.tableau.com/app/profile/john.r6470/viz/Top10countrieswiththehighestGDPforinvestmentopportunitiesStory_/Story1)

![Story 1](https://user-images.githubusercontent.com/81208412/219680747-99a46b8a-4b79-4211-acaf-43bd795592fb.png)


## 6. Act

Conclusion based on my analysis:

- According to the available data, out of 200+ countries, the United States is the most attractive country for investment, followed by China in second place, Japan in third place, Germany in fourth place, and the United Kingdom in fifth place.

- The United States boasts a GDP of $209 trillion over a 10-year period and an average inflation rate of 2.20%, making it the top choice for investment. China comes in second place with a total GDP of $131.35 trillion and an average inflation rate of 2.61%. Japan has a total GDP of $57.12 trillion and an average inflation rate of 0.51%, placing it in third position. Germany has a GDP of $41.43 trillion and an average inflation rate of 1.58%, making it the fourth best country for investment. Lastly, the United Kingdom has a GDP of $31.12 trillion and an inflation rate of 2.16%, securing its position as the fifth best country for investment.
