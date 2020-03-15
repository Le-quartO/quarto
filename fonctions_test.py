def test(case):
    for x in range(4):
        for i in range(4):


            if case[x][0][i]==case[x][1][i]and case [x][1][i]==case[x][2][i]and case[x][2][i]==case[x][3][i] and  case[x][3][i]!="O" :
                print ("bien joué")



    for y in range(4):
        for i in range(4):


            if case [0][y][i]==case [1][y][i]and case [1][y][i]==case[2][y][i]and case [2][y][i]==case [3][y][i] and case[3][y][i]!="O" :
                print ("bien joué")


    for i in range(4):
        if case[0][0][i]==case [1][1][i]and case [1][1][i]==case [2][2][i]and case [2][2][i]==case [3][3][i] and case[3][3][i]!="O" :
            print ("bien joué")

    for i in range(4):
        if case[0][3][i]==case [1][2][i]and case [1][2][i]==case [2][1][i] and case [2][1][i]==case [3][0][i] and case[3][0][i]!="O" :
            print ("bien joué")
