# YouOwe.me - Django Web Application

YouOwe.me is a Django-based web application that allows you to track how much your friends owe you, all in a fun and humorous way with memes (in Portuguese). 

## Features
- Track debts with friends in a lighthearted manner
- Display funny memes related to owing money (in Portuguese)
- Built with Python, Django, and a database for storing information

## Prerequisites
Before you begin, make sure you have the following installed on your system:
- Python 3.x
- Django 3.x or above
- pip (Python package manager)
- Git

## Cloning the Repository

1. **Clone the Repository**  
   Open your terminal or command prompt and run the following command to clone the repository:
   ```bash
   git clone https://github.com/your-username/YouOwe.me.git


2. **Navigate to the Project Directory**
   After cloning the repository, navigate into the project folder:
   ```bash
   cd YouOwe.me

3. **Create a Virtual Enviroment**
   It is a good practice to create a virtual enviroment to isolate your dependencies:
   ```bash
   python3 -m venv env

4. **Activate the virtual enviroment**
   On Windows:
   ```bash
   .env\Scripts\activate

   On Mac/Linux:
   ```bash
   source env/bin/activate

5. **Apply Database Migrations**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate

6. **Create a Superuser** (optional)
   ```bash
   python3 manage.py createsuperuser

7. **Running the Application**
   You can now start the Django Development Server:
   ```bash
   python3 manage.py runserver

8. **Access the Application**
   Open your browser and go to:
   ```cpp
   http://127.0.0.1:8000/

**Contributing**
Feel free to fork this repository and submit pull requests to improve the application.

**Accesing the Application Already on the Web**
https://youoweme.pythonanywhere.com
   
     
