'''#archers code
l=["arc101,0,0,5,5,5,7,7,9,9","arc102,9,6,6,8,8,8,8,8,9,9","arc103,6,6,6,6,6,8,8,9,9,9"]

l3=[]
l4=[]
for i in l:
    sum=0
    d={}
    l1=[]
    l1=i.split(",")
    l2=[]
    for j in l1:
        if j.isdigit():
            sum=sum+int(j)
            l2.append(int(j))
            if sum>=50:
                d[l1[0]]=(l2)
                break
    #print(l2)           
    if sum>=50:    
        l4.append(d)
print(l4)
print(l1)
#k=[list(d.keys())[0] for d in l4]
#print(k)
k=[]
for e in l4:
    k.append(list(e.keys())[0])
print(k)
'''




'''#encrypted message code in mock
#case1
s=input()
numkey=int(input())
l=s.split(" ")
print(l)
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
#case2
x=" ".join(l1)
n=""
for i in x:
    if i!=" ":
        n=n+chr(ord(i)+numkey)
    else:
        n=n+" "
print(n)'''



#archers score
archers_score=['ARC101,0,0,0,5,5,7,7,9,9','ARC102,9,6,6,8,8,8,8,8,9,9','ARC103,6,6,6,6,6,8,8,9,9,9']#l=["ARC101",'ARC102','ARC103']L1=[0,0,
l1=[]
l2=[]
l5=[]
for i in archers_score:
        l3=[]
        l=i.split(",")
        for i in l:
            if i.isdigit():
                l3.append(int(i))
            else:
                l2.append(i)
        l1.append(l3)
print(l2)
print(l1)
for i in l1:
    l4=[]
    summ=0
    if sum(i)<50: 
        pass
    else:
        for j in i:
           
            summ=summ+j
            l4.append(j)
            if summ>=50:
                break
        l5.append(l4)
print(l5)

























    
