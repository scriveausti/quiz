with open('test.txt', 'r+') as t:
    test = 'test'

    t.write('{}, {}, {}'.format(test, test, test))


    t.seek(0)
    print(t.read())


