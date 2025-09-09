import requests
import streamlit as st
import concurrent.futures



def format_url(url: str) -> str:
    url = url.removeprefix("http://").removeprefix("https://")
    url = url.removeprefix("www.")
    formated_url = "https://www." + url
    return formated_url
    

def check_site(formated_url):
    try:
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
            }
        r = requests.get(formated_url, headers=headers)
        if r.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False    
    

def main():
    st.title('Website Availability Checker')
    if "urls" not in st.session_state:
        st.session_state.urls = []

    url = st.text_input('Enter URL', value= "https://www.google.com/")
    formated_url = format_url(url)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button('Add URL', use_container_width=True):
            if formated_url not in st.session_state.urls:
                st.session_state.urls.append(formated_url)
            else:
                st.warning('URL is already in the list')    
    with col2:
        if st.button('Clear URLs', use_container_width=True):
            st.session_state.urls = []

    if st.button('Check Availability', use_container_width=True):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(check_site, u): idx for idx, u in enumerate(st.session_state.urls)}
            for future in concurrent.futures.as_completed(futures):
                idx = futures[future]
                with st.spinner(f'Checking {st.session_state.urls[idx]}'):
                    st.session_state[f"status_{idx}"] = future.result()


    if st.session_state.urls:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("URL")
            for idx, formated_url in enumerate(st.session_state.urls):
                st.write(formated_url)
        with col2:
            st.subheader("Status")
            for idx, formated_url in enumerate(st.session_state.urls):
                if st.session_state.get(f"status_{idx}"):
                    st.write(":white_check_mark:")
                elif st.session_state.get(f"status_{idx}") is False:     
                    st.write(":x:")       
                else:
                    st.write("")
    else:
        st.warning("Please add URLs to check avalability")


if __name__ == "__main__":
    main()













