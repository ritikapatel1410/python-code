'''
 @Author: Ritika Patidar
 @Date: 2021-02-12 21:28:29
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-12 21:30:29 
 @Title : Stop watch problem
'''
import time

def stop_watch():
    try:
        start_time=input("press enter for start stop watch: ")
        start_time=time.time()
        end_time=input("press enter for stop stop watch: ")
        end_time=time.time()
        elasped_time=end_time-start_time
        hours = elasped_time//3600
        minutes = (elasped_time%3600)//60
        seconds = ((elasped_time%3600)%60)
        print('%02d:%02d:%02d' %(hours,minutes,seconds))        
    except Exception as error:
        print("{0} error occured expected HH:MM:SS time format try again".format(error))
        stop_watch()
stop_watch()
