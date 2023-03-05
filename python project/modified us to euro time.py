us = input()

try:
    s = us.split(" ")
    l1 = list(s)
    d = l1[1]
    m = l1[0]
    y = l1[2]
    m = m.lower()
    m = m.replace(",", "")
    m = m.replace("/", "")
    d = d.replace(",", "")
    d = d.replace("/", "")
    y = y.replace(",", "")
    y = y.replace("/", "")
    months = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july", 8: "august",
              9: "september", 10: "october", 11: "november", 12: "december"}
    for j in months:
        if months[j] == m:
            m =j
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
    m = m.replace(",", "")
    m = m.replace(" ", "")
    d = d.replace(",", "")
    d = d.replace(" ", "")
    y = y.replace(",", "")
    y = y.replace(" ", "")
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
    m = m.replace(" ", "")
    m = m.replace("/", "")
    d = d.replace(" ", "")
    d = d.replace("/", "")
    y = y.replace(" ", "")
    y = y.replace("/", "")
    months = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july", 8: "august",
              9: "september", 10: "october", 11: "november", 12: "december"}
    for j in months:
        if months[j] == m:
            m = j
    print(d, m, y, sep="/")
except:
    pass

