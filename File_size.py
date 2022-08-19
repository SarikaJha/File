# f=open("docs.txt","r")
# a=f.read()
# count=0
# while count<len(a):
#     count+=1
# f.close()
# print("th size of the file is:",count,"Bytes")


# import os
# f = open('docs.txt')
# # move file cursor to end
# f.seek(0, os.SEEK_END)
# # get the current cursor position
# print('Size of file is:', f.tell(), 'bytes')

f = open('docs.txt')
print(f.read())
print("file size is:",f.tell(),"bytes")