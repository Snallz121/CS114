text = input();
textNew = text.split(" ");

SoCon = int(textNew[0]);
SoChan = int(textNew[1]);

SoCho = int((SoChan - 2 * SoCon) / 2);
SoGa = SoCon - SoCho;

print(str(SoGa) + " " + str(SoCho));