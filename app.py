#Create a real time chat application with support for multiple rooms,typing indicators and message history
import streamlit as st
import time
# Initialize session state for chat history and typing indicators
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = {}
if 'typing_indicators' not in st.session_state:
    st.session_state.typing_indicators = {}
# Function to handle sending messages
def send_message(room, user, message):
    if room not in st.session_state.chat_history:
        st.session_state.chat_history[room] = []
    st.session_state.chat_history[room].append((user, message))
    st.session_state.typing_indicators[room] = False
# Function to handle typing indicators
def set_typing(room, user, is_typing):
    if room not in st.session_state.typing_indicators:
        st.session_state.typing_indicators[room] = {}
    st.session_state.typing_indicators[room][user] = is_typing
# Streamlit UI
st.title("Real-Time Chat Application")
room = st.text_input("Enter room name:")

if room:
    user = st.text_input("Enter your name:")
    message = st.text_input("Enter your message:")
    if st.button("Send"):
        send_message(room, user, message)
    if st.session_state.typing_indicators.get(room):
        st.write(f"{user} is typing...")
    if room in st.session_state.chat_history:
        for sender, msg in st.session_state.chat_history[room]:
            st.write(f"{sender}: {msg}")
    set_typing(room, user, True)
    time.sleep(1)  # Simulate typing delay
    set_typing(room, user, False)
