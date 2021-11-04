askquestion = ["test"]
answer1 = ['test']
answer2 = ['test']
answer3 = ['test']
answer4 = ['test']
correct_answer = ['test']


with open('question_storage.py', 'r') as q:
    output_list
    while len(ask_q) > 0:
        askquestion.append(ask_q)
        print('1', askquestion)
        answer1.append(q.readline())
        print(answer1)
        answer2.append(q.readline())
        print(answer2)
        answer3.append(q.readline())
        print(answer3)
        answer4.append(q.readline())
        print(answer4)
        correct_answer.append(q.readline())
        print(correct_answer)
        ask_q = q.readline()



print(askquestion)
print(answer4)
print(answer3)
print(answer2)
print(answer4)
print(correct_answer)
