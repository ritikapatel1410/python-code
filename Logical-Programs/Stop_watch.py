'''
 @Author: Ritika Patidar
 @Date: 2021-02-12 21:28:29
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-12 21:28:29 
 @Title : Gambler problem
'''
def stop_watch():
    try:
        start_time=input("enter start time in HH:MM:SS format: ")
        end_time=input("enter end time in HH:MM:SS format: ")
        start_time_split=list(map(int,start_time.split(":")))
        end_time_split=list(map(int,end_time.split(":")))
        start_time_second=start_time_split[0]*3600+start_time_split[1]*60+start_time_split[2]
        end_time_second=end_time_split[0]*3600+end_time_split[1]*60+end_time_split[2]
        if(end_time_second>start_time_second and (start_time_split[0]<24 and start_time_split[0]>=0)and(start_time_split[1]<60 and start_time_split[1]>=0)and(start_time_split[2]<60 and start_time_split[2]>=0)and(end_time_split[0]<24 and end_time_split[0]>=0)and(end_time_split[1]<60 and end_time_split[1]>=0)and(end_time_split[2]<60 and end_time_split[2]>=0)):
            elapse_time_second=end_time_second-start_time_second
            elapse_time_hour=(elapse_time_second/3600)
            elapse_time_minute=(elapse_time_second%3600)/60
            elapse_time_second=(elapse_time_second%3600)%60
            print("elapse_time %02d:%02d:%02d" %(int(elapse_time_hour),int(elapse_time_minute),int(elapse_time_second)))
        else:
            print("expected future time greater then present time and 24 hours format try again")
            stop_watch()
    except Exception as error:
        print("{0} error occured expected HH:MM:SS time format try again".format(error))
        stop_watch()
stop_watch()
