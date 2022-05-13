from enum import Flag


a = int(input())

li = ["0","1","2","3","4","5","6", "O"]

for i in range(a):
    s = 0
    x = input()
    # print(x)
    y = []
    for i in range(len(x)):
        y.append(x[i])
    # print(y)
    for i in range(len(y)):
        if (y[i]) in li:
            # print("YES")
            # print(y[i])
            s = s+1
    o = 0
    b = 0        
    while s>=6:
        o = o+1
        s = s-6
    b = s
    
    bp = False
    op = False

    if o != 0:
        op = True
    if b!=0:
        bp = True
    
    if bp == False and op == True:
        if o == 1:
            print("1 OVER")
        else:
            print(f"{o} OVERS")
    
    elif bp == True and op == False:
        if b == 1:
            print("1 BALL")
        else:
            print(f"{b} BALLS")

    else:
        if o==1 and b==1:
            print("1 OVER 1 BALL")
        elif o == 1 and b!=1:
            print(f"1 OVER {b} BALLS")
        elif o!=1 and b==1:
            print(f"{o} OVERS 1 BALL")
        else:
            print(f"{o} OVERS {b} BALLS")