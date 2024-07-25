import random
prizes = [ "stawberry","apple","banana","cerry"]
jml = len(prizes)

num = random.randint(1, jml - 1)
if num >= 1 and num <= jml:
    print(f"you won {prizes[num]}")
else:
    print("last")