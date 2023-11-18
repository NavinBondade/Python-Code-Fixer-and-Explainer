import streamlit as st
from model import get_fixed_code,get_explanation
import time

# progress_text = "Operation in progress. Please wait."
# my_bar = st.progress(0, text=progress_text)


# for percent_complete in range(100):
    

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
   

with st.spinner('Wait, Model Fixing The Code...'):
    code = st.session_state['user_select_value'][0]
    error = st.session_state['user_select_value'][1]
    fixed_code = get_fixed_code(code, error)
    error_explain = get_explanation(error)


print(fixed_code)
print(error_explain)



code_m = '<p style="font-size: 30px;"><b>Your Errored Code</b></p>'
st.markdown(code_m, unsafe_allow_html=True)
st.code(code, language='python')



error_m = '<p style="font-size: 30px;"><b>Generated Error</b></p>'
st.markdown(error_m, unsafe_allow_html=True)
st.code(error, language='python')


fixed_code_m = '<p style="font-size: 30px;"><b>Fixed Code By  AI</b></p>'
st.markdown(fixed_code_m, unsafe_allow_html=True)
st.code(fixed_code, language='python')


error_explain_m = '<p style="font-size: 30px;"><b>Fixed Code Explanation By AI</b></p>'
st.markdown(error_explain_m, unsafe_allow_html=True)
st.code(error_explain, language='python')


# st.markdown(f'<p style="background-color:#F8F9FB; padding=10px">{st.session_state["user_select_value"][1]}</p>', unsafe_allow_html=True)
#st.markdown(original_title, unsafe_allow_html=True)
# st.write(st.session_state['user_select_value'][1])

# st.write(error)