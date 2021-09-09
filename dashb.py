import streamlit as st
import csv
import urllib.request
import pandas as pd
st.title('Covid Dashboard')
district_wise_url = "http://api.covid19india.org/csv/latest/cowin_vaccine_data_districtwise.csv"
vac_state_wise_url = "http://api.covid19india.org/csv/latest/vaccine_doses_statewise.csv"
india_vac_url = "http://api.covid19india.org/csv/latest/cowin_vaccine_data_statewise.csv"
selected = st.sidebar.selectbox("View Data by", ("Choose Below","District","State","Country","View All"))


if selected == "Choose Below":
    st.info("Choose any option from the Sidebar to access the data")


if selected =="District":
    st.info("This might take upto 30 seconds, as we are fetching the Data Realtime")
    url = district_wise_url
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    dist_data = []
    for row in cr:
        dist_data.append(row)
    dist_df = pd.DataFrame(dist_data)
    st.dataframe(dist_df)


if selected == "State":
    st.info("This might take upto 30 seconds, as we are fetching the Data Realtime")
    url = vac_state_wise_url
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    state_data = []
    for row in cr:
        state_data.append(row)
    state_df = pd.DataFrame(state_data)
    st.dataframe(state_df)


if selected == "Country":
    st.info("This might take upto 30 seconds, as we are fetching the Data Realtime")
    url = india_vac_url
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    india_data = []
    for row in cr:
        india_data.append(row)
    india_df = pd.DataFrame(india_data)
    st.dataframe(india_df)


if selected == "View All":
    st.info("This might take upto 30 seconds, as we are fetching the Data Realtime")
    url = district_wise_url
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    dist_data = []
    for row in cr:
        dist_data.append(row)
    dist_df = pd.DataFrame(dist_data)
    url = vac_state_wise_url
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    state_data = []
    for row in cr:
        state_data.append(row)
    state_df = pd.DataFrame(state_data)
    url = india_vac_url
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    india_data = []
    for row in cr:
        india_data.append(row)
    india_df = pd.DataFrame(india_data)
    st.dataframe(dist_df)
    st.dataframe(state_df)
    st.dataframe(india_df)