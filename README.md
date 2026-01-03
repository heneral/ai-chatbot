# Beans AI Chatbot using Streamlit

📘 Project Description

The Beans AI Chatbot using Streamlit is a fun, bean-powered Python-based application that allows users to interact with an AI through a clean and user-friendly web interface. The chatbot accepts user input and responds in real time, simulating a natural conversation experience with a coffee-loving twist.

This project is built using Streamlit, making it easy to run in a browser without complex setup. It is designed for beginners who want to learn how chatbots work, how to handle user input, and how to display dynamic content using Python.

The chatbot can be extended to connect with AI models such as OpenAI, Hugging Face, or local language models to generate intelligent responses.

🎯 Project Purpose

Learn basic chatbot logic

Understand Streamlit UI components

Practice Python programming

Build a fun, branded AI-based application

Create custom branding for projects

🛠 Technologies Used

Python

Streamlit

🚀 Features

Simple chat interface

Real-time message display with streaming responses

Easy to customize and expand

Beginner-friendly structure

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/heneral/ai-chatbot.git
   cd ai-chatbot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Set up OpenAI API key for AI responses:
   - Sign up at [OpenAI](https://platform.openai.com/) and get an API key
   - Set the environment variable:
     ```bash
     export OPENAI_API_KEY="your-api-key-here"
     ```
   - Without the API key, the chatbot will fall back to echo mode

## Running the Application

To run the chatbot application, execute the following command:

```bash
streamlit run app.py
```

If `streamlit` is not found in your PATH (common with user installations), use:

```bash
python3 -m streamlit run app.py
```

This will start the Streamlit server, and you can access the chatbot in your web browser at `http://localhost:8501`.

## Live Demo
https://ai-chatbot-richardsawanaka.streamlit.app/
