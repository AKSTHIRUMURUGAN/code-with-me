w1=input()
w2=input()
w3=input()
w4=input()
l1=list(w1)
l2=list(w2)
l3=list(w3)
l4=list(w4)

m1=l1[::-1]
m2=l2[::-1]
m3=l3[::-1]
m4=l4[::-1]

if l1==m1 or l2==m2 or l3==m3 or l4==m4:
    print("open")
else:
    print("sorry")