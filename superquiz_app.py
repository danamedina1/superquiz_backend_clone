import data.mongo_setup as mongo_setup
import chatgpt_api
import mongo_api
# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
# @app.route('/generate_mcq', methods=['POST'])
#create a new set of questions for a given url and store it in the DB:
def generate_mcq_list(url, number_of_questions = 10):
    answer, tags, title = chatgpt_api.create_superquiz_questions(url, number_of_questions)
    mongo_setup.connect_db()
    mcq_list =  mongo_api.gpt_output_to_mcq_list(answer, url, tags, title)
    [print(mcq) for mcq in mcq_list]
    return mcq_list


#parse 'True' and 'False' strings to boolean:
def parse_bool(string):
    if string == 'True' or string == 'true' or string == '1' or string == 1 or string == True or string == 'TRUE':
        return True
    elif string == 'False' or string == 'false' or string == '0' or string == 0 or string == False or string == 'FALSE':
        return False
    else:
        return None

#read the database with optional filters: id, url, tags, approved. returns a list of MCQuestions
def read(id = None, url = None, tags = None, approved = None):
    approved = parse_bool(approved)
    result = mongo_api.read_db(id, url, tags, approved)
    mcq_list = list(result)
    [print(mcq) for mcq in mcq_list]

    if len(mcq_list) == 0:
        return None
    return mcq_list


#update an mcq document in the db with optional fields.
def update(id = None, updated_mcq=None, updated_question=None, updated_answers=None,
           updated_correct_answer=None, updated_quote=None, updated_url=None,
           updated_tags=None, updated_date=None, updated_type=None,
           updated_approved=None, updated_approved_by=None):
    if(updated_mcq == None):
        updated_mcq = {}#create an empty mcq to store the updated fields

        #add the updated fields to the mcq:
        if(updated_question != None):
            updated_mcq['question'] = updated_question
        if(updated_answers != None):
            updated_mcq['answers'] = updated_answers
        if(updated_correct_answer != None):
            updated_mcq['correct_answer'] = updated_correct_answer
        if(updated_quote != None):
            updated_mcq['quote'] = updated_quote
        if(updated_url != None):
            updated_mcq['url'] = updated_url
        if(updated_tags != None):
            updated_mcq['tags'] = updated_tags
        if(updated_date != None):
            updated_mcq['date'] = updated_date
        if(updated_type != None):
            updated_mcq['type'] = updated_type
        if(updated_approved != None):
            updated_mcq['approved'] = parse_bool(updated_approved)
        if(updated_approved_by != None):
            updated_mcq['approved_by'] = updated_approved_by

    #update the mcq in the database:
    result, msg = mongo_api.update_db(id, updated_mcq)
    print(msg)
    return result, msg

#delete an mcq document from the db, selected by id or number.
#If no id or number are provided, the function will return without deleting anything.
def delete(id = None):
    result, msg =  mongo_api.delete_db(id = id)
    print(msg)
    return result, msg