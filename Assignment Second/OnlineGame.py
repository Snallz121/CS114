inputSet = set();

while(True):
    text = input();
    text = text.split(" ");
    firstNum = int(text[0]);
    if(firstNum == 0):
        break;
    secondNum = int(text[1]);

    if(firstNum == 1):
        inputSet.add(secondNum);
    if(firstNum == 2):
        flag = secondNum in inputSet;
        if(flag == True):
            print("1");
        else:
            print("0");