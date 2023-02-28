import math

a = float(input());
b = float(input());
c = float(input());

def SelfRound(num):
    if(num - int(num) == 0.0):
        return int(num)

if(a + b > c and a + c > b and b + c > a):
    p = float((a+b+c) / 2)
    DienTich = round(math.sqrt( p* (p-a)* (p-b)* (p-c) ),2); 
    if(DienTich - int(DienTich) == 0.0):
        DienTich = int(DienTich)
    DienTich = str(DienTich)
    if(a == b and a == c):
        print("Tam giac deu, dien tich = " + DienTich);
    elif( a == b or a == c or b == c):
        print("Tam giac can, dien tich = " + DienTich);
    elif( (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (c**2 + b**2 == a**2) ):
        print("Tam giac vuong, dien tich = " + DienTich);
    else:
        print("Tam giac thuong, dien tich = " + DienTich);
else:
    print("Khong phai tam giac");