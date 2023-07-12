import api



if __name__ == '__main__':
    #url = "https://blog.strive2thrive.earth/violent-imagery-the-mental-health-implications/"
    url = "https://blog.strive2thrive.earth/the-importance-of-forests-for-human-well-being/"

    #create a new set of questions for a given url and store it in the DB:
    mcq_list = api.generate_mcq_list(url)

    first_id = mcq_list[0].id
    first_no = mcq_list[0].no

    second_id = mcq_list[1].id
    second_no = mcq_list[1].no

    third_id = mcq_list[2].id
    third_no = mcq_list[2].no

    #read db:
    mcq_list = api.read(tags = ["SDG3"])
    mcq_list = api.read(id = first_id)
    mcq_list = api.read(no=first_no)


    #delete a document from the db:
    api.delete(id = first_id)#delete the first document
    api.delete(no = second_no)#delete the second document
    api.delete()#delete nothing

    #update a document in the db:
    api.update(id = third_id,updated_question= 'What is the primary ingredient in chocolate?')
    api.update(id=third_id, updated_answers=['Unicorn tears', 'Fairy dust', 'Cocoa beans', 'Stardust'])
    api.update(id = third_id,updated_correct_answer= 'c. Cocoa beans')