# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# file=open("file-question3.txt","w")
# for i in banks_list:
#     file.write(i+"\n")
# file.close()

banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
file=open("file-question3.txt","w")
i=0
while i<len(banks_list):
    file.write(banks_list[i]+"\n")
    i=i+1
file.close()