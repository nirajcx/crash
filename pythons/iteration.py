str=input("Enter String \n")
dic={}
for i in str:
    dic[i]=str.count(i)
print(dic)