# Segment Generator

## Requirements
- Python 3.x
- pip

## Getting Started
### Install Dependencies

Run the following command to install the required Python packages:

__pip install -r requirements.txt__

### Run Migrations

Run the following command to create the SQLite database and based on the defined schema in the Django models, including populating the initial data defined in migrations:

__python manage.py migrate__

### Run the Development Server

Run the following command to start the Django server:

__python manage.py runserver__

The application will be available at:

http://127.0.0.1:8000/

## API Documentation

### Get Nodes

Method: GET

Endpoint:

/api/canvas/

Description:

Endpoint that returns the full canvas data (nodes, ports, values, and connections)

Example Request:

GET http://127.0.0.1:8000/api/canvas/

### Get Segments

Method: GET

Endpoint:

/api/segments/

Description:

Replace this with your own description of the endpoint.

Example Request:

GET http://127.0.0.1:8000/api/segments/