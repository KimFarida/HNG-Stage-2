#STAGE 2 CRUD API DOCUMENTATION

This documentation provides information on how to use the Person API for CRUD (Create, Read, Update, Delete) operations on person records.

## Endpoints

### Create a New Person
- **Endpoint:** `/api`
- **HTTP Method:** POST
- **Request Format:**
  ```json
  {
    "name": "Mark Essien",
    "age": 30,
    "address": "HNG, Nigeria"
  }
  ```
- #### Response Format
    - Sucess(HTTP 201)
    ```json
    {
        "message": "New person created successfully"
    }
    ```
    - Error(HTTP 400 or 500)
    ```json
    {
        "error": "Something went wrong while updating the person"
    }
    ```
### Fetch Details of a Person
- **Endpoint:** `/api/<identifier>`
    - You can provide the person's name or ID as the `<identifier>` in the url
- **HTTP Method:** GET
- **Response Format:**
    - Success(HTTP 200):
     ```json
    {
        "name": "Mark Essien",
        "age": 30,
        "address": "HNG, Nigeria"
    }
    ```
    - Error(HTTP 400 or 500)
    ```json
    {
        "error": "Person not found"
    }
    ```

### Update Details of a Person
- **Endpoint:** `/api/<identifier>`
    - You can provide the person's name or ID as the `<identifier>` in the url
- **HTTP Method:** PUT
- **Request Format:**
    ```json
    {
        "name": "Updated Name",
        "age": 35,
        "address": "Zuri, Africa"
    }
    ```
- **Response Format:**
    - Success(HTTP 200):
     ```json
     {
        "message": "Person updated successfully"
    }
    ```
    - Error(HTTP 400 or 500)
    ```json
    {
        "error": "Error message"
    }

    ```
### Delete a Person
- **Endpoint:** /api/<identifier>
    - You can provide either the person's name or ID as the <identifier> in the URL.
- **HTTP Method:** DELETE
- **Response Format:**
    - Success (HTTP 200):
    ```json
    {
        "message": "Person deleted successfully"
    }

    ```
    - Error(HTTP 400 or 500)
    ```json
    {
        "error": "Person not found"
    }

### Fetch All Persons
- **Endpoint:** /api/persons
- **HTTP METHOD:** GET
- **Response Format:**
    - Success (HTTP 200):
    ```json
        [
    {
        "id": 1,
        "name": "Mark Essien",
        "age": 30,
        "address": "20 Admiralty St"
    },
    {
        "id": 2,
        "name": "Seyi Onifade",
        "age": 25,
        "address": "89 Babajide St"
    }
    // ... (more persons)
    ]

    ```
### Sample Usage
- **Create a New Person (POST):**
```
    curl -X POST -H "Content-Type: application/json" -d '{
    "name": "Mark Essien",
    "age": 30,
    "address": "20 Admiralty St"
    }' https://kimfarida1.eu.pythonanywhere.com/api
```
- **Fetch Details of a Person (GET):**
```
    curl -X PUT -H "Content-Type: application/json" -d '{
  "id": 1,
  "name": "Mark Essien",
  "age": 30,
  "address": "20 Admiralty St"
}' https://kimfarida1.eu.pythonanywhere.com/api/1
```

- **Update Details of a Person (PUT)::**
```
    curl -X PUT -H "Content-Type: application/json" -d '{
    "name": "Updated Name",
    "age": 35,
    "address": "456 Elm St"
    }' https://kimfarida1.eu.pythonanywhere.com/api/1
```

- **Delete a Person (DELETE):**
```
   curl -X DELETE https://kimfarida1.eu.pythonanywhere.com/api/1
```

## Swagger UI Documentation

You can also interact with this API using Swagger UI, which provides a user-friendly interface for exploring and testing the API endpoints.

### Access Swagger UI

To access Swagger UI and interact with the API, follow these steps:

*  Open a web browser and navigate to the Swagger UI URL. By default, it should be available at: `https://kimfarida1.eu.pythonanywhere.com/apidocs/`

* You will be presented with the Swagger UI interface, which allows you to explore the API endpoints, make requests, and view responses interactively.

### Sample Usage in Swagger UI

Here are sample API interactions you can perform in Swagger UI:

- **Create a New Person (POST):** Use Swagger UI to create a new person by providing the required data in the request body.

- **Fetch Details of a Person (GET):** Use Swagger UI to retrieve details of a person by specifying their name or ID.

- **Update Details of a Person (PUT):** Update a person's information using Swagger UI by providing the updated data in the request body.

- **Delete a Person (DELETE):** Delete a person record using Swagger UI by specifying their name or ID.

### Limitations and Assumptions
- Names are assumed to be unique.
- Age must be a positive integer.
- Address must be a string.
- No query parameters are supported for filtering.
- Data validation is minimal in this example.

### Setup and Deployment
Setting up and deploying the API on PythonAnywhere has already been taken care of. You don't need to perform these steps again because your application is live on https://kimfarida1.eu.pythonanywhere.com.

However, if you want to understand how the deployment process works or if you're working on a development environment, you can follow these steps:

* Clone the repository
* Install the required dependencies 
* Configure the database URI 
* Create the database tables by running: `flask create_tables`
* Run the Flask application: `flask run`

Now, you can test the API by making requests to `http://localhost:5000/api` or `http://localhost:5000/api/<identifier>` in your local environment.

For more detailed instructions, refer to the project's README or documentation.

This concludes the documentation for the Person API. If you have any questions or need further assistance, please reach out to me.
