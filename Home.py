import streamlit as st
import numpy as np
import requests
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.gridspec import GridSpec
import pandas as pd
from itertools import repeat

apptitle = 'Freight Rates'
st.set_page_config(page_title=apptitle, page_icon=":ship:", layout='wide')
st.title('Freight Rate Data Tool')

st.write(
    """
    This tool is a work in progress and will continue to be developed moving forward. The purpose of this tool is to reduce the 
    amount of time spent referencing multiple data sources to asses current freight rates.
    The sidebar includes links to view current freight rates from SeaRates and Freightos,
    as well as US fuel rate trends from the Energy Information Administration (EIA).
    """
)