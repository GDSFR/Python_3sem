a=[0,1,2,3,4,5,6,7,8,9]
print (a)
c=a[8::-2]
a[::2]=reversed (a[::2])
print (a)
for i in range(0,10,1):
    if not i%2:
        a[i]=c[i//2]
print(c)
print (a)