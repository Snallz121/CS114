import math

count = int(input());
InputList = [];
while(count > 0):
    text = input();
    if not text:
        continue;
    InputList.append(text);
    count -= 1;

for index in range (0,len(InputList)):
    newText = InputList[index].split(" ");
    tu = int(newText[0]);
    for i in range(1, len(newText)):
        if(newText[i] != " "):
            mau = newText[i];
            break;
    mau = int(mau);
    UocChung = math.gcd(tu,mau);
    tu = tu // UocChung;
    mau = mau // UocChung;
    if(mau <= 1):
        print(str(int(tu)));
    else:
        print(str(int(tu)) + " " + str(int(mau)));