test_list =['test']


with open('test.txt', 'r') as q:
    def read_line(q):
        read1 = 'e'
        read2 = 'e'
        output = ''
        while read1 != '\ '.strip() and read2 != 'n':
            read1 = q.read(1)
            read2 = q.read(1)
            output += read1 + read2
        return


    output = read_line(q)
    while len(output) > 0 :
        test_list.append(output)
        print(test_list)
        output = read_line(q)
