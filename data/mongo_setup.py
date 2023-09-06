import mongoengine
import os

#global vars for mongo db:
db_name = ''
user = ''
password = ''
cluster = ''

#load the environment variables of mongo db:
def load_mongo_vars():
    global db_name, user, password, cluster
    if 'VERCEL' in os.environ:
        db_name = os.environ['MONGO_DB_NAME']
        user = os.environ['MONGO_USER']
        password = os.environ['MONGO_PASSWORD']
        cluster = os.environ['MONGO_CLUSTER']
    else:
        #read from .env file when running locally:
        with open('.env', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('MONGO_DB_NAME'):
                    db_name = line.split('=')[1].strip('\n')
                if line.startswith('MONGO_USER'):
                    user = line.split('=')[1].strip('\n')
                if line.startswith('MONGO_PASSWORD'):
                    password = line.split('=')[1].strip('\n')
                if line.startswith('MONGO_CLUSTER'):
                    cluster = line.split('=')[1].strip('\n')

#initialize the database
def global_init():
    global db_name, user, password, cluster
    load_mongo_vars()
    mongoengine.register_connection(alias='core', name=db_name)


#connect to the database
def connect_db():
    global db_name, user, password, cluster
    load_mongo_vars()
    #when running locally:
    # mongoengine.connect(db='mongoengine_superquizDB', alias='core')

    atlas_connection_url = f'mongodb+srv://{user}:{password}@{cluster}/{db_name}?retryWrites=true&w=majority'
    # Connect using the provided Atlas connection URL
    mongoengine.connect(host=atlas_connection_url, alias='core')


# # Call global_init to register the connection only once!
# global_init(db_name='deployed_sq_db')
#
# # Call connect_db to connect to the database
# connect_db()