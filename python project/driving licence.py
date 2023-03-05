name=input()
worker=int(input())
o=input()
om=o.split(" ")
om.append(name)
om.sort()
c=0
for i in om:
    if i==name:
        break
    else:
        c=c+1

t=((c//worker)*20)+20
print(t)

