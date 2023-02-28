smatrix1 = list(map(int, input().split()));
smatrix2 = list(map(int, input().split()));
dong1 = smatrix1[0];
cot1 = smatrix1[1];
dong2 = smatrix2[0];
cot2 = smatrix2[1];

inputMatrix = [];
for i in range(0, dong1):
    inputMatrix.append(input());

if((dong1 * cot1) != (dong2 * cot2)):
    for i in range (0, dong1):
        print(inputMatrix[i]);
else:
    oneDArray = [];
    for i in range(0, dong1):
        inputMatrix[i] = inputMatrix[i].split();
        for j in range(0, cot1):
            oneDArray.append(inputMatrix[i][j]);

    newMatrixline = str();
    index = 0;
    for i in range(0, dong2):
        for j in range(0, cot2):
            if(j == cot2 - 1):
                newMatrixline += oneDArray[index];
                index+=1;
            else:
                newMatrixline += oneDArray[index] + " ";
                index +=1;
        print(newMatrixline);
        newMatrixline = str();