lo=input()
flg=1
flm=1
flt=1



for j in lo:
    if '$'==j:
        break
    else:
        flm+=1
for k in lo:
    if 'T'==k:
        break
    else:
        flt+=1
if lo.count("G")>1 and flt>flm:
    for n in range(flm+1,len(lo)):
       if lo[n]=="G":
           break
       else:
           flg=flm+1
else:
    for i in lo:
        if 'G' == i:
            break
        else:
                flg = flg + 1

if flm<flg and flg<flt:
    print("quiet")
elif flm>flg and flg>flt:
    print("quiet")
else:
    print("ALARM")



