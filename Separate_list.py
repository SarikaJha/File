file=open("question3.txt")
a=file.readlines()
i=0
while i<len(a):
    if "delhi" in a[i]:
        x=open("delhi.txt","a")
        x.write(a[i])
    elif "shimla" in a[i]:
        y=open("shimla.txt","a")
        y.write(a[i])
    else:
        z=open("others.txt","a")
        z.write(a[i])
    i+=1
file.close()   