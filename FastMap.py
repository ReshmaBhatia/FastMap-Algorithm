# Group Members: 1) Reshma Bhatia (8959806814)   2) Shiv Prathik Velagala (2654019972)
import copy
import math

with open('C:/Users/RESHMA BHATIA/Desktop/Machine Learning/hw3/hw3/fastmap-data.txt') as f:
    data = [l.split() for l in f.readlines()]
data = [[int(j) for j in i] for i in data]
#print data

max= max(map(lambda x: x[2], data))

temp=[]
for i in data:
    j=data.index(i)
    if max==data[j][2]:
        temp.append(j)

obj1=[]
obj2=[]
#print temp
for i in temp:
    #print i
    j=data[i][0]
    k=data[i][1]
    obj1.append(j)
    obj2.append(k)


pivot1 = min(obj1)
index= obj1.index(pivot1)
pivot2=obj2[index]

pd=max

trying=[]
def distance(data,a,trying):
    #print a
    for i in data:
        j=data.index(i)
        if (data[j][0]<a):
            if (data[j][1]==a):
                trying.append(data[j][2])
        if (data[j][0]==a):
                trying.append(data[j][2])
    #print trying
    return trying
    #print trying
#Distance wrt to pivot1
distwrtp1=[]
distwrtp1=distance(data,pivot1,distwrtp1)
distwrtp1.insert(pivot1-1,0)

#Distance wrt to pivot2
distwrtp2=[]
distwrtp2=distance(data,pivot2,distwrtp2)
distwrtp2.insert((pivot2-1),0)

def cosine(da,db,pd,projection):
    for i in range(len(da)):
        dai=da[i]*da[i]
        dbi=db[i]*db[i]
        pdsq=pd*pd
        numerator=dai+pdsq-dbi
        denominator=2*pd
        x=float(numerator)/(denominator)
        x=round(x,2)
        projection.append(x)
    return projection

projection1=[]
projection1=cosine(distwrtp1,distwrtp2,pd,projection1)
#print 'projection1',projection1

dataduplicate=copy.deepcopy(data)

for i in data:
    j=data.index(i)
    a=data[j][0]
    b=data[j][1]
    c=abs(projection1[a-1]-projection1[b-1])
    c=round(c,2)
    dataduplicate[j][2]=c

newdata=copy.deepcopy(data)


def orthogonal(data,dataduplicate,newdata):
    for i in newdata:
        j=newdata.index(i)
        p=data[j][2]
        sqp=p*p
        q=dataduplicate[j][2]
        sqq=q*q
        r=abs(sqp-sqq)
        s=math.sqrt(r)
        s=round(s,2)
        newdata[j][2]=s


orthogonal(data,dataduplicate,newdata)

l=(map(lambda x: x[2], newdata))
m=0
for k in l:
    if k>m:
        m=k

temps=[]
for i in newdata:
    j=newdata.index(i)
    if m==newdata[j][2]:
        temps.append(j)

obj11=[]
obj22=[]
for i in temps:
    j=newdata[i][0]
    k=newdata[i][1]
    obj11.append(j)
    obj22.append(k)

pivot3 = min(obj11)
index= obj11.index(pivot3)
pivot4=obj22[index]
pd1=m

#Distance wrt to pivot3
distwrtp3=[]
distwrtp3=distance(newdata,pivot3,distwrtp3)
distwrtp3.insert(pivot3-1,0)

#Distance wrt to pivot4
distwrtp4=[]
distwrtp4=distance(newdata,pivot4,distwrtp4)
distwrtp4.insert(pivot4-1,0)


projection2=[]
projection2=cosine(distwrtp3,distwrtp4,pd1,projection2)
#print 'projection2',projection2

FinalProjection=[]
FinalProjection.append(projection1)
FinalProjection.append(projection2)
#print FinalProjection

Invr=zip(*FinalProjection)
print Invr











