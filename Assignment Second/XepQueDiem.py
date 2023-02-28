NumTestcase = int(input());
count = 0;
while(count < NumTestcase):
    num = int(input());
    if(num == 2):
        print("2");
    else:
        tmp = num % 2;
        print(tmp);
    count += 1;