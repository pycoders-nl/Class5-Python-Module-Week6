#1. sWAP cASE: https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    a=""
    for i in s:
        if i.isupper():
            a+=i.lower()
        elif i.islower():
            a+=i.upper()
        else:
            a+=i
    return a


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# 2. String Split and Join: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
def split_and_join(line):
    return '-'.join(line.split(' '))
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
# 3. Mutations: https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
#4. Text Wrap: https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap
def wrap(string, max_width):
    return '\n'.join([string[i:i+max_width] for i in range(0,len(string),max_width)])


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
