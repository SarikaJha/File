#Write a Python program to read first n lines of a file. 
file=open("first_n_lines.txt")
n=int(input("enter the number of lines:"))
i=0
while i<n:
    line=file.readline()
    print(line)
    i+=1