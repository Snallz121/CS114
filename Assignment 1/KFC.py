import math
from decimal import Decimal, getcontext

F = float(input()); 
getcontext().prec = 6;
C = Decimal(F - 32) * Decimal(5 / 9);
C = str(C.normalize());
K = Decimal(float(C)) + Decimal(273.15);
K = str(K.normalize());
print(C + " " + K);