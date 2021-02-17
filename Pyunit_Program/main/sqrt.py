'''
 @Author: Ritika Patidar
 @Date: 2021-02-15 22:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-15 22:30:38  
 @Title : Computes the square root of a nonnegative number using Newton's method
'''
import logging
import math
def sqrt(c):
    '''
    Computes the square root of a nonnegative number c using Newton's method
            Parameters:
                    c (float): A float number
            Returns:
                    t (float): estimate of the square root of c
    '''
    epsilon=math.exp(-15)
    t=c
    while(abs(t - (c/t))>epsilon*t):
        t=(t+(c/t))/2
    return float("{0:.3f}".format(t))

def main():
    """ 
    it's main function of code
    o/p : print into logger file which located on /home/logger
    """
    logging.basicConfig(filename="/home/patidar/logger.log",level=logging.DEBUG,format='%(levelname)s:%(asctime)s:%(name)s:%(message)s') 
        #Creating an object 
    logger=logging.getLogger(__name__)
    try:
        while True:
            userinput=float(input("enter the positive number: "))
            if(userinput>0):
                break
            else:
                logger.debug("input is not as expected")
        logger.debug("the estimate of the square root of c: {0}".format(sqrt(userinput)))
    except Exception as error :
        logger.error("{0} occured input not as expected try again".format(error))
#main function    
if __name__ == "__main__":
    main()
