# program to find the sum of two reversed numbers

number_1 = int(input('enter a number: '))
rev = 0
while number_1 > 0:
    new_digit = number_1 % 10
    rev = rev * 10 + new_digit
    number_1 = number_1 // 10

result_1 = rev

number_2 = int(int(input('enter another number: ')))
rev = 0
while number_2 > 0:
    new_digit = number_2 % 10
    rev = rev * 10 + new_digit
    number_2 = number_2 // 10

result_2 = rev

result_3 = result_1 + result_2
print('THE REVERSED SUM OF THE TWO NUMBERS IS: ', result_3)
