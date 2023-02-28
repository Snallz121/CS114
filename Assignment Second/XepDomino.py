import math
text = list(map(int,input().split()));
m = text[0];
n = text[1];

result = math.floor((m * n)/2);
print(result);