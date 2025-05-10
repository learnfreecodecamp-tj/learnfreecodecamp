'''
project 4
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


#1. Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
df = pd.read_csv('fcc-forum-pageviews.csv')
df.head()

#2. Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

#3.Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(30, 8))
    ax.plot(df.index, df['value'], color='blue')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.show()

    fig.savefig('line_plot.png')
    return fig

#4. Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
def draw_bar_plot():
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['date'] = pd.to_datetime(df_bar['date'])
    df_bar['Years'] = df_bar['date'].dt.year
    df_bar['Months'] = df_bar['date'].dt.month_name()
    
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    mapping = {month: i for i, month in enumerate(months)}
    key = df_bar['Months'].map(mapping)
    df_bar.iloc[key.argsort()]
    
    #draw image
    fig, ax = plt.subplots(figsize=(10, 10))
    df_bar.pivot_table(index='Years', columns=key, values='value', fill_value=0).plot(kind='bar', label='Months', stacked=False, figsize=(9,6), ax=ax)
    labels =  ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    plt.legend(labels=labels, title='Months')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    ax.set_title('Average Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.tight_layout()
    #plt.show(fig)

    fig.savefig('bar_plot.png')
    return fig

#5.Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.
def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['date'] = pd.to_datetime(df_box['date'])  #otherwise will occur, 'str' object has no attribute 'year'
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,5))
    a1 = sns.boxplot(y='value', x='year', data=df_box, ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    mapping = {month: i for i, month in enumerate(months)}
    key = df_box['month'].map(mapping)
    key = pd.DataFrame(key)
    df_box['key'] = key['month']
    a2 = sns.boxplot(x='key', y='value', data=df_box, ax=ax2)
    my_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')
    #plt.show(fig)

    fig.savefig('box_plot.png')
    return fig
    


