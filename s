a= 1
b=1000
n=int(b**(1/2))
d,final=[],[]
for i in range(a,b-a,2):
    d.append(i)
d.append(2)
del d[1]
for num in d:
    for m in range(2,n):
        if m<num:
            if num%m!=0:
                print()

