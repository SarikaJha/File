f=open("vowel_consonant.txt")
a=f.read()
print(a)
# upper=0
# lower=0
vowel=0
consonant=0
i=0
while i<len(a):
    # if a[i]. isupper():
    #     upper+=1
    # if a[i]. islower():
        # lower+=1
    if a[i] in ("a","e","i","o","u","A","E","I","O","U"):
        vowel+=1
    else:
        consonant+=1
    i+=1
# print("upper:",upper)
# print("lower:",lower)
print("vowel:",vowel)
print("consonant:",consonant) 
f.close()