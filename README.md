As Per the Requirements.

# Project Name: Client & Project Management System

## Description
This project is built using Django and Django REST Framework. It allows users to manage clients and assign projects to clients. Each project can have multiple users assigned to it. 

The application is designed with MySQL as the database backend, and all functionality, such as creating clients, assigning projects, and viewing projects, is done via APIs.

## Getting Started

### Prerequisites

Before starting, make sure you have the following installed:

- **Python 3.x**
- **MySQL**
- **Git**

### Installation Steps

#### 1. Clone the Repository

First, clone the repository using Git.

```bash
git clone https://github.com/Akshay-Patil-005/Nimap_task.git
cd Nimap_task
2. Set Up a Virtual Environment
Create and activate a virtual environment to isolate the project dependencies.

For Windows:

python -m venv venv
venv\Scripts\activate

3. Install Dependencies
Install the required packages listed in requirements.txt.

pip install -r requirements.txt

4. Database Setup
Ensure MySQL is installed and running. Afterward, follow these steps:

Create a MySQL Database:

Log in to MySQL and create a database.

CREATE DATABASE nimap_db;

Update the DATABASES settings in the settings.py file to match your MySQL credentials:

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nimap_db',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Apply Migrations:

Run the following commands to apply migrations and create the necessary database tables:

python manage.py makemigrations
python manage.py migrate

5. Create a Superuser
To access the Django admin panel and manage clients and projects, create a superuser account:


python manage.py createsuperuser

6. Run the Application
Start the Django development server with the following command:

python manage.py runserver
The application should now be running at http://127.0.0.1:8000/.

# Commented code for various databases such as Sqlite and Plsql. Default database used Mysql

![nimap_1](https://github.com/user-attachments/assets/eb81f776-7569-4e64-8639-0bba7ee26936)
![nimap_2](https://github.com/user-attachments/assets/eb03d8c9-85eb-41fa-b6ef-3fe2c0aaceb7)
![nimap_3](https://github.com/user-attachments/assets/61ea662b-8040-4df3-9921-360c19cdfefc)
![nimap_4](https://github.com/user-attachments/assets/8b92fc38-79f5-465d-af18-4b2163c2de48)
![nimap_json_format](https://github.com/user-attachments/assets/2e72495a-c077-4625-a686-7687fa266be2)
