# PyBot - Your Intelligent Chat Assistant

**PyBot** is an AI-powered chatbot application designed to help users with various queries. Built using Flask, it leverages machine learning models and provides a simple, intuitive interface for users to interact with. With features like recent chats, dynamic responses, and a beautiful UI, PyBot is your go-to assistant for answering any question!

![PyBot Sample](./images/sample.png)

## Features

- **Intelligent Chatbot**: Ask any query and get real-time responses powered by AI.
- **Recent Chats**: View and revisit your past conversations.
- **Responsive Design**: The app is fully responsive and works seamlessly across all devices.
- **Interactive UI**: With a modern and visually appealing design that features a semi-transparent background and smooth interactions.
- **Real-time Communication**: Instant feedback on your queries with smooth messaging interactions.
- **Customizable**: Add more features and customize the backend or frontend as needed.

## Tech Stack

- **Frontend**: 
  - HTML5, CSS3, JavaScript
  - Responsive Layout using Flexbox
  - Google Fonts (Inter font family)
  - Tailwind CSS for utility-based styling
  - JavaScript for dynamic functionality

- **Backend**:
  - Flask (Python framework)
  - APIs for handling user queries and responses
  
- **Additional**:
  - Machine Learning for chatbot responses (could be integrated with any AI-powered library in the future)

## Project Structure

```plaintext
pybot/
├── app.py                 # Main Flask application
├── templates/             # HTML files for the app (frontend)
│   └── index.html         # Main chatbot interface
├── static/                # Static files (CSS, JS, images)
├── requirements.txt       # Python dependencies
└── README.md              # Documentation for the project
```

## Clone the Repository

```bash
git clone https://github.com/prashant-sagar-shakya/PyBot.git
cd PyBot
```
#### Obtain your open-ai api-key and paste it in ***app.py*** **openai.api_key = "your_openai_api_key"**
### Set Up a Virtual Environment for the Project
**Setup On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your web browser and visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the application.

## Contact

For any inquiries or support, please contact:

- **Name**: Prashant Sagar Shakya
- **Email**: prashant43602003@gmail.com
- **GitHub**: [prashant-sagar-shakya](https://github.com/prashant-sagar-shakya)
