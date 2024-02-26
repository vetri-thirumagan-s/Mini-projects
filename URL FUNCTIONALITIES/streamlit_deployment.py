import pyshorteners as pyshort
import pyperclip
import streamlit as st


def shortening(url):

  #  Creates a URL shortener object
  short_url = pyshort.Shortener()

  # Provides access to shortening
  return short_url.tinyurl.short(url)

def expanding(url):

  #  Creates a URL shortener object
  long_url = pyshort.Shortener()

  # Provides access to expanding
  return long_url.tinyurl.expand(url)       


def copy(text_to_be_copied):
    return pyperclip.copy(text_to_be_copied)


st.set_page_config(page_title='url_shortening',page_icon=':link:')

st.title('URL FUNCTIONALITIES')

col1 , col2 = st.columns(2,gap="large")

with col1:

    st.subheader('URL_SHORTENENING')
    url = st.text_input("Enter the link you need to shorten 🔗")

    if url:

        short_url = shortening(url)
        st.write("Your link  ➡️ ",short_url)
        copy_button1 = st.button('copy')
        if copy_button1:
            copy(short_url)


with col2:
        
    st.subheader('URL_EXPANDING')
    url = st.text_input("Enter the link you need to expand 🔗")

    if url:

        long_url = expanding(url)
        st.write("Your link  ➡️ ",long_url)
        copy_button2 = st.button('copy original link')
        if copy_button2:
            copy(long_url)