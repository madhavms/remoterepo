import random
a=raw_input("ENTER NUMBER TO BE SEARCHED:")
ls=[]
ls1=[]
x=True
y=True
i=0
l=10
j=0
k=0
p=0
while x:

    num=random.randint(1,l)
    if num not in ls1:
        ls1.append(num)
        i=i+1
    if i==l:
        x=False
print "ACTUAL LIST"
print ls1
print "SORTED LIST:",

ls=sorted(ls1)
l=len(ls)
last=l-1
first=0

print ls



while first<=last:
    mid=(first+last)/2
    if(int(a)==ls[mid]):
        print 'ELEMENT FOUND AT'+" "+str(mid+1)

        break
    elif(int(a)>ls[mid]):

        first=mid+1


    else:

        last=mid-1
if last<first:
    print "ELEMENT NOT FOUND"
