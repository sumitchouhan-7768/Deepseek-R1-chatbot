import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Set up page configuration for better design
st.set_page_config(page_title="Mr. Spock Chatbot", layout="centered")

# Main chatbot interface
st.title("🖖 MR. Spock Chatbot using Deepseek R1")

# Sidebar instructions
with st.sidebar:
    st.markdown("### Instructions")
    st.write("1. Enter your question in the input box below.")
    st.write("2. Click **Submit** to get a response.")
    st.write("3. Scroll to see chat history.")

# Define template for the chatbot prompt
template = """question: {question}
answer = Generate the answer step by step."""

prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="deepseek-r1")
chain = prompt | model

# Chat history for better user interaction
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input field for user question
question = st.text_input("💬 Enter your question here:", key="question_input")

# Submit button to trigger the chatbot
if st.button("Submit"):
    if question.strip():
        try:
            # Get chatbot response
            formatted_prompt = prompt.format(question=question)
            response = chain.invoke({"question": question})
            st.session_state.chat_history.append(("User", question))
            st.session_state.chat_history.append(("Mr. Spock", response))

        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a valid question.")

# Display chat history with a cleaner UI
for sender, message in st.session_state.chat_history:
    if sender == "User":
        st.markdown(f"**🧑‍💻 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")
