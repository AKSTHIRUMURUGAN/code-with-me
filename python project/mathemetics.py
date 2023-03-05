ans = int(input())


def os():

    option = input()
    o = option.split(" ")
    n = 0
    ov = []
    for i in o:
        x = i.replace("(", "")
        y = x.replace(")", "")
        if "+" in y:
            z = y.split("+")
            op = "+"
        elif "-" in y:
            z = y.split("-")
            op = "-"
        elif "*" in y:
            z = y.split("*")
            op = "*"
        elif "/" in y:
            z = y.split("/")
            op = "/"
        else:
           pass


        v1 = int(z[0])
        v2 = int(z[1])

        if op == "+":
            a = v1 + v2
            ov.append(a)

        elif op == "-":
            a = v1 - v2
            ov.append(a)
        elif op == "*":
            a = v1 * v2
            ov.append(a)
        elif op == "/":
            a = v1 / v2
            ov.append(a)
        else:
            print("no")
    return ov


ov=os()


if ov[0]==ans:
    print("index 0")
elif ov[1] == ans:
    print("index 1")
elif ov[2]==ans:
    print("index 2")
else:
    print("none")


