## SCAICO_turnover_rate
This is an archive for the 2023 SCAICO contest.

## Abstract
Review data, turnover rate, and financial statement data for each company are retrieved from **[JobPlanet](https://www.jobplanet.co.kr/job)** and **[Wanted Insight](https://insight.wanted.co.kr/)**. After combining these, we created a machine learning model that predicts turnover rate using **topic modeling**. Through comparison of **MSE, RMSE, and MAE** values ​​for each model, it was concluded that turnover rate prediction model using **topic modeling showes the highest performance in XGB and LGBM**.<br>
<br>
However, these models also have limitations. There was an imbalance in words due to differences in the number of reviews by company, and the number of data was small due to differences in data held by each site.
<br>

## Utilization plans 
### In job seekers
1. Job seekers can check the number of topics of the company he or she chooses as a percentage.<br>
2. Job seekers can select a topic and search for companies with high satisfaction for the topic in order.
### In corporate managers
1. This program provides business managers with a plan for the supply of their workforce and provides services to use in the decision-making process of how they operate. <br>
2. The program helps companies change their direction to help them grow by comparing them to competitors with similar financial indicators. <br>
3. The company can reduce the cost of personnel and employee training.<br>
## Data analysis in topic modeling
### Topic modeling in advantages
1. Compared to previous papers, leisure support can be seen as a new topic, and it can be seen that supporting the leisure life of office workers is an important factor.<br>
2. The autonomous working environment in the paper was considered an autonomous working environment in which vacations could be used without caring about other people's eyes, regarding annual leave, vacation, and awareness. The words of the autonomous working environment in 2023 show that companies that allow telecommuting with words such as **"재택 근무"**, **"재택"** are considered autonomous working environments.
### Topic modeling in disadvantages
1. Compared to our topic, first of all, the difficulty of converting to a full-time employee is a new topic.<br>
2. Pressure on customer response and performance is also a new topic <br>

## Branches
The code to extract review text data, turnover rate data, and financial statement data is in the **crawling**.<br>
Code and files related to topic modeling are in the **tm**.<br>
The code and files that ultimately create the machine learning model with these data are in the **ml**.<br>
Finally, each content is neatly organized and stored in the **main**.<br>
You can predict the turnover rate by directly inputting review data through **the turnover_calculator in the main**.<br>

## How to use
### The way to use turnover_calculator
#### In job seekers
Job seekers can select the topic they want the most and then get the companies in order, starting with the highest number of topics they choose. After that, you can choose a company by considering other topics.<br>


## Note
Code and models are only available for non-commercial research purposes.<br>
Good Luck :)

   

