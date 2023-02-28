SoPhanTu = int(input());
MangSoNguyen = input();
text = input();
text = text.split();
k = int(text[0]);
x = int(text[1]);

MangSoNguyen = list(map(int,MangSoNguyen.split()));

def Distance(num1, num2):
    return abs(num1 - num2);

result = [];

if(MangSoNguyen[0] > x):
    Target = 0;
    while(k > 0):
        result.append(MangSoNguyen[Target]);
        Target += 1;
        k -= 1;
elif(MangSoNguyen[len(MangSoNguyen) - 1] < x):
    Target = len(MangSoNguyen) - k;
    while(k > 0):
        result.append(MangSoNguyen[Target]);
        Target += 1;
        k -= 1;
elif(len(MangSoNguyen) == k):
    result = MangSoNguyen;
else:
    Target = 0;
    for i in range(0,len(MangSoNguyen)):
        if(MangSoNguyen[i] > x):
            Target = i - 1;
            break;
 
    index1 = Target - 1;
    index2 = Target + 1;

    result.append(MangSoNguyen[Target]);
    k -= 1;

    while(k > 0):

        if(index1 >= 0):
            dis1 = Distance(x, MangSoNguyen[index1]);
        if(index2 < len(MangSoNguyen)):
            dis2 = Distance(x, MangSoNguyen[index2]);

        if(index2 == len(MangSoNguyen)):
            if(index1 == -1):
                break;
            result.append(MangSoNguyen[index1]);
        elif(index1 == -1):
            if(index2 == len(MangSoNguyen)):
                break;
            result.append(MangSoNguyen[index2]);
        elif(dis1 == dis2):
            result.append(MangSoNguyen[index1]);
            index1 -= 1;
        elif(dis1 > dis2):
            result.append(MangSoNguyen[index2]);
            index2 += 1;
        else:
            result.append(MangSoNguyen[index1]);
            index1 -= 1;
        k -= 1;

result.sort();
result = ' '.join(map(str,result));
print(result);