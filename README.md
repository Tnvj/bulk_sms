# SMS Application

This project is a simple SMS application built with Django. It includes user registration, login, profile updates, and basic SMS functionalities.

## Prerequisites

- Python 3.x
- MySQL server
- Pip (Python package installer)

## Installation

1. **Clone the repository**

    ```sh
    git clone https://github.com/Tnvj/bulk_sms
    cd bulk_sms
    ```

2. **Create a virtual environment**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**

    ```sh
    pip install django mysqlclient
    ```


4. **Configure the database**

    Edit `myproject/settings.py` to configure your MySQL database settings under `DATABASES`.

5. **Apply migrations**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser**

    ```sh
    python manage.py createsuperuser
    ```

    Follow the prompts to create a superuser account.

7. **Run the development server**

    ```sh
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000/` in your web browser to see the application.

## Features

- User registration
- User login
- Profile update
- SMS functionalities
