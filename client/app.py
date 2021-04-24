import streamlit as st

import requests

st.write('Dapp App')

url = "http://dapp-back:5005"

def home():
    ''' landing page untuk project'''
    st.subheader('Rumah')

def conn_status():
    endpoint = '/api/connection/status/'
    
    resp = requests.get(url+endpoint)
    
    resp_json = resp.json()
    
    st.write(resp_json)

def block_num():
    endpoint = '/api/eth/block/number'
    
    resp = requests.get(url+endpoint)
    
    resp_json = resp.json()
    
    st.write(resp_json)

def accounts_known():
    endpoint = '/api/eth/accounts'
    
    resp = requests.get(url+endpoint)
    
    resp_json = resp.json()
    
    st.write(resp_json)

def accounts_balance():
    st.write('Please Provide Wallet Address')

    account = st.text_input('Provide wallet address here')

    if account:
        if st.button('Balance'):
            endpoint = f'/api/eth/balance/{account}'
    
            resp = requests.get(url+endpoint)
    
            resp_json = resp.json()
    
            st.write(resp_json)

def main():
    st.title('Twistcode - Ethflow')
    menu = [
        'Home', 
        'General',
        'Accounts'
    ]
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'General':
        conn_status()
        block_num()
    elif choice == 'Accounts':
        accounts_known()
        accounts_balance()
    else:
        home()

if __name__ == '__main__':
    main()