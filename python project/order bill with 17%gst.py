order=input()
s=order.lower()
p=s.split(" ")
value=0
menu={"nachos":6,"pizza":6,"cheese burger":10,"meal":10,"water":4,"coke":5}
for i in p:
    for j in menu:
        if i==j:
            v=menu[j]
            v=int(v)
            value+=v
        else:
            value+=0
bill=value+(7/100)*value
print(bill)

