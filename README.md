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
