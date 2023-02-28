text = list(map(int, input().split()));
dong = text[0];
cot = text[1];
image = [];
for i in range (0, dong):
    inputLine = list(map(int, input().split()));
    image.append(inputLine);
location = list(map(int,input().split()));

for i in range(0, location[0]): 
    for j in range(0, cot):
        image[i][j] = 0;
for i in range(0, dong): 
    for j in range(0, location[1]):
        image[i][j] = 0;

for i in range(0, dong): 
    for j in range(location[3] + 1, cot):
        image[i][j] = 0;

for i in range(location[2] + 1, dong): 
    for j in range(0, cot):
        image[i][j] = 0;

for i in range(0, dong):
    image[i] = ' '.join(map(str,image[i]));

for i in range(0, dong):
    print(image[i]);