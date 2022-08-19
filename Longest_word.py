# file=open("longest_word.txt")
# a=file.read().split()
# b=0
# for i in a:
#     if len(i)>b:
#         b=len(i)
#         word=i
# print(word)
# file.close()


file=open("longest_word.txt")
file1=file.read()
word=file1.split()
print(word)
max=word[0]
i=0
while i<len(word):
  if len(word[i])>len(max):
    max=word[i]
  i+=1
print("The longest word is:",max)