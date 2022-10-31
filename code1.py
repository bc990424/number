a= 1
b=100
n=int(b**(1/2))
d,final=[2],[]
def privenum(x,y):
  for i in range(x,y-x,2):
    d.append(i)
  del d[1]
  for num in d:
    for m in range(3,n):
        if m<num:
            if num%m ==0:
              del d[num]
privenum(a,b)
print(d)
