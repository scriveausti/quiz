with open('question_storage.txt', 'r+') as f:
    question_read = f.readline()
    question_len = len(question_read)
    while question_len > 0:
        print(question_read, end='')
        question_read = f.readline()
        question_len = len(question_read)
    f.write('')
    f.write('\n test')
    f.seek(0)
    print(f.read)
