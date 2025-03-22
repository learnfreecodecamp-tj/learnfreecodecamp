'''
analyze the census data
'''
import pandas as pd

def calculate():
        
    df = pd.read_csv('adult.data.csv')
    print(df.head())
    
    #1.How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
    cnt_race = df['race'].value_counts(ascending = False)
    print("#1 people count of each race:\n", cnt_race)
    
    #2 What is the average age of men?
    df_men = df[df['sex'] == 'Male']
    avg_age_men = round(df_men['age'].mean(),1)
    print('#2 average age of men is: ', avg_age_men)

    #3 What is the percentage of people who have a Bachelor's degree?
    cnt_bachelor = len(df[df['education'] == 'Bachelors'])
    cnt_total = len(df)
    pct_bachelor = round(cnt_bachelor/cnt_total*100,1) 
    print('#3 the percentage of people who have a Bachelor\'s degree is: ', pct_bachelor, '%')

    #4 What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    cnt_adv_morethan50 = len(df[(df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '>50K')])
    pct_adv_morethan50 = round(cnt_adv_morethan50/cnt_total*100,1) 
    print('#4 the percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K: ', pct_adv_morethan50, '%')

    #5 What percentage of people without advanced education make more than 50K?
    cnt_not_adv_morethan50 = len(df[(~df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '>50K')])
    pct_not_adv_morethan50 = round(cnt_not_adv_morethan50/cnt_total*100,1) 
    print('#5 the percentage of people without advanced education make more than 50K: ', pct_not_adv_morethan50, '%')

    #6 What is the minimum number of hours a person works per week?
    min_hours = df['hours-per-week'].min()
    print("#6 the minimum number of hours a person works per week is:", min_hours)

    #7 What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    cnt_min_morethan50 =  len(df[(df['hours-per-week'] == min_hours) & (df['salary'] == '>50K')])
    pct_min_morethan50 = round(cnt_min_morethan50/cnt_total*100,4) 
    print('#7 the percentage of the people who work the minimum number of hours per week have a salary of more than 50K: ', pct_min_morethan50, '%')

    #8 What country has the highest percentage of people that earn >50K and what is that percentage?
    d_country_morethan50 = df[df['salary'] == '>50K']
    highest_country_morethan50 = d_country_morethan50['native-country'].value_counts(ascending = False).head(1)
    name_country_morethan50 = highest_country_morethan50.index[0]
    cnt_country_morethan50 = highest_country_morethan50.iloc[0]
    pct_country_morethan50 = round(cnt_country_morethan50/cnt_total*100,4) 
    print('#8 ',name_country_morethan50, 'has the highest percentage of people that earn >50K and the percentage is: ', pct_country_morethan50, '%')
  
    #9 Identify the most popular occupation for those who earn >50K in India.
    #india_morethan50 = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    name_occup = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts(ascending = False).index[0]
    print('#9 the most popular occupation for those who earn >50K in India is: ', name_occup)    

    return 1
    