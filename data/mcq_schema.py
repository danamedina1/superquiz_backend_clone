import mongoengine as mongoengine
import datetime as datetime


#superquiz question types:
class QuestionType:
    ACCEPTANCE = "ACCEPTANCE"
    CHECKBOX = "CHECKBOX"
    CHECKGRID = "CHECKGRID"
    CHOICE = "CHOICE"
    DATE = "DATE"
    GRID = "GRID"
    IMAGE1 = "IMAGE1"
    IMAGE2 = "IMAGE2"
    LIST = "LIST"
    PAGE = "PAGE"
    PARAGRAPH = "PARAGRAPH"
    SCALE = "SCALE"
    SECTION = "SECTION"
    TEXT = "TEXT"
    TIME = "TIME"
    VIDEO = "VIDEO"


class MCQuestion(mongoengine.Document):

    name = mongoengine.StringField(required=True)
    no = mongoengine.IntField(required=True)
    date = mongoengine.DateTimeField(default=datetime.datetime.now)
    type = mongoengine.StringField(default=QuestionType.CHOICE)
    tags = mongoengine.ListField(required=True)
    question = mongoengine.StringField(required=True)
    answers = mongoengine.ListField(mongoengine.StringField())
    correct_answer = mongoengine.StringField(required=True)
    quote = mongoengine.StringField(required=True)
    url = mongoengine.StringField(required=False)

    meta = {
        'db_alias': 'core',
        'collection': 'packages',
        'indexes': [
            'name',
            'no',
            'date',
            'type',
            'tags',
            'question',
            'answers',
            'correct_answer',
            'quote',
            'url',
        ],
        'ordering': ['-created']
    }

    #printable version of the MCQuestion object:
    def __str__(self):
        printable_mcq = '\n\nMCQuestion:\n'
        printable_mcq += f'id: \t\t\t{str(self.id)}\n'
        printable_mcq += f'name: \t\t\t{self.name}\n'
        printable_mcq += f'no: \t\t\t{self.no}\n'
        printable_mcq += f'date: \t\t\t{self.date}\n'
        printable_mcq += f'type: \t\t\t{self.type}\n'
        printable_mcq += f'tags: \t\t\t{self.tags}\n'
        printable_mcq += f'question: \t\t{self.question}\n'
        printable_mcq += f'answers: \t\t{self.answers}\n'
        printable_mcq += f'correct_answer: {self.correct_answer}\n'
        printable_mcq += f'quote: \t\t\t{self.quote}\n'
        printable_mcq += f'url: \t\t\t{self.url}\n'

        return printable_mcq

    #convert the MCQuestion object to a dictionary:
    def to_dict(self):
        mcq_dict = {}
        mcq_dict['id'] = str(self.id)
        mcq_dict['name'] = self.name
        mcq_dict['no'] = self.no
        mcq_dict['date'] = self.date
        mcq_dict['type'] = self.type
        mcq_dict['tags'] = self.tags
        mcq_dict['question'] = self.question
        mcq_dict['answers'] = self.answers
        mcq_dict['correct_answer'] = self.correct_answer
        mcq_dict['quote'] = self.quote
        mcq_dict['url'] = self.url

        return mcq_dict
