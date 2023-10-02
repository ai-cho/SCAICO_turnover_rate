## competition-by-AI
This is an archive for the SCAICO contest.

## Abstract
Review data, turnover rate, and financial statement data for each company are retrieved from Job Planet and Wanted Insight. After combining these, we created a machine learning model that predicts turnover rate using TF-IDF and topic modeling. Through comparison of MSE, RMSE, and MAE values ​​for each model, it was concluded that the turnover rate prediction model using TF-IDF shows the highest performance in Ridge and RF. And the results showed that the turnover rate prediction model through topic modeling showed the highest performance in XGB and LGBM.

The turnover rate prediction models obtained in this way can help corporate managers establish new personnel strategies, and help job seekers apply to companies that are right for them.
However, these models also have limitations. There was an imbalance in words due to differences in the number of reviews by company, and the number of data was small due to differences in data held by each site.

## Branches
The code to extract review text data, turnover rate data, and financial statement data is in the crawling branch.

Code and files related to topic modeling are in the tm branch.

The code and files that ultimately create the machine learning model with these data are in the ml branch.

Finally, each content is neatly organized and stored in the main branch.

You can predict the turnover rate by directly inputting review data through the turnover_calculator in the main branch.

## How to use
### The way to use turnover_calculator
1. Input a csv file containing company_name, adv, dadv, average_salary, and total_sale values.

2. Compare the turnover rate predictions and actual values ​​for each model, and compare the topic modeling values ​​for each topic.

3. ~ing

   

