LaptopLeft = int(input());
inputArray = list(map(int, input().split()));

inputArray.sort();
count = 0;
for i in range(1, len(inputArray)):
    tmp = inputArray[i] - inputArray[i-1];
    if(tmp > 1):
        count += tmp - 1;
print(count);