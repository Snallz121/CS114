import math
size = int(input());
TreasureLocation = list(map(int,input().split()));

whiteDistance = math.sqrt((TreasureLocation[0]-1)**2 + (TreasureLocation[1]-1)**2);
blackDistance = math.sqrt((size - TreasureLocation[0])**2 + (size - TreasureLocation[1])**2);

if(whiteDistance == 0):
    print("White");
elif(blackDistance == 0):
    print("Black");
else: 
    if(blackDistance >= whiteDistance):
        print("White");
    else:
        print("Black")