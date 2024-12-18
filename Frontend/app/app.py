import streamlit as st
import requests
import time
import random
from static.constants import department, contact_options, predefined_responses

# Streamed response emulator
def response_generator(message: str):
    """Simulate a streaming response."""
    response = message
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# FastAPI backend URL
BACKEND_URL = "http://localhost:8000/webhook"

st.title("Simple Chat with Backend")

# Initialize session state for the selector and chat messages
if "contact_method" not in st.session_state:
    st.session_state.topic = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# Step 1: Select department
topic = st.selectbox("Select department to contact:", ["Select an option"] + department)

if topic != "Select an option":
    # Save the selected topic in session state
    st.session_state.topic = topic

    # Extract department, description, and contact method
    selected_index = department.index(topic)
    department = topic.split(' - ')[0]
    description = topic.split(' - ')[1]
    contact_method = contact_options[selected_index]

    #Configure params to post call
    params = {"topic": department, "description": description, "method": contact_method}

    # Send POST request to backend
    try:
        response = requests.post(
            BACKEND_URL, json = params
        )
        response.raise_for_status()
        backend_response = response.json().get("message", "No response from backend.")
    except requests.RequestException as e:
        st.error(f"Error contacting backend: {str(e)}")

    st.success(f"**Don't tell anyone 🤫 but we have sent a notification to:** {backend_response["department"]} department by {backend_response["method"]}")
    
# Step 2: Display chat only if a contact method is chosen
if st.session_state.topic:
    st.write(f"***Chat with our bot***")

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input for the chat
    if prompt := st.chat_input("What would you like to ask?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a random predefined response based on the department
        department_name = st.session_state.topic.split(' - ')[0]
        response = random.choice(predefined_responses[department_name])

        # Display assistant response
        with st.chat_message("assistant"):
            st.write_stream(response_generator(response))

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

