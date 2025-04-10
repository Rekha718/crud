# CRUD Project

This is a simple Django-based CRUD web application. This project allows users to create, read, update, and delete user records with their details.

## 🗂️ Folder Structure

CRUD/
├── crud_app/
│   ├── crud_app/
│   ├── myapp/
│   ├── templates/
│   ├── static/
│   ├── manage.py
├── myvenv/

## 🚀 Steps to Run the Project

### 1. **Clone the repository**:
First, clone this repository to your local machine:

```bash
git clone <your_repo_link>
cd CRUD/crud_app

2. Create and activate a virtual environment (Optional but recommended):
On Windows:

python -m venv venv
venv\Scripts\activate

3. Install required dependencies:
Once the virtual environment is activated, install the required packages using requirements.txt:

pip install -r requirements.txt

4. Run database migrations:
This step sets up the database by applying migrations:

python manage.py makemigrations
python manage.py migrate

5. Start the server:
Now that everything is set up, start the Django development server:

python manage.py runserver

6. Access the project in your browser:
Open your browser and go to:

http://127.0.0.1:8000/


Note: MySQL should be installed, and the database should be created. You can create the database using the following command:

CREATE DATABASE user_registration_db;
