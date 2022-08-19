file=open(input("enter filename:"))
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