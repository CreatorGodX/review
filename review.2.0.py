#    
data = []
count = 0
number = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)

        x = len(line)
        number += x

        count += 1
        if count % 1000 == 0:
            print(len(data))
LEN = len(data)
average = round(number / LEN, 1)

print('the comment lenght average is', average, ':D')

great = []
with open ('reviews.txt', 'r') as g:
    for line in g:
        if 'great' in line:
            great.append(line)
print('there are', len(great), 'comment with "great" here :D')