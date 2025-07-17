## SCAICO_turnover_rate 
This is an archive for the 2023 SCAICO <sub> (Seoul Central AI Competition) </sub> contest. It's a competition hosted by SK Telecom. The judges said that we used a simple model, but we analyzed the data well in terms of data science and created the program that the actual company(Wanted Insight, Job Planet) wanted.

## Abstract
Review data, turnover rate, and financial statement data for each company are retrieved from **[JobPlanet](https://www.jobplanet.co.kr/job)** and **[Wanted Insight](https://insight.wanted.co.kr/)**. After merging these data, we analyzed it through LDA topic modeling and grouped up company characteristics into 6 advantage topics and 7 disadvatange topics. Then, we created a machine learning model that predicts turnover rate using **topic modeling**. Through comparison of **MSE, RMSE, and MAE** values ​​for each model, it was concluded that turnover rate prediction model using **topic modeling showes the highest performance in XGB and LGBM**.<br>
<br>
However, these models also have limitations. There was an imbalance in words due to differences in the number of reviews by company, and the number of data was small due to differences in data held by each site.
<br>

## Utilization plans 
We view that our findings can be utilized by...
### 1. job seekers
1. Job seekers can check the number of topics of the company he or she chooses as a percentage.<br>
2. Job seekers can select a topic and search for companies with high satisfaction for the topic in order.
### 2. corporate managers
1. This project can guide business managers to set a plan for the supply of their workforce and provide services to use in the decision-making process of how they manage their firm. <br>
2. The project is expected to change firms' management strategy and aid them to enhance their performance by comparing their characteristics to that of their competitors with similar financial indicators. <br>
3. Implementing our project is expected to reduce the cost of HR and employee training.<br>

## Data analysis in topic modeling
### Topic modeling in advantages
1. Compared to precedent papers, in 2023, leisure support is a rizing topic among workforces. Supporting the leisure life of office workers is an important factor, and it is backed up by the survey done by Jobplanet.<br>
2. The autonomous working environment in precedent paper was considered as working environment that work forces can use their vacations without caring about other people's eyes. However, autonomous working environment in 2023 is comprised of words like **"재택 근무"**, **"재택"** , which are allows their employees to telecommute.
### Topic modeling in disadvantages
1. Compared to precedent paper, the difficulty of converting to permanent employee is a rizing topic. It has been supported by the rize of the wage gap between permanent employee and temporary employee. <br>
2. Pressure on customer response and performance is also a new topic. <br>

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
![sort](https://github.com/Sue-HyeongLee/SCAICO_turnover_rate/assets/142400569/2522d32a-4dcb-4b4a-907f-b3b578b4ee08)
<br>
![check](https://github.com/Sue-HyeongLee/SCAICO_turnover_rate/assets/142400569/0c4af67a-03ae-4ad6-8390-6f8eb54db01c)
#### In corporate managers
If you put the company's review data and financial indicators into the model, you can see the turnover rate and the percentage of each topic.
<br>
![image](https://github.com/Sue-HyeongLee/SCAICO_turnover_rate/assets/142400569/f9ed9f18-e0f9-4112-986f-2a20084e94b0)
## Verify that topic modeling is valid
We used Amore Pacific's actual case to confirm that each topic modeling figure was valid.
<br>
![verify](https://github.com/Sue-HyeongLee/SCAICO_turnover_rate/assets/142400569/97221a0f-c553-44c3-b8dc-2fe87046bfc0)
<br>
## Suggestion for follow-up studies
1. Using topic modeling, I would like to propose a study on a recommendation system that analyzes the shortcomings of previous companies and recommends companies that compensate for shortcomings in similar occupations.<br>
2. I would like to propose a study to understand the company's strategy to reflect the findings found in the current study and to determine the growth of the companies that implemented this strategy 5 to 10 years later.<br>
3. I think it would be good to conduct a follow-up study in business administration and statistics that suggests fundamental solutions to keywords such as **“소통, 보수, 꼰대, 복지”** that often appear in topics.

## Note
Code and models are only available for non-commercial research purposes.<br>
Good Luck :)

   

