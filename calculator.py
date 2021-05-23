# def calculator(number_x,number_y,operation):
#     if operation=="add":
#         return number_x+number_y
#     elif operation=="substrct":
#         return number_x-number_y
#     elif operation=="multiply":
#         return number_x*number_y
#     else:
#         return number_x/number_y
# number_1=calculator(20,25,"add")
# number_2=calculator(50,60,"substract")
# number_3=calculator(80,120,"multiply")
# number_4=calculator(90,23,"devide")
# print(number_1)


number_x=int(input("enter number"))
number_y=int(input("enter number"))
def calculator(number_x,number_y,operation):
    if operation=="add":
        return number_x+number_y
    elif operation=="substrct":
        return number_x-number_y
    elif operation=="multiply":
        return number_x*number_y
    else:
        return number_x/number_y
add_result=calculator(number_x,number_y,"add")
substract_result=calculator(number_x,number_y,"substrct")
multiply_result=calculator(number_x,number_y,"multiply")
divide_result=calculator(number_x,number_y,"devide")
print(add_result)
print(substract_result)
print(multiply_result)
print(divide_result)

# def list_change(list1,list2):
#     i=0
#     a=[]
#     while i<len(list1):
#         a.append(list1[i]*list2[i])
#         i+=1
#         return a
# x=(list_change([5, 10, 50, 20], [2, 20, 3, 5]))
# print(x)






