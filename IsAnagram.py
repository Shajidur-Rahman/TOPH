a = input()
b = input()

ali = []
bli = []

for i in range(len(a)):
    ali.append(a[i])
    
for i in range(len(b)):
    bli.append(b[i])

ali.sort()
bli.sort()

if ali == bli:
    print("Yes")
else:
    print("No")    