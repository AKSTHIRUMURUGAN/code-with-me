nl1=[]
word = input()
nl = []
for n in range(1,3):
    for i in word:
        nl.append(i)
    if len(nl) == 0:
        nl.append(nl[0])
        del nl[0]
        x = str(nl)
        y = x.replace(",", "")
        z = y.replace("[", "")
        z1 = z.replace("]", "")
        z2 = z1.replace("'", "")
        z3 = z2.replace('"', "")
        f = z3.replace(" ", "")
        nl1.append(f)

    else:
        for j in nl[-1]:
            j = str(j)
            for k in j:
                nl.append(k)
            nl.append(nl[0])
            del nl[0]
            x = str(nl)
            y = x.replace(",", "")
            z = y.replace("[", "")
            z1 = z.replace("]", "")
            z2 = z1.replace("'", "")
            z3 = z2.replace('"', "")
            f = z3.replace(" ", "")
            nl1.append(f)





print(nl1)
