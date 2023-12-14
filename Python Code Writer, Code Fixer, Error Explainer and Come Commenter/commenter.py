import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, hide_pages
from c_model import get_commented_code

st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "Navigation Zone";
                margin-left: 20px;
                margin-bottom: 20px;
                font-size: 20px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
   

show_pages([
    Page("fixer.py","Code Fixer"),
    Page("generator.py","Code Generator"),
    Page("commenter.py","Code Commenter"),

    Page("solution.py","Solution"),

])

hide_pages(['Solution'])




title_m = '<p style="font-size: 30px;"><b>Python Code Commenter</b></p>'
st.markdown(title_m, unsafe_allow_html=True)


users_code = st.text_area(label='Drop your CODE', height=450)
submit = st.button("Comment The Code", type="primary")

if submit:
    if users_code:
        st.info("AI Commenting Your CODE... Please wait ⏳")
        output = get_commented_code(users_code)
        print('Done')
        st.code(output)


