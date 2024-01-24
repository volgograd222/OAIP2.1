f = open('prices.txt', 'r')
total = 0
lines = f.readlines()
for i in lines:
    line = i.split()
    if len(line) == 3:
        a = float(line[1])
        b = float(line[2])
        total += a * b
if total:
    print(f'{total:.2f}')
