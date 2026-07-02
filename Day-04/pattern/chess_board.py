white='\u25A0'
black='\u25A1'
white_pawn='♙'
black_pawn='♟'
black_rook='♜'
white_rook='♖'
white_knight='♘'
black_knight='♞'
white_bishop='♗'
black_bishop='♝'
black_king='♚'
white_king='♔'
white_queen='♕'
black_queen='♛'
for i in range(0,8):
    for j in range(8):
        if(i==1):
            print(white_pawn,end=' ')
        elif(i==6):
            print(black_pawn,end=' ')
        elif(i==0 ):
            if (j==0 or j==7):
                print(white_rook,end=' ')
            elif(j==1 or j==6):
                print(white_knight,end=' ')
            elif(j==2 or j==5):
                print(white_bishop,end=' ')
            elif(j==4):
                print(white_king,end=' ')
            else:
                print(white_queen,end=' ')
        elif(i==7):
            if (j==0 or j==7):
                print(black_rook,end=' ')
            elif(j==1 or j==6):
                print(black_knight,end=' ')
            elif(j==2 or j==5):
                print(black_bishop,end=' ')
            elif(j==4):
                print(black_king,end=' ')
            else:
                print(black_queen,end=' ')
        elif(i+j)% 2 == 0:
            print(white,end=" ")
        else:
            print(black,end=" ")
    print()