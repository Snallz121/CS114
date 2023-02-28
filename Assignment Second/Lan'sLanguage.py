text = input().split();

def LanLanguage(text):
    nounnum = 0;
    count = 0;
    flag = -1; # 0 la nam, 1 la nu
    sstruct = -1; # 0 la adj, 1 la noun, 2 la verb
    for i in range(0, len(text)):
        #adjective
        tmp1 = text[i][len(text[i]) - 4 : len(text[i])];
        tmp2 = text[i][len(text[i]) - 5 : len(text[i])];
        if(tmp1 == "lios"):
            if(flag == 1 or sstruct > 0):
                print("NO");
                return;
            flag = 0;
            sstruct = 0;
            count +=1;
        elif(tmp2 == "liala"):
            if(flag == 0 or sstruct > 0):
                print("NO");
                return;
            flag = 1;
            sstruct = 0;
            count += 1;
        #noun
        tmp1 = text[i][len(text[i]) - 3 : len(text[i])];
        tmp2 = text[i][len(text[i]) - 4 : len(text[i])];
        if(tmp1 == "etr"):
            nounnum += 1;
            if(flag == 1 or nounnum > 1 or sstruct > 1):
                print("NO");
                return;
            flag = 0;
            sstruct = 1;
            count += 1;
        elif(tmp2 == "etra"):
            nounnum += 1;
            if(flag == 0 or nounnum > 1 or sstruct > 1):
                print("NO");
                return;
            flag = 1;
            sstruct = 1;
            count +=1;
        #verb
        tmp1 = text[i][len(text[i]) - 6 : len(text[i])];
        if(tmp1 == "initis"):
            if(flag == 1):
                print("NO");
                return;
            flag = 0;
            sstruct = 2;
            count += 1;
        elif(tmp1 == "inites"):
            if(flag == 0):
                print("NO");
                return;
            flag = 1;
            sstruct = 2;
            count += 1;
    if(count == len(text)):
        print("YES");
    else:
        print("NO");

LanLanguage(text);