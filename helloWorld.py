print('-' *10  + 'EXERCISE: 3' + '-'*10)

name = input("Enter your name: ")
nLen = len(name)
if nLen < 3:
    print("Name must be at least 3 characters")
elif nLen > 10:
    print("Name can be max of 10 characters")
else:
    print("Name looks good")