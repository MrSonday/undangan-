import random
prizes = {
    1: 'strawberry',
    2: 'cherry',
    3: 'banana',
    4: 'watermelon'
}
number = input('Give me a prize (1-4): ')
number = int(number)
if number in prizes:
    print("You won " + prizes[number])
else:
    print("You won nothing!")