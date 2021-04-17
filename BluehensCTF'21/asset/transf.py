from pwn import *

p = remote("challenges.ctfd.io",30008)


while(1):
    print(p.recvline())
    p.recvline()
    temp = (p.recvline().split())
    print(temp)
    a = [0]*5
    for i in range(4):
        a[i] = temp[i].decode("utf-8") 
    print(a)
    if(a[1]=='bytearray'):
        b=[]
        for i in range(4,len(temp)-1):
            if(i==4):
                b.append(str(temp[i])[3:-2])
            else:
                b.append(str(temp[i])[2:-2])
        print(b)
    elif(a[1]=='string'):
        a[4] = temp[4]
    else:
        a[4] = temp[4].decode("utf-8")
    print(a)




    if(a[1] == 'bytearray' and a[3] == 'integer:'):
        print("wow0")    
        f = list(map(int,b))
        k=""
        for i in f:
            k=k+(str(i))
        print(k)
        #p.sendline(k)
        p.interactive()


    elif(a[1] == "string" and a[3] == "hexdigest:"):
        print("wow4")
        f=[]
        for i in (a[4]):
            f.append(str(hex((i)))[2:])
        print("".join(f))
        p.sendline("".join(f))       
  
    elif(a[1] == "string" and a[3] == "integer:"):
        print("wow1")
        f=[]
        for i in (a[4]):
            f.append(str((i)))
        print("".join(f))
        p.interactive()
        #p.sendline("".join(f))


   
    #-------------------working-func-start-----------------------
    elif(a[1] == 'bytearray' and a[3] == 'string:'):
        print("wow00")  
        d = list(map(int,b))
        f = ""
        for i in d:
            f=f+str(chr(i))
        print(f)
        p.sendline(f)
        
    

    elif(a[1] == 'bytearray' and a[3] == 'hexdigest:'):
        print("wow00")  
        d = list(map(int,b))
        f = ""
        for i in d:
            f=f+str(hex(i))[2:]
        print(f)
        p.sendline(f)

    elif(a[1] == "integer" and a[3] == "bytearray:"):
        print("wow2")
        a[4]=str(hex(int(a[4],10)))[2:]
        a[4]=a[4][::-1]
        f=""
        for i in range(0,len(a[4]),2):
            f = str(int(a[4][i:i+2][::-1],16)) + ', ' + f
        f= "["+f[:-2]+ "]"
        print(f)
        p.sendline(f)

    elif(a[1] == "integer" and a[3] == "string:"):
        print("wow8")
        a[4]=str(hex(int(a[4],10)))[2:]
        f=""
        for i in range(0,len(a[4]),2):
            f=f+chr(int(a[4][i:i+2],16))
        print(f)
        p.sendline(f)
     

    elif(a[1] == "integer" and a[3] == "hexdigest:"):
        print("wow3")
        f = hex(int(a[4],10))
        f = str(f)[2:]
        print(f)
        p.sendline(f)


    elif(a[1] == "string" and a[3] == "bytearray:"):
        print("hi")
        f="["
        for i in (a[4]):
            f=f+(str(i))+', '
        f=f[:-2]+']'
        print(f)
        p.sendline(f)

    elif(a[1] == "hexdigest" and a[3] == "string:"):
        print("wow5")
        f=""
        for i in range(0,len(a[4]),2):
            f = f + chr(int(a[4][i:i+2],16))
        print(f)
        p.sendline(f)


    elif(a[1] == "hexdigest" and a[3] == "integer:"):
        print("wow7")
        h = str(a[4])
        i = str(int(h,16))
        print(i)
        p.sendline(i)
 

    elif(a[1] == "hexdigest" and a[3] == "bytearray:"):
        print("wow6")
        f=""
        a[4]=a[4][::-1]
        for i in range(0,len(a[4]),2):
            f = str(int(a[4][i:i+2][::-1],16)) + ', ' + f
        f= "["+f[:-2]+ "]"
        print(f)
        p.sendline(f)
       #-------------------end-----------------------








 

p.interactive()