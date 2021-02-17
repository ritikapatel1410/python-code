'''
 @Author: Ritika Patidar
 @Date: 2021-02-14 17:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-14 8:40:38  
 @Title : vending machine problem
'''
import logging 
# fun for change money
def vending_machine(money,total_change,return_money):
    """
    this function define for vending machine logic and it will return total money in dictionary format
    """
    counter=0
    if((money//total_change[counter])>0):
        change=money//total_change[counter]
        money=money-(change*total_change[counter])
        return_money[total_change[counter]]=change
    if(money!=0):
            total_change=total_change[1:]
            vending_machine(money,total_change,return_money)
    return return_money

def main():
    """
   this is main function in this take input from user and call vending-machine and return number of notes needed      
    """
    return_money=dict() 
    while True:
        try:
            money=int(input("enter money: "))
            logger.info("code working as expected")
            break
        except Exception as error:
            logger.error(error)

    total_change=[1000,500,100,50,10,5,2,1]
    return_change=vending_machine(money,total_change,return_money)
    final_return=["X".join([str(key),str(value)]) for key,value in return_change.items()]
    logger.debug("return money is: {0}".format(final_return))

#main function    
if __name__ == "__main__":
        #Create and configure logger 
    logging.basicConfig(filename="/home/patidar/logger.log",level=logging.DEBUG,
                        format='%(levelname)s:%(asctime)s:%(name)s:%(message)s') 
    #Creating an object 
    logger=logging.getLogger(__name__)
    main()
