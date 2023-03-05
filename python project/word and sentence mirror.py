w=input()
s=w.split(" ")
pig=[]
for i in s:
    j=i[::-1]
    k=j+"ay"
    pig.append(k)
c=str(pig)
r=c.replace(",","")
r=r.replace("'","")
r=r.replace("[","")
r=r.replace("]","")
print(r)