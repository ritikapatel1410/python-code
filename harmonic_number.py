num=int(input("enter the number: "))
string=""
for i in range(1,num+1):
    if(i<num):
        string+="1/"+str(i)+" + "
    else:
        string+="1/"+str(i)
print(string)

    