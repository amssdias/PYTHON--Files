question = open('questions.txt', 'r')
question_content = [question.strip().split("=") for question in question.readlines()]
question.close()

print(question_content)

question_content = {
    question[0]:question[1]
    for question in question_content
}

print(question_content)