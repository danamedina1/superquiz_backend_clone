
import chatgpt_api

#read URL text:
import requests

if __name__ == '__main__':

    answer = chatgpt_api.create_superquiz_questions()
    print(answer)

