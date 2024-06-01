from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Set page configuration with a custom title and potentially a favicon
st.set_page_config(page_title="Chat with Gemini", page_icon=":robot:")  # Replace ":robot:" with a custom favicon path if desired

# Header with potentially a custom background color
with st.container():
    st.markdown("<h1 style='text-align: center; color: #333'>Made with Gemini API</h1>", unsafe_allow_html=True)  # Adjust color as needed

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Input field with a placeholder text
input_box = st.container()
with input_box:
    input = st.text_input("", key="input", placeholder="What would you like to ask?")

submit = st.button("Ask Question?")

if submit and input:
    # Append the new question to the chat history
    st.session_state.chat_history.append(input)
    response = get_gemini_response(input)

    # Subheader with custom class (no style argument)
    st.markdown("<h3 style='font-weight: bold; color: #007bff;'>The Response is:</h3>", unsafe_allow_html=True)  # Use markdown

    for chunk in response:
        st.write(chunk.text)
        # Append the response to the chat history
        st.session_state.chat_history.append(("Google", chunk.text))

    # Chat history with Markdown formatting
    chat_history_container = st.container()
    with chat_history_container:
        st.markdown("<h3 style='font-weight: bold; color: #6c757d;'>Chat History:</h3>", unsafe_allow_html=True)  # Use markdown
        # Create the dropdown
        chat_history_dropdown = st.selectbox("Chat History", options=st.session_state['chat_history'], format_func=lambda item: f"**{item[0]}**: {item[1]}")
        # Display selected item 
        # Note: The `chat_history_dropdown` variable holds the selected item
        # You can use it to perform actions based on the user's choice
        st.write(f"You selected: {chat_history_dropdown}")

# Add CSS styles using st.markdown
st.markdown(
    """
    <style>
    /* Style the header */
    h1 {
        text-align: center;
        color: #333;
    }

    /* Style the input field */
    input[type="text"] {
        /* Target input elements of type text */
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
    }

    /* Style the subheaders */
    .subheader {
        font-weight: bold;
        color: #007bff;
    }

    /* Style the subheaders */
    .response_subheader {
        font-weight: bold;
        color: #007bff;
    }

    .chat_history_subheader {
        font-weight: bold;
        color: #6c757d;
        /* Adjust color as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)