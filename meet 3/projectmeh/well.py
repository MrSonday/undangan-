import random

prizes = {
    1: 'strawberry',
    2: 'cherry',
    3: 'banana',
    4: 'watermelon'
}

number = int(input('Give me a prize (1-4): '))

print("You won " + prizes.get(number, "nothing!"))