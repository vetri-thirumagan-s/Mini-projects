import streamlit as st
import main_url

st.set_page_config(page_title='url_shortening',page_icon=':link:')

st.title('URL FUNCTIONALITIES')

col1 , col2 = st.columns(2,gap="large")

with col1:

    st.subheader('URL_SHORTENENING')
    url = st.text_input("Enter the link you need to shorten 🔗")

    if url:

        short_url = main_url.shortening(url)
        st.write("Your link  ➡️ ",short_url)
        copy_button1 = st.button('copy')
        if copy_button1:
            main_url.copy(short_url)


with col2:
        
    st.subheader('URL_EXPANDING')
    url = st.text_input("Enter the link you need to expand 🔗")

    if url:

        long_url = main_url.expanding(url)
        st.write("Your link  ➡️ ",long_url)
        copy_button2 = st.button('copy original link')
        if copy_button2:
            main_url.copy(long_url)
