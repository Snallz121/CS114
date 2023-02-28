import math
from decimal import Decimal, getcontext

num = float(input()); 
getcontext().prec = 6;
newNum = Decimal(num) * Decimal(0.453592 / 2.54**2);
newNum = str(newNum.normalize());
print(newNum);