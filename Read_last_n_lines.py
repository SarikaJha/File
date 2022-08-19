#Write a Python program to read last n lines of a file.
file=open("last_n_lines.txt")
f=file.readlines()
n=int(input("enter the number of lines:"))
print(f[-n:])

 
# file=open("last_n_lines.txt")
# f=file.readlines()
# n=int(input("enter the number of lines:"))
# last_lines=f[-n:]
# for i in last_lines:
#     print(i)
# file.close()