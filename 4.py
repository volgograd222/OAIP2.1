f = open('words.txt', 'r')
lines = f.readlines()
maxlen = 0
maxword = []
for i in lines:
    word = i.strip()
    if len(word) > maxlen:
        maxlen = len(word)
        maxword = [word]
    elif len(word) == maxlen:
        maxword.append(word)
print(*maxword)

