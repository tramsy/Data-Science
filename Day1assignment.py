cost = int(input('Enter a cost price' ))
selling = int(input('Enter a selling price' ))

if cost>selling:
    print('"Loss"')
elif selling>cost:
    print('"Profit"')
else:
    print('"Neighter"')


#question 2

print('"LETS UPGRADE"')

#question 3

price = int(input())
print(price*80)


#question 4

word = ['RANIBOW', 'RAINBOW', 'BOWRANI', 'ROBWANI']
for i in word:
    if i == 'RAINBOW':
        print(i, 'is meaningfull word')
