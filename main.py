
import data.mongo_setup as mongo_setup
import chatgpt_api
import mongo_questions_set



if __name__ == '__main__':
    url = "https://blog.strive2thrive.earth/the-importance-of-forests-for-human-well-being/"
    #url = "https://blog.strive2thrive.earth/violent-imagery-the-mental-health-implications/"

    answer = chatgpt_api.create_superquiz_questions(url)
    # answer = "Question 1: What are some of the mental health impacts of witnessing violent images in the media?\n" \
    #          "a. Increased empathy and compassion\n" \
    #          "b. Decreased rates of PTSD\n" \
    #          "c. Altered mental conditions and emotional distress\n" \
    #          "d. Improved overall mental well-being\n" \
    #         "\n"\
    #         "The correct answer is: c. Altered mental conditions and emotional distress\n" \
    #         "Quote that contains the answer: \"Studies have shown that children exposed to political violence experience emotional distress. This exposure can also alter the mental conditions of the child.\" \n" \
    #         "\n"    \
    #         "Question 2: What are the media's responsibilities regarding the presence of violent imagery in their content?\n" \
    #         "a. To glorify and promote violence\n" \
    #         "b. To ensure violence is depicted accurately\n" \
    #         "c. To remove violent imagery for the well-being of their audience\n" \
    #         "d. To incite violence against certain groups\n" \
    #         "\n"\
    #         "The correct answer is: c. To remove violent imagery for the well-being of their audience\n" \
    #         "Quote that contains the answer: \"It is the duty of social media giants to prevent violent content from being distributed. Penalties need to exist for individual accounts that distribute violent material.\" \n" \
    #         "\n"\
    #         "Question 3: What is the term used to describe the labeling of certain groups or individuals as different or evil in order to justify violence towards them?\n" \
    #         "a. Othering\n" \
    #         "b. Altruism\n" \
    #         "c. Empathy\n" \
    #         "d. Collaboration\n" \
    #         "\n"\
    #         "The correct answer is: a. Othering\n" \
    #         "Quote that contains the answer: \"Othering is a way of labelling certain groups or individuals as different or evil... This difference is then instrumentalised to produce violence towards that group and justify that violence as acceptable.\"\n" \
    #         "\n"\
    #         "Question 4: How do social media algorithms contribute to the exposure of violent videos?\n" \
    #         "a. They prioritize non-violent content\n" \
    #         "b. They limit the distribution of violent posts\n" \
    #         "c. They show more violent posts to people who seek out such content\n" \
    #         "d. They prevent violent content from being posted\n" \
    #         "\n"\
    #         "The correct answer is: c. They show more violent posts to people who seek out such content\n" \
    #         "Quote that contains the answer: \"Naturally, social media algorithms provide greater exposure to violent videos. Algorithms show more violent posts to people who already seek out such content.\"\n" \
    #         "\n"\
    #         "Question 5: What is the responsibility of social media giants regarding the distribution of violent content?\n" \
    #         "a. To promote violent material\n" \
    #         "b. To allow hate-filled glorification of violence\n" \
    #         "c. To prevent the distribution of violent material\n" \
    #         "d. To increase the distribution of violent content\n" \
    #         "\n" \
    #         "The correct answer is: c. To prevent the distribution of violent material\n" \
    #         "Quote that contains the answer: \"It is the duty of social media giants to prevent violent content from being distributed.\"\n" \
    #         "\n"
    print(answer)
    mongo_setup.connect_db()
    mongo_questions_set.gpt_output_to_mcq_set(answer, url)
