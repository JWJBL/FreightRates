import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.gridspec import GridSpec

st.title('Fuel Rates')

with st.spinner('Loading Freightos Rates...'):
    url = "https://www.eia.gov/petroleum/gasdiesel/"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    soup = BeautifulSoup(response.text, 'html.parser')
    first_table = soup.find('table')
    table_data = []
    for row in first_table.find_all('tr'):
        row_data = []
        for cell in row.find_all(['th', 'td']):
            row_data.append(cell.text.strip())
        table_data.append(row_data)
    regular_gas_prices = pd.DataFrame(table_data[2:], columns=table_data[1])
    regular_gas_prices.columns.values[4]="1 wk change"
    regular_gas_prices.columns.values[5]="1 yr change"

    second_table = soup.find_all('table')[1] 
    table_data = []
    for row in first_table.find_all('tr'):
        row_data = []
        for cell in row.find_all(['th', 'td']):
            row_data.append(cell.text.strip())
        table_data.append(row_data)
    diesel_prices = pd.DataFrame(table_data[2:], columns=table_data[1])
    diesel_prices.columns.values[4]="1 wk change"
    diesel_prices.columns.values[5]="1 yr change"

    fig = plt.figure(figsize=(16,16))
    plt.rcParams['font.family'] = 'Segoe UI'
    gs = GridSpec(nrows=2, ncols=1, height_ratios=[1,1])
    ax0 = fig.add_subplot(gs[0, :])
    ax0.axis('off')
    ax0.set_title("Regular Gas (eia.gov)", fontsize=24)
    table0= ax0.table( 
        cellText = regular_gas_prices.values,
        colLabels= regular_gas_prices.columns,
        rowLoc = 'left',
        cellLoc ='center',  
        loc ='upper left')
    table0.auto_set_font_size(False)     
    table0.auto_set_column_width(col=list(range(len(regular_gas_prices.columns))))
    table0.set_fontsize(24)
    table0.scale(1,3)

    ax1 = fig.add_subplot(gs[1, :])
    ax1.axis('off')
    ax1.set_title("Diesel (eia.gov)", fontsize=24)
    table1= ax1.table( 
        cellText = diesel_prices.values,
        colLabels= diesel_prices.columns,
        rowLoc = 'left',
        cellLoc ='center',  
        loc ='upper left')
    table1.auto_set_font_size(False)     
    table1.auto_set_column_width(col=list(range(len(diesel_prices.columns))))
    table1.set_fontsize(24)
    table1.scale(1,3)


    st.pyplot(plt.gcf())