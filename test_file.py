with open('question_storage.py', 'r+') as f:
    f.writelines(1["test"])
    read = f.read()
    print(read)
