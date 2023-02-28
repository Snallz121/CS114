import sys
MyList = [];

while(True):
    text = sys.stdin.readline().split();
    order = text[0];

    if(order == "6"):
        break;

    if(order == "5"):
        if(len(MyList) == 0):
            continue;
        MyList.remove(MyList[0]);
        continue;

    num = text[1];

    if(order == "0"):
        MyList.insert(0, num);
        continue;

    if(order == "1"):
        MyList.append(num);
        continue;

    if(order == "2"):
        tmp = text[2];
        if (num in MyList):
            i = MyList.index(num);
            MyList.insert(i + 1, tmp);
            continue;
        else:
            MyList.insert(0, tmp);
            continue;

    if(order == "3"):
        if (num in MyList):
            MyList.remove(num);
            continue;
        else:
            continue;
    
    if(order == "4"):
        while(num in MyList):
            MyList.remove(num);
            
MyList = ' '.join(map(str,MyList));
sys.stdout.write(MyList)