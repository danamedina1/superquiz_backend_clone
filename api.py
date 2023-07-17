import data.mongo_setup as mongo_setup
import chatgpt_api
import mongo_api

#create a new set of questions for a given url and store it in the DB:
def generate_mcq_list(url, number_of_questions = 10):
    answer, tags, title = chatgpt_api.create_superquiz_questions(url, number_of_questions)
    mongo_setup.connect_db()
    mcq_list =  mongo_api.gpt_output_to_mcq_list(answer, url, tags, title)
    [print(mcq) for mcq in mcq_list]
    return mcq_list



#read the database with optional filters: id, url, tags. returns a list of MCQuestions
def read(id = None, url = None, tags = None):
    mcq_list = list(mongo_api.read_db(id, url, tags))
    [print(mcq) for mcq in mcq_list]
    return mcq_list


#update an mcq document in the db with optional fields.
def update(id = None, updated_mcq=None, updated_question=None, updated_answers=None, updated_correct_answer=None, updated_quote=None, updated_url=None, updated_tags=None, updated_date=None, updated_type=None):
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

    #update the mcq in the database:
    result, msg = mongo_api.update_db(id, updated_mcq)
    print(msg)
    return result

#delete an mcq document from the db, selected by id or number.
#If no id or number are provided, the function will return without deleting anything.
def delete(id = None):
    result, msg =  mongo_api.delete_db(id = id)
    print(msg)
    return result