import mongoengine



#initialize the database
def global_init(db_name: str):
    mongoengine.register_connection(alias='core', name=db_name)

#connect to the database
def connect_db():
    mongoengine.connect(db='mongoengine_superquizDB', alias='core')


