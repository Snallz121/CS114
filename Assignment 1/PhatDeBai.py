import math

SoHS = int(input());
SoDe = int(input());
AliceH = int(input());
AliceC = int(input());

def Coordinate(ViTriBob):
    if(ViTriBob <= 0):
        return -1;
    if(ViTriBob > SoHS):
        return -1;
    if(ViTriBob % 2 != 0):
        result = (ViTriBob + 1) / 2;
        return (int(result),1);
    else:
        result = ViTriBob / 2;
        return (int(result),2);

ViTriAlice = 0;

if(AliceC % 2 != 0):
    ViTriAlice = AliceH * 2 - 1;
else:
    ViTriAlice = AliceH * 2;


ViTriBob1 = Coordinate(ViTriAlice - SoDe);
ViTriBob2 = Coordinate(ViTriAlice + SoDe);

if(ViTriBob1 == -1 and ViTriBob2 == -1):
    print("-1");
elif(ViTriBob1 == -1):
    print(str(ViTriBob2[0]) + " " + str(ViTriBob2[1]));
elif(ViTriBob2 == -1):
    print(str(ViTriBob1[0]) + " " + str(ViTriBob1[1]));
else:
    print(str(ViTriBob1[0]) + " " + str(ViTriBob1[1]));