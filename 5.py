f = open('input.txt', 'r')
lines = f.read()
lentext = len(lines) * 8
print(lentext)
a = ['байт', 'килобайт', 'мегабайт', 'гигабайт', 'терабайт']
b = 0
c = lentext
while True:
    c = c // 1024
    if c != 0:
        b += 1
    else:
        break
for i in range(0, b):
    lentext = lentext / 1024
print(f'{lentext} {a[b]}')
