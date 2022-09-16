# First one
a = float(input('Enter number a:'))
b = float(input('Enter number b:'))
c = float(input('Enter number c:'))
if a > 10 < b <= c and b % 3 == 0 == a % 3:
    print('yes')
else:
    print('no')

# Second one
max_number = None
a = int(input('Enter number a:'))
b = int(input('Enter number b:'))
c = int(input('Enter number c:'))
if b < a > c:
    max_number = a
elif a < b > c:
    max_number = b
elif b < c > a:
    max_number = c
else:
    print('no way')
    exit()

print(f'max value = {max_number}')

# Third one
try:
    input_number = int(input('Enter number: '))
    first_digit = input_number//100
    second_digit = (input_number % 100)//10
    third_digit = input_number % 10
    reversed_number = third_digit*100 + second_digit*10 + first_digit
    if 99 < input_number < 1000:
        print(reversed_number)
    else:
        print('Sorry, this code only for 3 digit numbers')
except ValueError:
    print('Enter number only')
