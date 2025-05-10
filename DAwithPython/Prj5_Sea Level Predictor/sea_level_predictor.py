'''
project 5
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    #1.Use Pandas to import the data from epa-sea-level.csv.
    df = pd.read_csv('epa-sea-level.csv')
    df.head()
    
    #2.Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    #x = df['Year']
    #y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots()
    #plt.scatter(x, y, c=np.sign(y))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    #3.Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series([i for i in range(1880,2051)])
    y = res.intercept + res.slope * x
    plt.plot(x , y , 'o', label= "1880-2050 predict")
    #plt.show()
    
    #4.Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    new_df = df[df['Year'] >= 2000]
    res1 = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x1 = pd.Series([i for i in range(2000,2051)])
    y1 = res1.intercept + res1.slope * x1
    plt.plot(x1 , y1 , 'r', label= "2000-2050 predict")
    
    #5.The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    plt.savefig('sea_level_plot.png')
    return plt.gca()

