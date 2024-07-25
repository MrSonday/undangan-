import random
prize1 = 'strawberry'
prize2 = 'cherry'
prize3 = 'banana'
prize4 = 'watermelon'
number = input('Give me a prize :')
number = int(number)

if number == 1:
    print(" You won " + prize1 )
elif number == 2:
    print(" You won " + prize2 )
elif number == 3:
    print(" You won " + prize3 )
elif number == 4:
    print(" You won " + prize4 )
else:
    print(" You won nothing ! ")