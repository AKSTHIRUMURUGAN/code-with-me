#this commented program is work when we use perfect formate osnumber values only
#s=input()
#m=list(s)
#print(m[3],m[4],"/",m[0],m[1],"/",m[6],m[7],m[8],m[9])

#this is work for any type of formate
us = input()

try:
    s = us.split(" ")
    l1 = list(s)
    d = l1[1]
    m = l1[0]
    y = l1[2]
    m = m.lower()
    months = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july", 8: "august",
              9: "september", 10: "october", 11: "november", 12: "december"}
    for j in months:
        if months[j] == m:
            m = j
    print(d, m, y, sep="/")
except:
    pass
try:
    s = us.split("/")
    l1 = list(s)
    d = l1[1]
    m = l1[0]
    y = l1[2]
    m = m.lower()
    months = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july", 8: "august",
              9: "september", 10: "october", 11: "november", 12: "december"}
    for j in months:
        if months[j] == m:
            m = j
    print(d, m, y, sep="/")
except:
    pass
try:
    s = us.split(",")
    l1 = list(s)
    d = l1[1]
    m = l1[0]
    y = l1[2]
    m = m.lower()
    months = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july", 8: "august",
              9: "september", 10: "october", 11: "november", 12: "december"}
    for j in months:
        if months[j] == m:
            m = j
    print(d, m, y, sep="/")
except:
    pass

print(''' **note:
      the input must seperate using comma space or backslash(,or or /)
      if the value is wrong,check your input formate:** ''')




