w=input()
s=w.split(" ")
pig=[]
pig1=[]

for i in s:
    e=i[0]
    k=e+"ay"
    n=i+k
    pig.append(n)
for j in pig:
    l1=list(j)
    l1.pop(0)
    k=l1
    pig1.append(k)
    pig1.append("/")
c=str(pig1)
r=c.replace(",","")
r=r.replace("'","")
r=r.replace("[","")
r=r.replace("]","")
r=r.replace(" ","")
r=r.replace("/"," ")
print(r)