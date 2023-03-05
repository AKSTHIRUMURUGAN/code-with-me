pw=input()
pw=list(pw)
num=['1','2','3','4','5','6','7','8','9','0']
sc=['!','@','#','$','%','&','*']
n=0
s=0
for i in pw:
    for j in num:
        if i==j:
            n=n+1
    for k in sc:
        if k==i:
            s=s+1
if len(pw)>7 and n>=2 and s>=2:
    print("Strong")
else:
    print("Weak")