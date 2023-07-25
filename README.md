# -superquiz-v1-backend
The Superquiz Questions Generator for the https://blog.strive2thrive.earth/ website.
Makes usage of chatGPT to generate the questions.

Add openai_credentials.json file with the chatGPT credentials to the root folder in order to run the app.
the file should be in the following format:
{
  "account_handle": "<email address>",
  "password": "<passwod>",
  "api_key": "<the OpenAI key>"
}

## Installation:

**Mongo setup:**
1.	Install MongoDB on your PC 
2.	Create virtual environment (venv): file -> settings -> project -> Python Interpreter -> Add Interpreter -> Virtualenv Environment
	Now when opening the project it should be opened with (venv) prompt.
3.	Install MongoEngine: 
	pip install mongoengine
For more info:
https://youtu.be/rlvGCTE4MI0


**OpenAI setup:**
In the terminal window:
pip install openai

**BeautifulSoup Setup:**
In the terminal window:
pip install beautifulsoup4

or in PyCharm:
1.	Open File > Settings > Project from the PyCharm menu.
2.	Select your current project.
3.	Click the Python Interpreter tab within your project tab.
4.	Click the small + symbol to add a new library to the project.
5.	Now type in the library to be installed, in your example "bs4" without quotes, and click Install Package.
6.	Wait for the installation to terminate and close all popup windows.


# SuperQuiz App API - Requests
The SuperQuiz app API provides endpoints to generate, read, update, and delete Multiple Choice Questions (MCQs) through HTTP requests. 
This README will guide you on how to send requests to interact with the API.

## Base URL

Before you start sending requests, ensure that the SuperQuiz app server is up and running. The base URL for the API will be the server's address, which could be something like `http://localhost:5000/` if you are running it locally.

## Request Types

The SuperQuiz app API supports four types of HTTP requests:

1. **POST** - Used to generate MCQs based on a URL.
2. **GET** - Used to read (fetch) MCQs with specific criteria.
3. **PUT** - Used to update an existing MCQ.
4. **DELETE** - Used to delete an existing MCQ.

Please note that the request types and endpoints should be used as follows:

- To generate MCQs: Send a POST request to `/generate_mcq`.
- To read MCQs: Send a GET request to `/read`.
- To update an MCQ: Send a PUT request to `/update`.
- To delete an MCQ: Send a DELETE request to `/delete`.

## Endpoints and Parameters

### 1. Generate MCQs
**Endpoint:** `/generate_mcq`
**Request Method:** POST
**Parameters:**
- `url`: (required) The URL from which the MCQs will be generated.
- `number_of_questions`: (optional) The number of MCQs to generate (default is 10 if not provided).
**Sample Request:**
```http
POST /generate_mcq HTTP/1.1
Content-Type: application/json

{
    "url": "https://example.com/questions",
    "number_of_questions": 5
}
```

### 2. Read MCQs
**Endpoint:** `/read`
**Request Method:** GET
**Parameters:**
- `id`: (optional) The ID of the MCQ to fetch (if not provided, fetches all MCQs).
- `url`: (optional) Filter MCQs by URL.
- `tags[]`: (optional) Filter MCQs by tags. You can provide multiple tags as an array.
- `approved`: (optional) Filter MCQs by approved filed.
**Sample Request:**
```http
GET /read?id=123&tags[]=science&tags[]=biology HTTP/1.1
```

### 3. Update an MCQ
**Endpoint:** `/update`
**Request Method:** PUT
**Parameters:**
- `id`: (required) The ID of the MCQ to update.
- `updated_question`, `updated_answers[]`, `updated_correct_answer`, `updated_quote`, `updated_url`, `updated_tags[]`, `updated_date`, `updated_type`, `updated_approved`, `updated_approved_by`: (optional) The updated values for the corresponding fields.
**Sample Request:**

```http
PUT /update?id=123 HTTP/1.1
Content-Type: application/json

{
    "updated_question": "What is the capital of France?",
    "updated_answers": ["Paris", "London", "Berlin", "Rome"],
    "updated_correct_answer": "Paris"
}
```

### 4. Delete an MCQ
**Endpoint:** `/delete`
**Request Method:** DELETE
**Parameters:**
- `id`: (required) The ID of the MCQ to delete.
**Sample Request:**
```http
DELETE /delete?id=123 HTTP/1.1
```

## Response
The responses will be in JSON format and will vary based on the requested endpoint. For example, generating MCQs will return a JSON array of generated questions, while reading, updating, or deleting MCQs will return a status message.
## Status Codes
The API may return the following status codes:

- `200`: Successful request.
- `201`: Successful creation (for POST requests).
- `204`: Successful deletion (for DELETE requests).
- `400`: Bad request - incorrect or missing parameters.
- `404`: Not found - the requested resource does not exist.
- `500`: Internal server error - something went wrong on the server side.

## Conclusion

With this API documentation, you can now interact with the Superquiz app to generate, read, update, and delete MCQs using HTTP requests. 
Make sure to include the appropriate request type, endpoint, and parameters to perform the desired action successfully. Happy quizzing!
