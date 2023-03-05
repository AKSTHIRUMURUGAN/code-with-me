z=1
def num():
    for i in range(z,z+1):
        k=str(i)
        return k

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
       file = open("todolist.txt", "a")
       a= input("enter your task:")
       k=num()
       print(k)
       file.write(k+"."+a+"\n")

       file.close()
       z = z + 1
       print("your task successfully uploaded...")
    elif iv==2:
        file = open("todolist.txt", "r")
        x=file.readlines()
        for i in x:
            print(i)
    elif iv==3:
        n=int(input("which number you want to delete"))
        with open("todolist.txt") as x:
            x=x.readlines()
            x.pop(n-1)
            file=open("todolist.txt",'w')
            file.writelines(x)





    elif iv==4:

        e=e+1
    else:

        print("invalid option try again")
        file = open("todolist.txt", "w")
        file.write("")





