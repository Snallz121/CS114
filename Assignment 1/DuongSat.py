text = input();
textNew = text.split(" ");

k = int(textNew[0]);
t = 0;

for i in range(1,len(textNew),1):
    if(textNew[i] != " "):
        t = textNew[i];

t = int(t);

k2 = k * 2; 
t = t % k2;

if (t < k):
    print(t);
elif (t == k):
    print(t);
else:
    t = k - (t % k);
    print(t);