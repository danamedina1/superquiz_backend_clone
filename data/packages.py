import mongoengine as mongoengine
import datetime as datetime

class MCQuestion(mongoengine.Document):
    created = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    num = mongoengine.IntField(required=True)
    question = mongoengine.StringField(required=True)
    answers = mongoengine.ListField(mongoengine.StringField())
    correct_answer = mongoengine.StringField(required=True)
    quote = mongoengine.StringField(required=True)
    article = mongoengine.StringField(required=False)
    maintainers = mongoengine.ListField(mongoengine.ObjectIdField())

    meta = {
        'db_alias': 'core',
        'collection': 'packages',
        'indexes': [
            'created',
            'name',
            'maintainers',
            #'total_downloads',
        ],
        'ordering': ['-created']
    }

