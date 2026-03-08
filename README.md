# Flask Blog Application

A full-featured blog web application built using the Python microframework Flask.

The application allows users to register, log in, create posts, and interact with a dynamic blogging platform while following secure development practices.

---

## Features

###  User Authentication

- User registration and login system
- Secure session management
- Password reset functionality

###  Security Practices

- Passwords stored using secure hashing
- CSRF protection implemented in forms
- Application secret keys protected using environment variables

###  Blog Functionality

- Create, edit, and delete blog posts
- View posts from different users
- Pagination for posts

###  Error Handling

- Custom error pages for common HTTP errors
- User-friendly error messages

---

## Technologies Used

### Backend

- **Python** - Programming language
- **Flask** - Micro web framework

### Frontend

- **HTML** - Markup
- **CSS** - Styling
- **Jinja2** - Template engine

### Security

- **Password hashing** - Secure password storage
- **CSRF protection** - Form security
- **Environment variables** - Secret management

### Tools

- **Git** - Version control
- **GitHub** - Repository hosting
- **pip** - Python package manager

---

## Project Structure
```
flask-blog-app
│
├── app/
│   ├── users/          # User authentication logic
│   ├── posts/          # Blog post routes and logic
│   ├── errors/         # Custom error handlers
│   ├── templates/      # HTML templates
│   ├── static/         # CSS and static assets
│   ├── __init__.py     # Application factory
│   ├── config.py       # Configuration settings
│   └── models.py       # Database models
│
├── instance/           # Instance-specific files
├── run.py              # Application entry point
├── .gitignore
└── README.md
```
---


## Installation and Setup

### 1. Clone the repository
git clone https://github.com/yashisaini718/flask-blog-app.git

cd flask-blog-app
### 2. Create a virtual environment
python -m venv venv

Activate the environment:
 - **Mac/Linux:** source venv/bin/activate
 - **Windows:** venv\Scripts\activate
### 3. Install dependencies
pip install -r requirements.txt
### 4. Run the application
python run.py

The application will run on : http://127.0.0.1:5000

---

## Security Consideration

Sensitive data such as secret keys and credentials are not stored in the repository.
These values should be placed inside a .env file which is excluded using .gitignore.

---

## Learning Outcome

Through this project I explored:
- Backend web development using Flask
- Secure authentication systems
- Password hashing techniques
- CSRF protection mechanisms
- Modular application design using Blueprints
- Version control using Git and GitHub
