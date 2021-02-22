'''
 @Author: Ritika Patidar
 @Date: 2021-02-10 17:50:30
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-13 10:20:40 
 @Title : count triplet sum zero problem
'''
while True:
    try:
        user_input=int(input("enter the number of element: "))
        input_array=[int(input("enter int element of array: ")) for i in range(user_input)]
        print("input array is: ", input_array)
        sum_zero_count=0
        for input_array_index_i in range(user_input-2):
            for input_array_index_j in range(input_array_index_i+1,user_input-1):
                for input_array_index_k in range(input_array_index_j+1,user_input):
                    if(input_array[input_array_index_i]+input_array[input_array_index_j]+input_array[input_array_index_k]==0):
                        print(input_array[input_array_index_i],input_array[input_array_index_j],input_array[input_array_index_k])
                        sum_zero_count+=1
        print("triplet zero sums are: ",sum_zero_count)
        break
    except ValueError:
        print("enter only int number try again !!")


