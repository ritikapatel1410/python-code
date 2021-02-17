'''
 @Author: Ritika Patidar
 @Date: 2021-02-12 21:52:29
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-12 21:52:29 
 @Title : Coupon number problem
'''
import random
def coupon_number_fun():
    try:
        total_coupon=int(input("enter number of coupon: "))
        coupon_check=[0 for coupon in range(total_coupon)]
        coupon_number=sorted([int(input("enter coupon number: ")) for coupon in range(total_coupon)])
        random_number_count=0
        print(coupon_number)
        while(all(coupon_check)==False):
            random_number=random.randint(coupon_number[0],coupon_number[total_coupon-1])
            random_number_count+=1
            if(random_number in coupon_number):
                for coupon_value in range(total_coupon):
                    if(random_number==coupon_number[coupon_value]):
                        coupon_check[coupon_value]=1
        print("{0} random count needed".format(random_number_count))
    except Exception as error:
        print("{0} error occured int input excepted try again".format(error))
        coupon_number_fun()
coupon_number_fun()