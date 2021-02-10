import random
number=int(input("enter the number: "))
head=0
tail=0
n=number
while n!=0:
    if(random.randint(0, 1)==0):
        head+=1
    else:
        tail+=1
    n-=1
print("Head: ", ((head/number)*100))
print("Tail: ", ((tail/number)*100))