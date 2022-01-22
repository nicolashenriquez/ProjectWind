import streamlit as st
import datetime
import requests
'''
# TaxiFareModel
'''

columns1= st.columns(2)
columns2 = st.columns(2)
columns3 = st.columns(2)
d = columns1[0].date_input("When's your trip", datetime.date(2019, 7, 6))
t = columns1[1].time_input('Set an alarm for', datetime.time(8, 45))
pickup_lon = columns2[0].number_input('Inster pickup longitud')
pickup_lat = columns2[1].number_input('Inster pickup latitud')
dropoff_lon = columns3[0].number_input('Inster dropoff longitud')
dropoff_lat = columns3[1].number_input('Inster dropoff latitud')


passanger_count = st.slider('Select a modulus', 1, 4, 1)
date = datetime.datetime(d.year,d.month, d.day, hour =t.hour, minute = t.minute, second=t.second)



dic ={
    "pickup_datetime" : date,
    "pickup_longitude" : pickup_lon,
    "pickup_latitude" : pickup_lat,
    "dropoff_longitude" : dropoff_lon,
    "dropoff_latitude" : dropoff_lon,
    "passenger_count" : passanger_count
}


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )

st.write(requests.get(url, params=dic).json())
