# Customer Support Chatbot Web App — Setup & Usage Guide

## Overview
This project is a minimal AI chatbot web application using **Flask (Python)** for the backend and **HTML/CSS/JS** for a frontend UI. It allows users to input text and receive responses in a chat-style format.


### Folder Structure
<pre> ### Folder Structure ``` RAG/ ├── app.py ├── rag_pipeline.py ├── requirements.txt ├── README.md ├── chroma_db/ └── templates/ └── index.html ``` </pre>


### Requirements

-  Python 3.11
- `pip` (Python package installer)


### Installation

1. Clone the Repository
   ```bash
   git clone https://github.com/yourusername/ai-chatbot.git
   cd ai-chatbot
   ```

2. Create Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

4.  Run the App
    ```bash
    flask run
    ```

Visit: [http://127.0.0.1:5000]

---

### How It Works

- User types a message into the chat box.
- The frontend sends the message to the Flask backend via `fetch('/Chatbot')`.
- The Flask server:
    - recieve the message 
    - find the 5 similar sentenses from vector DB.
    - Sends 5 sentenses and query to LLM and recieves the structured answer for query from LLM.
    - Returns the answer to frontend
- The frontend displays the answer dynamically in the chat interface.

---


### Theming & UI

You can customize the UI by editing CSS inside `index.html`.  
Change colors, fonts, or layout to suit your brand (blue theme is default).

---

### Future Enhancements

- Add OpenAI / GPT backend
- Create vector db after cleaning the data.
- Store chat history in a database (SQLite, PostgreSQL)
- Add timestamps to messages
- Add user login/authentication

---

## Author

**Shreeganesha**  
Email: shreeganesha@2001@gmail.com
GitHub: [@yourusername](https://github.com/yourusername)
