import sys

def count_e(line):
    return line.count('e')

def count_words(line):
    return len(line.split(' '))


def count_consecutive(line):
    last = None
    count = 0
    for c in line:
        if c == last:
            count += 1

        last = c

    return count
        

while True:
    line = raw_input()
    if line:
        v8 = count_consecutive(line)
        v9 = count_words(line)
        v10 = count_e(line)

        if v8 <= v9 or v8 <= v10:
            if v9 <= v8 or v9 <= v10:
                print 'Negotiate'
            else:
                print 'Refused'

        else:
            print 'Accepted'
    else:
        break

