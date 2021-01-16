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

# Another way of doing it

# # read from questions.txt and append each line into a list
# questions = open("questions.txt", "r")  # read from questions.txt
 
# # read all lines and get rid of line break for each line, then append each stripped line to a list
# question_list = [line.strip() for line in questions]
# questions.close()
 
# score = 0  # initialize score
# total = len(question_list)  # set total score
 
# for line in question_list:
#     # split equation with `=` into question and answer
#     q, a = line.split("=")
 
#     # print question and wait for user to input their answer
#     ans = input(f"{q}=")
 
#     if a == ans:  # if user input matches answer
#         score += 1  # increase score
 
# result = open("result.txt", "w")  # open result.txt
# # write final score to result.txt
# result.write(f"Your final score is {score}/{total}.")
# result.close()