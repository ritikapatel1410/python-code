'''
 @Author: Ritika Patidar
 @Date: 2021-02-15 18:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-15 18:30:38  
 @Title : Monthly payment problem
'''
import logging
import sys 
def Monthlypayment_calulation(P,Y,R):
    n=12*Y
    r=R/(100*12)
    payment=P*r/(1-(1+r)**(-n))
    return float("{0:.3f}".format(payment))

def main():
    """
    it is main funnction which is responsible for input, call the class and return the final o/p
    """
    try:
        #Create and configure logger 
        logging.basicConfig(filename="/home/patidar/logger.log",level=logging.DEBUG,format='%(levelname)s:%(asctime)s:%(name)s:%(message)s') 
        #Creating an object 
        logger=logging.getLogger(__name__)
        Y=float(sys.argv[1])
        R=float(sys.argv[2])
        P=float(sys.argv[3])
        if(Y>0 and R>0 and P>0):
            logger.info("code working properly")
            logger.debug("Monthly payment: {0}".format(Monthlypayment_calulation(P,Y,R)))
        else:
            logger.debug("input is not as expected")
    except ValueError as error:
        logger.error("{0} occured try again!! ".format(error))
    except IndexError as error:
        logger.error("{0} occured try again!! ".format(error))

#main function    
if __name__ == "__main__":
    main()            

