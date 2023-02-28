text = input();
newText = text.split(" ");

n = int(newText[0]);
for i in range(1, len(newText),1):
    if(newText[i] != " "):
        m = newText[i];
        break;
m = int(m);

AllMove = (n - 1) * (m - 1);
print(AllMove);