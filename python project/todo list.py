tl=[]

e=0

while e<1:
    print('''
     options:
     1.add a new task
     2.view tasks
     3.delete
     4.quite''')

    iv = int(input("ENTER YOUR OPTION:"))
    if iv==1:
       a= input("enter your task:")
       tl.append(a)
       print("your task successfully uploaded...")
    elif iv==2:
        for i in tl:
            print(i)
    elif iv==3:
        r=int(input("enter the number of  to be delete:"))
        tl.pop(r-1)
    elif iv==4:
        e=e+1
    else:
        print("invalid option try again")