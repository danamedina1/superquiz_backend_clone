from data.mcq_schema import MCQuestion
from data.mongo_setup import global_init, connect_db


#split the GPT output into a list of MCQs:
def gpt_output_to_mcq_list(gpt_output, url, tags, title):
    mcq_set = []

    paragraphs_list = gpt_output.strip('').split('Question')
    for paragraph in paragraphs_list:
        if paragraph == '':
            continue

        q = MCQuestion()
        try:
            q.name = f'{title} | Question - {paragraph.split(":")[0].strip(" ")}'
            #paragraph.split(':')[0].strip(' ')
            q.question = paragraph.split(':')[1].split('\n')[0].strip(' ')
            q.tags = tags
            q.answers = [paragraph.split('a. ')[1].split('b. ')[0].strip('\n'),
                         paragraph.split('b. ')[1].split('c. ')[0].strip('\n'),
                         paragraph.split('c. ')[1].split('d. ')[0].strip('\n'),
                         paragraph.split('d. ')[1].split('The correct answer is: ')[0].strip('\n')]
            q.correct_answer = paragraph.split('The correct answer is: ')[1].split('Quote that contains the answer: ')[0].strip('\n') if len(paragraph.split('The correct answer is: '))>1 else ''
            q.quote = paragraph.split('Quote that contains the answer: ')[1].strip('\n').strip('"').strip('\n') if len(paragraph.split('Quote that contains the answer: '))>1 else ''
            q.url = url
            q.no = increase_db_counter()
            mcq_set.append(q)
            q.save()

        except IndexError as e:
            print(e)
            print(paragraph)
            continue
    return mcq_set


#create a db_counter file if one doesn't exist, and increase the counter by 1
def increase_db_counter():
    try:
        with open('db_counter.txt', 'r') as file:
            counter = int(file.read())
    except:
        counter = 0
    counter += 1
    with open('db_counter.txt', 'w') as file:
        file.write(str(counter))
    return counter


#read the database with optional filters:
def read_db(id = None, no = None, url = None, tags = None):
    connect_db()#connect to the database

    if(id == None and no == None):#if no id or no is specified, then filter by url and tags
        if url == None and tags == None:#if no url or tags are specified, then return all
            results = MCQuestion.objects()
        elif url == None:#if no url is specified, then filter by tags
            results = MCQuestion.objects(tags__all=tags)
        elif tags == None:#if no tags are specified, then filter by url
            results = MCQuestion.objects(url = url)
        else:#if both url and tags are specified, then filter by both
            results = MCQuestion.objects(url = url, tags__all=tags)
    else:#if id or no is specified, then filter by id or no
        if id != None:#if id is specified, then filter by id
            results = MCQuestion.objects(id=id)
        else:#if no is specified, then filter by no
            results = MCQuestion.objects(no=no)
        # print the results:

    return results

#update an mcq document in the database:
def update_db(id = None, no = None, updated_mcq = None):
    connect_db()    #connect to the database

    if(id != None):#if id is specified, then filter by id and update the mcq document
        result =  MCQuestion.objects(id=id).update(**updated_mcq)
        return result, "Question id {id} updated in the database." if result else "Question id {id} not found in the database."
    elif(no != None):#if no is specified, then filter by no and update the mcq document
        result = MCQuestion.objects(no=no).update(**updated_mcq)
        return result, "Question no. {no} updated in the database." if result else "Question no. {no} not found in the database."
    else:#if neither id nor no is specified, return a message
        return -1, "Please specify either an id or a question number to update a question in the database."


#delete a document from the database, select by id or number:
def delete_db(id = None, no = None):
    connect_db()#connect to the database

    if(id != None):#if id is specified, then filter by id and delete the document
        result = MCQuestion.objects(id=id).delete()
        return result, f"Question id {id} deleted from the database." if result else f"Question id {id} not found in the database."
    elif(no != None):#if no is specified, then filter by no and delete the document
        result = MCQuestion.objects(no=no).delete()
        #print(f"Question no. {no} deleted from the database.") if result else print(f"Question no. {no} not found in the database.")
        return result, f"Question no. {no} deleted from the database." if result else f"Question no. {no} not found in the database."
    else:#if neither id nor no is specified, return a message
        return -1, "Please specify either an id or a question number to delete a question from the database."
