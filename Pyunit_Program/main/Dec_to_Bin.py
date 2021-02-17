'''
 @Author: Ritika Patidar
 @Date: 2021-02-15 23:40:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-15 23:40:10  
 @Title : Decimal to binary conversion 
'''
import logging
def toBinary(Dec_num):
    '''
    it's define for binary to decimal conversion
            Parameters:
                   Dec_num (float): A float number
            Returns:
                    bin sormat string (string): contain converted binary number
    '''    
    bin_float=[]
    int_part,float_part=str(Dec_num).split(".")
    bin_int_part=bin(int(int_part))[2:]
    float_part=float("."+float_part)
    while(float(float_part)!=0.0 and len(bin_float)<=8):
        intial_float_part=float_part
        float_part_bin=float(float_part)*2
        float_part=float_part_bin-int(float_part_bin)
        bin_float.append(str(int(float_part_bin)))
        if(intial_float_part==float_part):
            break 
    if len(bin_float)>0:
        return ("0"*(24-(len(bin_int_part)))+str(bin_int_part)+"."+"".join(bin_float)+"0"*(8-len(bin_float)))
    else:
        return ("0"*(32-(len(bin_int_part)))+str(bin_int_part))


def main():
    '''
    it's main function of the code
            Parameters:
                    None
            Returns:
                    None
    it's output will log into logger.log which path is /home/patidar/looger.log
    '''
    logging.basicConfig(filename="/home/patidar/logger.log",level=logging.DEBUG,format='%(levelname)s:%(asctime)s:%(name)s:%(message)s') 
    #Creating an object 
    logger=logging.getLogger(__name__)
    while True:
        try:
            userinput=float(input("enter the decimal value: "))
            logger.debug("{0} binary conversion is {1}".format(userinput,toBinary(userinput)))
            break
        except ValueError as error:
            logger.error("{0} occured input is not as expected!!".format(error))

if __name__ == "__main__":
    main()

            







