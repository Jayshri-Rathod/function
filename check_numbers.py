# def check_numbers(num1,num2):
#     if num1%2==0 and num2%2==0:
#             print("Dono numbers even hai")
#     else:
#         print("Dono numbers odd hai")
# check_numbers(7,6)

def check_numbers_list(list1,list2):
    i=0
    j=0
    while i<len(list1):
        if list1[i]%2==0 and list2[i]%2==0:
            print("Dono numbers even hai")
        else:
            print("Dono even nahi hai")
        j+=1
        i+=1
check_numbers_list([2, 6, 18, 10, 3, 75] ,[6, 19, 24, 12, 3, 87])
