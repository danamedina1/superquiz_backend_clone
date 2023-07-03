from data.packages import MCQuestion
from data.mongo_setup import global_init
from mongoengine import connect

# if __name__ == '__main__':
#     #global_init('mongoengine_superquizDB')
#     connect(db='mongoengine_superquizDB', alias='core')
#
#     q = MCQuestion()
#     q.name = 'What is the impact of violent images on mental health?'
#     q.answers = ['Minimal impact', 'Negative impact', 'Minimal impact', 'No impact']
#     q.correct_answer = 'a'
#     q.article = 'https://www.bbc.com/news/health-47934692'
#     q.save()

#split the GPT output into a list of MCQs:
def gpt_output_to_mcq_set(gpt_output, url):
    mcq_set = []

    paragraphs_list = gpt_output.strip('').split('Question')
    for paragraph in paragraphs_list:
        if paragraph == '':
            continue
        q = MCQuestion()
        q.name = url + " Question "+paragraph.split('a. ')[0].strip(' ').strip('\n')
        q.num = paragraph.split(':')[0].strip(' ')
        q.question = paragraph.split(':')[1].split('\n')[0].strip(' ')
        q.answers = [paragraph.split('a. ')[1].split('b. ')[0].strip('\n'),
                     paragraph.split('b. ')[1].split('c. ')[0].strip('\n'),
                     paragraph.split('c. ')[1].split('d. ')[0].strip('\n'),
                     paragraph.split('d. ')[1].split('The correct answer is: ')[0].strip('\n')]
        q.correct_answer = paragraph.split('The correct answer is: ')[1].split('Quote that contains the answer: ')[0].strip('\n')
        q.quote = paragraph.split('Quote that contains the answer: ')[1].strip('\n')
        q.article = url
        mcq_set.append(q)
        q.save()

    return mcq_set