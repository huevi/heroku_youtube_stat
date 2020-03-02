import streamlit as st

import os

def main():
    """"simple app"""
    st.title("A simple app")
    title = st.text_input('Enter password', 'password')
    if title == "Newtime":
        scrape = True
    if st.button('scrape youtube trends'):
        st.write('Why hello there')
        if scrape:
            os.system("python scraper.py")
        else:
            st.write('enter correct password')
    else:
        st.write('Goodbye')

if __name__ == "__main__":
    main()