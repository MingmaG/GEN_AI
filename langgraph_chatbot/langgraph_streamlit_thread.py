import streamlit as st
from langgraph_chatbot import chatbot
from langchain_core.messages import HumanMessage
import uuid
from dotenv import load_dotenv
load_dotenv()
#********* utility functions ****

def generate_thread():
    thread_id = uuid.uuid4()
    return thread_id

#******** reset ui **************

def reset_chat():
    thread_id = generate_thread()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id, title = 'New Chat'):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'][thread_id] = title


def load_conversation(thread_id):
    state = chatbot.get_state(config={'configurable':{'thread_id': thread_id}})
    return state.values.get("messages",[])
    
def generate_thread_title(text, max_len=30):
    text = text.strip()
    return text[:max_len] if text else "New Chat"

    
# st.session_state -> dict -> 

#*********session setup *********

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = {}
    
add_thread(st.session_state['thread_id'])



#********* Sidebar UI ***********
 
st.sidebar.title('Langgraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My conversations')

for thread_id, title in reversed(list(st.session_state['chat_threads'].items())):
    if st.sidebar.button(title, key=f"thread_btn_{thread_id}"):
        st.session_state['thread_id'] = thread_id

        messages = load_conversation(thread_id)
        temp_messages = []

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_messages.append({'role': role, 'content':msg.content})
        st.session_state['message_history'] = temp_messages
      
           
#********* Main UI **************

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)
    CONFIG = {'configurable':  {'thread_id':st.session_state['thread_id']}}

    with st.chat_message('assistant'):
        
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream({'messages':[HumanMessage(content=user_input)]},
            config = CONFIG, 
            stream_mode='messages')
        )
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})

# Set readable title only once
    if st.session_state['chat_threads'][st.session_state['thread_id']] == "New Chat":
        st.session_state['chat_threads'][st.session_state['thread_id']] = \
            generate_thread_title(user_input)
