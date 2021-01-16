question = open('questions.txt', 'r')
question_content = [question.strip().split("=") for question in question.readlines()]
question.close()

question_content = {
    question[0]:question[1]
    for question in question_content
}

answers = []

for key in question_content:
    answer = input(key + "=")
    answers.append(answer)

n = 0

for index, key in enumerate(question_content):
    if question_content[key] == answers[index]:
        n += 1

result = open('result.txt', 'w')
result.write(f"Your final score is {n}/{len(question_content)}.")
result.close()