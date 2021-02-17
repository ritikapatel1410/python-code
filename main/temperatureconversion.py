'''
 @Author: Ritika Patidar
 @Date: 2021-02-15 18:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-15 18:30:38  
 @Title : Temperature conversion problem
'''
import logging 
class Temp_conv:
    """
    it will convert temperature f to c or c to f depends on user choice and return converted temperature 
    """
    def __init__(self,temp):  
        self.temp=temp
    def fahrenheit(self):
        f=self.temp*(9/5) + 32
        return float("{0:.3f}".format(f))
    def celsius(self):
        c=(self.temp-32)*5/9
        return float("{0:.3f}".format(c))

def main():
    """
    it's main function in this Temp_conv will call and print o/p in logger file 
    """
    logging.basicConfig(filename="/home/patidar/logger.log",level=logging.DEBUG,format='%(levelname)s:%(asctime)s:%(name)s:%(message)s') 
    #Creating an object 
    logger=logging.getLogger(__name__)
    while True:
        try:
            user_input=float(input("enter the temp: "))
            user_choice=int(input("enter 0 for convert into celsius and 1 for convert into degree: "))
            if(user_choice==0 or user_choice==1):
                break
            else:
                logger.debug("you entered {0} insted of 0 or 1:".format)
        except ValueError as error:
            logger.error(error)
    Temperature=Temp_conv(user_input)
    if(user_choice==0):
        logger.debug("temerature in celsius: {0}".format(Temperature.celsius()))
    else:
        logger.debug("temerature in fahrenheit: {0}".format(Temperature.fahrenheit()))

#main function    
if __name__ == "__main__":
    main()

