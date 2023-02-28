import math
SoChuSo = int(input());
Number = input();

count = 0;
for i in range(SoChuSo):
    if(Number[i] == "8"):
        count += 1;
possibleANum = math.floor(SoChuSo / 11);
if(possibleANum < count):
    count = possibleANum;

print(count);