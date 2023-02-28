inData = int(input());

def Fibonanci(inData):
    FiboArray = [0,1];
    for i in range(2, inData+1):
        newVindex = FiboArray[i-1] + FiboArray[i-2];
        FiboArray.append(newVindex);
    return FiboArray[inData];

if(inData < 1 or inData > 30):
    print("So",inData,"khong nam trong khoang [1,30].")
else:
    print(Fibonanci(inData))