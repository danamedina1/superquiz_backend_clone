import superquiz_app



if __name__ == '__main__':
    url = "https://blog.strive2thrive.earth/violent-imagery-the-mental-health-implications/"
    #url = "https://blog.strive2thrive.earth/the-importance-of-forests-for-human-well-being/"

    #create a new set of questions for a given url and store it in the DB:
    # mcq_list = superquiz_app.generate_mcq_list(url)
    #
    # first_id = mcq_list[0].id
    #  # mcq_dict = mcq_list[0].to_dict()
    # second_id = mcq_list[1].id
    # third_id = mcq_list[2].id
    #
    # #read db:
    mcq_list = superquiz_app.read(tags = ["SDG3"])
    # mcq_list = superquiz_app.read(id = first_id)
    #
    # # first_id = mcq_list[0].id
    # # mcq_dict = mcq_list[0].to_dict()
    # # second_id = mcq_list[1].id
    # # third_id = '64b55416e3b9d88faea73e3e'
    #
    # #delete a document from the db:
    # superquiz_app.delete(id = first_id)#delete the first document
    #
    # #update a document in the db:
    # superquiz_app.update(id = third_id,updated_question= 'What is the primary ingredient in chocolate?')
    # superquiz_app.update(id = third_id, updated_tags=['SDG12', 'SDG15'])
    # superquiz_app.update(id = third_id,updated_correct_answer= 'c. Cocoa beans')
    # superquiz_app.update(id = third_id,updated_approved= 'True')

