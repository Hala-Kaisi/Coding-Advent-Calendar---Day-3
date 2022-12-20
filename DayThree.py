import string
lines = open("D3_Input.txt").readlines()
sharedLetter = []
sum = 0
i = 0
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

print(len(lines))

while i < len(lines):
    firstList = list(lines[i].strip())
    secondList = list(lines[i+1].strip())
    thirdList = list(lines[i+2].strip())
    sharedLetter = [value for value in firstList if value in secondList and value in thirdList]
    if sharedLetter[0] in lowercase:
        sum += lowercase.index(sharedLetter[0]) + 1
    else:
        sum += uppercase.index(sharedLetter[0]) + 27
    i += 3
    
    
print("Sum is: " + str(sum))
    
