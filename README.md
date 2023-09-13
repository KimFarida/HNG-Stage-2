# HNG STAGE 2 CRUD API

Welcome to the HNG STAGE 2 CRUD API project! This API allows you to perform CRUD (Create, Read, Update, Delete) operations on person records.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Swagger UI](#swagger-ui)
- [Sample Usage](#sample-usage)
- [Limitations and Assumptions](#limitations-and-assumptions)


## Project UML Diagram

![UML Diagram](UML%20Diagram.png)


## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed.
- [Pip](https://pip.pypa.io/en/stable/) installed.
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) installed (optional but recommended).

### Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/KimFarida/HNG-Stage-2
```
2. Create a virtual environment (optional but recommended):
```
cd HNG-Stage-2/
```
3. Activate the virtual environment (if created):
  * On Windows:
  ```
  venv\Scripts\activate
  ```
  * On macOS and Linux:
  ```
  source venv/bin/activate
  ```
4. Install the project dependencies:
```
pip install -r requirements.txt
```
### Running the Application
To run the Flask application, use the following command:
```
flask run
```

The API should now be accessible at `http://localhost:5000.`

### API Endpoints
The API provides the following endpoints:

* Create a New Person (`POST /api`)
* Fetch Details of a Person (`GET /api/<identifier>`)
* Update Details of a Person (`PUT /api/<identifier>`)
* Delete a Person (`DELETE /api/<identifier>`)

For detailed information on each endpoint, please refer to the [API Documentation](https://github.com/KimFarida/HNG-Stage-2/blob/main/DOCUMENTATION.md).

### Swagger UI
You can also interact with this API using Swagger UI, which provides a user-friendly interface for exploring and testing the API endpoints. To access Swagger UI, follow the Swagger UI Documentation.

### Sample Usage
Sample API interactions and usage examples are provided in the [API Documentation](https://github.com/KimFarida/HNG-Stage-2/blob/main/DOCUMENTATION.md).

### Limitations and Assumptions
* Names are assumed to be unique.
* Data validation is minimal in this example.



Feel free to customize this template to fit your project's specific needs and add any additional information or sections that are relevant to your project.

