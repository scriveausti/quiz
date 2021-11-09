test1 = 'this is a test'
test2 = 'this is also a test'


with open('question_storage.py', 'r+') as f:
    question_read = f.readline()
    question_len = len(question_read)
    while question_len > 0:
        question_read = f.readline()
        question_len = len(question_read)
    f.write('')
    f.write('{} {}\n'.format(test1, test2))
    f.seek(0)
    read = f.read()
    print(read)

