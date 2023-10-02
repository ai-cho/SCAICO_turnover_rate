## SCAICO_turnover_rate
This is an archive for the 2023 SCAICO contest.

## Abstract
Review data, turnover rate, and financial statement data for each company are retrieved from **[JobPlanet](https://www.jobplanet.co.kr/job)** and **[Wanted Insight](https://insight.wanted.co.kr/)**. After combining these, we created a machine learning model that predicts turnover rate using **TF-IDF** and **topic modeling**. Through comparison of **MSE, RMSE, and MAE** values ​​for each model, it was concluded that the turnover rate prediction model using **TF-IDF shows the highest performance in Ridge and RF**. And the turnover rate prediction model using **topic modeling showes the highest performance in XGB and LGBM**.<br>
<br>
The turnover rate prediction models obtained in this way can help corporate managers establish new personnel strategies, and help job seekers apply to companies that are right for them.
However, these models also have limitations. There was an imbalance in words due to differences in the number of reviews by company, and the number of data was small due to differences in data held by each site.

## Branches
The code to extract review text data, turnover rate data, and financial statement data is in the **crawling**<br>
Code and files related to topic modeling are in the **tm**<br>
The code and files that ultimately create the machine learning model with these data are in the **ml**<br>
Finally, each content is neatly organized and stored in the **main**<br>
You can predict the turnover rate by directly inputting review data through **the turnover_calculator in the main**<br>

## How to use
### The way to use turnover_calculator
1. Input a csv file containing company_name, adv, dadv, average_salary, and total_sale values.

2. Compare the turnover rate predictions and actual values ​​for each model, and compare the topic modeling values ​​for each topic.
   
![how_to_use](https://github.com/Sue-HyeongLee/SCAICO_turnover_rate/assets/120773889/1980bde2-ac9d-415f-9ea2-9b8482d55f60)

## Note
Code and models are only available for non-commercial research purposes.<br>
Good Luck :)

   

