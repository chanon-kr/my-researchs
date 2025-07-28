# Load ENV
from dotenv import load_dotenv
load_dotenv()
# Get Graph
from graph.graph import graph
# Streamlit
import streamlit as st
from datetime import datetime

create_session= lambda : datetime.now().strftime(f'%Y%m%d%H%M%S')

if 'session_id' not in st.session_state :
    session_id = st.session_state.session_id = create_session()


st.header("Chatbot")
st.set_page_config(page_title= 'Chatbot', 
                   page_icon="📊", 
                   initial_sidebar_state="expanded", 
                   layout='wide')

st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 2rem;
                    padding-right: 2rem;
                }
        </style>
        """, unsafe_allow_html=True)

with st.sidebar:
    st.write('# Option')
    if st.button("Reset Session"):
        session_id = st.session_state.session_id = create_session()
        st.rerun() 
    model_name= st.session_state.model_name = st.selectbox(
    'Select Model, not use yet',
    [
    'gemini-2.0-flash',
    'gemini-2.0-flash-lite',
    'gemini-2.5-flash',
    'gemini-2.5-flash-lite',
    ])
    
prompt = st.chat_input("Prompt")
thread = {"configurable": {"thread_id": st.session_state.session_id}}

if prompt:
    with st.spinner("Generating response.."):
        if graph.get_state(thread).next :
            graph.update_state(thread, {"messages": [('human', prompt)]},)
            user_input= None
        else :
            user_input= {'messages' : prompt}
        generated_response = graph.invoke(user_input, thread)
        messages= [(x.type, x.content) for x in generated_response['messages']]
        for x in messages :
            st.chat_message(x[0]).write(x[1])