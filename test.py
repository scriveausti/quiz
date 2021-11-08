with open('test.txt', 'r') as q:
    def read_line(q):
        line_start = q.tell()
        q.readline()
        line_end = q.tell() - 2
        q.seek(line_start)
        output = q.read(line_end)
        q.read(2)
        return output


    output = read_line(q)
    while len(output) > 0 :
        print(output)
        output = read_line(q)