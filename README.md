# Client & Appointment Dashboard

A simple Django-based dashboard to manage clients. It uses Bootstrap for styling and jQuery for AJAX operations.

## Features

- Add and view clients
- Add appointments for individual clients
- Search and paginate client table
- AJAX-based form submissions
- Bootstrap modal for adding data

## How to Run

1. **Clone the project**
   ```bash
   git clone https://github.com/your-username/client-dashboard.git
   cd client-dashboard

## Create and Activate Virtual Environment  
python -m venv venv
venv\Scripts\activate


## Install dependencies
pip install -r requirements.txt

## Apply migrations
python manage.py migrate

## Run the server
python manage.py runserver