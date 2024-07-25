def biggestNum ( numbers ) :
    biggest= 0
    for number in numbers :
        if number > biggest:
            biggest = number
        return biggest





print( biggestNum (1,2,3,4,5))