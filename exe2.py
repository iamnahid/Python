print('-' *10  + 'EXERCISE: 2' + '-'*10)

goodCredit = True
hPrice = 1000000
if goodCredit:
    payment = hPrice * (10/100)
else:
    payment = hPrice * (20/100)

print(f'Down Payment: ${payment}')
