import openai
import web_page
import json

KEY_FILE = "THRIVE_key.txt"
OPENAI_API_KEY= ""
MODEL = "gpt-3.5-turbo"


message_history = {}

def create_superquiz_questions(url, number_of_questions = 10):
    chatGPT_set_key()
    web_text, tags, title = web_page.get_web_article(url)
    tags_string = ""#all tags in one string
    tags_string += ", ".join(tags)
    request = f'create {number_of_questions} multiple-choice questions with 1 correct answer and 3 incorrect answers each, ' \
              f'based on this text:   {web_text}. ' \
              # f'/nTags of this article: {tags_string}'
    answer = chatGPT_request(request)
    return answer, tags, title


def load_openAI_credentials():
    # Load the credentials from the JSON file
    with open('openai_credentials.json') as file:
        credentials = json.load(file)

    # Access the account handle, password, and API key
    account_handle = credentials['account_handle']
    password = credentials['password']
    api_key = credentials['api_key']
    return api_key



#read KEY_FILE and return the key
def chatGPT_read_key():
    global OPENAI_API_KEY
    with open(KEY_FILE, "r") as file:
        OPENAI_API_KEY = file.read().strip('\n')
    return OPENAI_API_KEY

#submit the key for the chatGPT API
def chatGPT_set_key():
    # chatGPT_read_key()
    global OPENAI_API_KEY
    OPENAI_API_KEY = load_openAI_credentials()
    openai.api_key = OPENAI_API_KEY
    return openai.api_key

#set the system content with the relevant requirments for a multiple-choice question base on a web article
def chatGPT_set_system_content():

    system_content = "return as a response multiple-choice questions. " \
                     "Within the tags of this article, choose only the relevant tags for this question. Always include tags that starts with SDG " \
                     "The questions should be presented in the following format:" \
                     "Question <question number>: <question> " \
                     "a. <answer> " \
                     "b. <answer> " \
                     "c. <answer> " \
                     "d. <answer> " \
                     "The correct answer is: <correct answer> " \
                     "Quote that contains the answer: <quote> " \
                     # "Tags: <relevant_tags> " \

    return system_content

def chatGPT_request(text):
    system_content = chatGPT_set_system_content()

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{'role':'user','content':text},
                  {'role':'system','content':system_content}
                  ])
    print(response)
    response_content = response['choices'][0].message.content

    #message_history.append({}
    return response_content




