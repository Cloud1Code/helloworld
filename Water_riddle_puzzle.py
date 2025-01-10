def bottle_riddle(five_gallon,three_gallon):

    #fill the 5Gallon jug
    five_gallon=5
    print("5gallon jug = ", five_gallon, " 3 gallon jug = ", three_gallon)
    #Pour from 5G jug to 3G jug
    five_gallon-=3
    three_gallon+=3
    print("5gallon jug = ", five_gallon, " 3 gallon jug = ", three_gallon)
    #empty 3gallon jug
    three_gallon=0
    print("5gallon jug = ", five_gallon, " 3 gallon jug = ", three_gallon)
    #Pour reamining 2gallon from 5G jug to the 3G jug
    five_gallon-=2
    three_gallon+=2
    print("5gallon jug = ", five_gallon, " 3 gallon jug = ", three_gallon)
    #Refill 5Gallon jug
    five_gallon+=5
    print("5gallon jug = ", five_gallon, " 3 gallon jug = ", three_gallon)
    #pour 1G from 5G jug to 3G jug
    five_gallon-=1
    three_gallon+=1
    print("5gallon jug = ", five_gallon, " 3 gallon jug = ", three_gallon)

# main function
#initial jug fill amount is empty
five_gallon=0
three_gallon=0
bottle_riddle(five_gallon, three_gallon)