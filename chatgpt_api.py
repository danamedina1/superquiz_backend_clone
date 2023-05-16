#connect to chatGPT API
import openai
import web_page

KEY_FILE = "key.txt"
OPENAI_API_KEY= ""
MODEL = "gpt-3.5-turbo"
#url = "https://blog.strive2thrive.earth/the-importance-of-forests-for-human-well-being/"
url = "https://blog.strive2thrive.earth/violent-imagery-the-mental-health-implications/"

message_history = {}

def create_superquiz_questions():
    chatGPT_set_key()
    web_text = web_page.get_web_article(url)
    answer = chatGPT_request("create 10 multiple-choice questions, based on this text: "+web_text)
    return answer

def chatGPT_get_key():
    global OPENAI_API_KEY
    OPENAI_API_KEY = open(KEY_FILE, "r").read().strip('\n')
    return OPENAI_API_KEY

def chatGPT_set_key():
    chatGPT_get_key()
    openai.api_key = OPENAI_API_KEY
    return openai.api_key

#set the system content with the relevant requirments for a multiple-choice question base on a web article
def chatGPT_set_system_content(url):

    system_content = "return as a response multiple-choice questions with 1 correct answer and 3 incorrect answers each. " \
                     "Provide the correct answer at the end of each question." \
                     "Provide the sentance/sentances from the article that contains the answer . " \
                     "Keep the questions and answers short, not more than 12 words each. "
                     # "Don't include numbers, percentages and statistics in the questions and answers." \



    return system_content

def chatGPT_request(text):
    system_content = chatGPT_set_system_content(url)

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{'role':'user','content':text},
                  {'role':'system','content':system_content}
                  ])
    print(response)
    response_content = response['choices'][0].message.content

    #message_history.append({}
    return response_content


