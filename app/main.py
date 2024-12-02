import streamlit as st

from scraper import fetch_page_content
from chains import Chain
from technology import Technology
from utils import clean_text

def create_streamlit_app(llm, technology, clean_text):
    st.title("Cover Letter Generator")
    url_input = st.text_input("Enter a job URL:", value="https://www.ziprecruiter.com/c/Glassdoor/Job/Lead-IT-System-Engineer/-in-Austin,TX?jid=5e69078f9a6a4d95")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            data = clean_text(fetch_page_content(url_input))
            technology.load_technologies()
            task = llm.extract_task(data)
            skills = task.get('skills')
            links = technology.query_links(skills)
            coverletter = llm.generate_cover_letter(task, links)
            st.markdown(coverletter,)
            
        except Exception as e:
            st.error("An error occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    technology = Technology()
    st.set_page_config(page_title="Cover Letter Generator")
    create_streamlit_app(chain, technology, clean_text)