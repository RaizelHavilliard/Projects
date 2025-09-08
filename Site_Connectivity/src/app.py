import requests
import streamlit as st
import concurrent.futures


def format_url():

    for url in url:
        url = url.removeprefix("http://").removeprefix("https://")
        url = url.removeprefix("www.")
        return url
    formated_url = "https://www." + url
    return formated_url

def check_site(url):
    try:
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
            }
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False    
    

def main():
    st.title('Website Availability Checker')

    url = st.text_input('Enter URL', value= "https://www.google.com/")
    url = format_url(url)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button('Check avalability'):
            if url not in st.session_state.urls:
                st.session_state.urls.append(url)
            else:
                st.warning('Please enter a valid URL')    
    with col2:
        if st.button('Clear URLs'):
            st.session_state.urls = []

    if st.button('Check Avalability'):
        for idx, url in enumerate(st.session_state.urls):
            st.session_state[f"status_{idx}"] = check_site(url)

            with st.spinner(F'Checking {url}'):
                with concurrent.futures.ThreadPoolExecutor() as executer:
                    futurs = executer.submit(check_site, url)
                    st.session_state[f"status_{idx}"] = futurs.result()

    if st.session_state.urls:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("URL")
            for idx, url in enumerate(st.session_state.urls):
                st.write(url)
        with col2:
            st.subheader("Status")
            for idx, url in enumerate(st.session_state.urls):
                if st.session_state.get(f"status_{idx}"):
                    st.write(":white_check_mark:")
                elif st.session_state.get(f"status_{idx}") is False:     
                    st.write(":x:")       
                else:
                    st.write("")
    else:
        st.warning("Please ass URLs to check avalability")


if __name__ == "__main__":
    main()













