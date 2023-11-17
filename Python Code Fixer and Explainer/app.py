import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, hide_pages

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
   

title_m = '<p style="font-size: 30px;"><b>Python Code Fixer Powered By CodeLLAMA</b></p>'
st.markdown(title_m, unsafe_allow_html=True)


show_pages([
    Page("app.py","App"),
    Page("solution.py","Solution")
])

hide_pages(['Solution'])



if 'user_select_value' not in st.session_state:
    st.session_state['user_select_value'] = 0 

user_select_value = st.session_state['user_select_value']

errored_code = st.text_area(label='Errored Code', height=300)
error = st.text_area(label='Error', height=300)
submit = st.button("Submit", type="primary")


if submit:
    if errored_code and error:
        st.session_state['user_select_value'] = [errored_code, error]
        switch_page('Solution')



