import sys
inputSet = set();

while(True):
    text = sys.stdin.readline();
    text = text.split(" ");
    if (len(text) == 1):
        break;
    firstNum = int(text[0]);
    if(firstNum == 0):
        break;
    secondNum = int(text[1]);

    if(firstNum == 1):
        inputSet.add(secondNum);
    flag = secondNum in inputSet;
    if(firstNum == 2):
        if(flag == True):
            print("1");
        else:
            print("0");
    if(firstNum == 3):
        if(flag == True):
            inputSet.remove(secondNum);