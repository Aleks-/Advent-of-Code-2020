import pprint

count = 0
with open('input.txt') as f:
    for line in f:
        count += 1
    #pprint.pprint(lines)
print(count)