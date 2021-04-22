import streamlit as st

import requests

st.write('Dapp App')

url = "http://dapp-back:5005"

endpoint = '/api/connection/status/'

resp = requests.get(url+endpoint)

resp_json = resp.json()

st.write(resp_json)