# f=open("count_WLL.txt")
# f1=f.read()
# f2=f1.split()
# print(f1)
# i=0
# count_letters=0
# while i<len(f2):
#     j=0
#     while j<len(f2[i]):
#         count_letters+=1
#         j+=1
#     i+=1
# print("no. of words:",len(f2))
# print("no. of letters:",count_letters)
# f.close()
# f3=open("count_WLL.txt")
# f4=f3.readlines()
# print("no. of lines:",len(f4))


file = open("count_WLL.txt","r")

number_of_lines = 0
number_of_words = 0
number_of_letters = 0
for line in file:
  line = line.strip("\n")


  words = line.split()
  number_of_lines += 1
  number_of_words += len(words)
  number_of_letters += len(line)
# print("lines:", number_of_lines, "words:", number_of_words, "letters:", number_of_letters)
print("number of lines:",number_of_lines)
print("number of words:",number_of_words)
print("number of letters:",number_of_letters)
file.close()