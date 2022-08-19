#Write a Python program to append text to a file and display the text.
file_name="append_read.txt"
file=open(file_name,"a")
file.write("\n"+"Engineering in Navgurukul.")
file.close()
file=open(file_name)
print(file.read())

# file_name="append_read.txt"
# def append_file(file_name):
#     file=open(file_name,"a")
#     file.write("\n"+"append to end of line")
#     file.close()
#     file=open(file_name)
#     print(file.read())
# append_file("append_read.txt")