# Level 3 - Task 1: Django Web App with Authentication

A secure Django-based web application featuring user registration, login, logout, and a protected dashboard.

## Features
- **User Authentication**: Secure registration and login using Django's built-in auth system.
- **Protected Routes**: Dashboard is restricted to authenticated users only.
- **Responsive UI**: Styled with Bootstrap 5 for a modern, mobile-friendly look.
- **Admin Panel**: Full user management via the Django Admin interface.

## Setup Instructions
1. **Clone the repository**:
   `git clone <your-repo-url>`
2. **Create and activate a virtual environment**:
   `python -m venv venv`
   `source venv/bin/activate`
3. **Install dependencies**:
   `pip install -r requirements.txt`
4. **Run Migrations**:
   `python manage.py migrate`
5. **Start the server**:
   `python manage.py runserver`

## Tech Stack
- Python 3.12
- Django 6.0
- Bootstrap 5

