test_list =['test']


with open('test.txt', 'r') as q:
    def read_line(q):
        line_start = q.tell()
        q.readline()
        line_end = q.tell() - 2
        q.seek(line_start)
        output = q.read(line_end)
        q.read(1)
        return output


    output = read_line(q)
    while len(output) > 0 :
        test_list.append(output)
        print(test_list)
        output = read_line(q)
