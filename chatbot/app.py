import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the template and model
template = """
Answer the question below.

Here is the conversation history:
{context}

Question: {question}

Answer:
"""
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Streamlit app definition
def main():
    st.title("AI Chatbot")
    st.write("Welcome to the AI chatbot! Type your message below.")

    # Initialize session state variables
    if "context" not in st.session_state:
        st.session_state.context = ""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "visible_chat" not in st.session_state:
        st.session_state.visible_chat = []

    # Temporary variable for user input
    user_input = st.text_input("Type your message:")

    # Buttons for sending and clearing chat
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Send"):
            if user_input.strip():
                try:
                    # Get the response from the chatbot
                    result = chain.invoke({"context": st.session_state.context, "question": user_input})

                    # Append user and bot messages to the visible chat
                    st.session_state.visible_chat.append(("You", user_input))
                    st.session_state.visible_chat.append(("Bot", result))

                    # Append to full chat history (not displayed)
                    st.session_state.chat_history.append(("You", user_input))
                    st.session_state.chat_history.append(("Bot", result))

                    # Update the context (limit to last 20 exchanges)
                    st.session_state.context += f"\nUser: {user_input}\nAI: {result}"
                    if len(st.session_state.context.splitlines()) > 20:
                        st.session_state.context = "\n".join(st.session_state.context.splitlines()[-20:])

                    # Reset the temporary input variable
                    user_input = ""
                    st.success("Message sent!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    with col2:
        if st.button("Clear Screen"):
            # Clear only the visible chat
            st.session_state.visible_chat = []
            st.success("Chat screen cleared!")

    # Display visible chat
    for sender, message in st.session_state.visible_chat:
        if sender == "You":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**Bot:** {message}")

if __name__ == "__main__":
    main()
