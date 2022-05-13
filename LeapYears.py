num = int(input())

isp = False

if num > 1:
    
    for i in range(2, num):
        if (num % i) == 0:           
            isp = True
            break

if isp:
    print("No")
else:
    print("Yes")