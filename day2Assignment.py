#list comnprehensions

lst = [i for i in range(10) if i%2==0]
print(lst)

#dictonary compreshensions

dec = {i:f"item{i}" for i in range(10)}
print(dec)

#quesiont 2

length = int(input())
dec={}
for i in range(length):
    i = i+1
    dec.update({i:i*i})
print(dec)


#quesiont 3

lst = []
for i in range(10):
    inpt = int(input())
    if inpt%2==0:
        lst.append(inpt)
print(lst)


#questiont 4

steps = int(input())
up = int(input("UP: "))
down = int(input("DOWN: "))
left = int(input("LEFT: "))
right = int(input("RIGHT: "))


total = up+down+right+left
position = total/steps
print(round(position))
