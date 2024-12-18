# AI Chatbot using LangChain and Streamlit

This project implements an AI chatbot using the **LangChain** library for AI interaction and **Streamlit** for creating an interactive web application. The chatbot leverages the **Ollama** model to generate responses to user queries while maintaining conversation context.

## Features

- **Interactive Chat:** Users can interact with the chatbot and receive intelligent responses.
- **Conversation History:** The chatbot remembers the conversation context and responds accordingly.
- **Clear Screen Functionality:** A button to clear the visible chat history without affecting the full conversation context or history.
- **Streamlit Interface:** A clean, easy-to-use interface built with Streamlit, allowing real-time communication with the AI.

## Requirements

To run this project locally, make sure you have the following installed:

- [Python 3.7+](https://www.python.org/downloads/)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/) (Ensure you have access to the Ollama LLM model)

You can install the necessary dependencies using the following commands:

```bash
pip install streamlit langchain_ollama langchain_core

Project Structure.
├── app.py                  # Main Streamlit app
├── README.md               # Project documentation
└── requirements.txt        # List of dependencies
