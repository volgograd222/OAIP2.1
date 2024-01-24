import random
f = open('lines.txt', 'r')
lines = f.read()
lines = lines.split('\n')
if lines:
    print(random.choice(lines))
