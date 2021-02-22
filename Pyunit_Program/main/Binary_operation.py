'''
 @Author: Ritika Patidar
 @Date: 2021-02-16 15:50:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-15 15:50:10  
 @Title : Binary operation problem
'''
import math
import logging
def Binary_operation(Dec_num):
    """
    it will convert Decimal value into Binary value and do following operation:
        i.Swap nibbles and find the new number.
        ii. Find the resultant number is the number is a power of 2

    Parameters:
            Dec_num (int): A int number
    Returns:
            Bin_nibble_dec (int): A int number
            power_of_two (boolean) : True or False

    """
    if(Dec_num<0):
        raise ValueError
    bin_convert=bin(Dec_num)[2:]
    eight_bit=len(bin_convert)%8
    if(eight_bit!=0):
        bin_convert="0"*(8-eight_bit)+bin_convert
    Bin_nibble=[bin_convert[nibble:nibble+4] for nibble in range(0,len(bin_convert),4)]
    changed_bin=""
    for nibble in range(0,len(Bin_nibble),2):
        changed_bin+=Bin_nibble[nibble+1]
        changed_bin+=Bin_nibble[nibble]
    Bin_nibble_dec=int(changed_bin,2)
    if(Bin_nibble_dec>1):
        Log2x=math.log10(Bin_nibble_dec)/math.log10(2)
        return (Bin_nibble_dec,math.ceil(Log2x) == math.floor(Log2x))
    else:
        return (Bin_nibble_dec,False)    

def main():
    """
    it's main function and responsible for call the Binary_operation function
    Parameters:
            None
    Returns:
            None
    Input:
        userinput (int) = ask to user for inter 
    """
    #Create and configure logger 
    logging.basicConfig(filename="/home/patidar/logger.log",level=logging.DEBUG,format='%(levelname)s:%(asctime)s:%(name)s:%(message)s') 
    #Creating an object 
    logger=logging.getLogger(__name__)
    while True:
        try:
            userinput=int(input("enter the decimal value int only :"))
            logger.debug("is converted output number {0} is power of 2? {1} ".format(Binary_operation(userinput)[0],Binary_operation(userinput)[1]))
            break
        except ValueError as error:
            logger.error("{0} occured".format(ValueError))

if __name__ == "__main__":
    main()



