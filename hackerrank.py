### sWAP cASE
s = "Hayat"
def swap_case(s):   
    return s.swapcase()
print(swap_case(s))
### String Split and Join
words = "Is it work?"
def split_and_join(words):
    x=words.split(" ") 
    x='-'.join(x)    
    return x
print(split_and_join(words))
### Mutations
word = "Hello"
def mutation(word):
    a = list(word)
    a[1] = "ö"
    word = "".join(a)
    return word
print(mutation(word))
### Text Wrap
x = "I   dontknowthatis  it  work"
max_width = 4
def wrap(x, max_width):
    s=""
    for i in range(0,len(x),max_width):
        s=s+x[i:i+max_width]+"\n"
    return s
print(wrap(x, max_width))
