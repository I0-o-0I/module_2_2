first = input('Введите превое число:')
second = input('Введите второе число:')
third = input('Введите третье число:')
if first==second==third:
    print('3')
elif first==second!=third or first==third!=second or first!=second==third:
    print('2')
else:
    print('0')
