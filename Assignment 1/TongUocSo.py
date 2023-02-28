inData = int(input());
Tong = 0;
inData2 = int(inData / 2) + 1
for i in range(1, inData2 ):
    if( (inData % i) == 0):
        Tong += i;
print(Tong);