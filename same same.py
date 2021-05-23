# def menu(day):
#     if day == "monday":
#         food = "Butter Chicken"
#     elif day == "tuesday":
#         food = "Mutton Chaap"
#     else:
#         food = "Chole Bhature"
#     print ("Kya main print ho payungi? :-(")
#     return food
#     print ("Lekin main toh pakka nahi print hounga :'(")
# print(menu("monday")) 





def menu(day):
    if day == "monday":
        return "Butter Chicken"
    elif day == "tuesday":
        return "Mutton Chaap"
    else:
        return "Chole Bhature"
    print ("Kya main print ho payungi? :-(")    
    

mon_menu = menu("monday")
print (mon_menu)
tues_menu = menu("tuesday")
print (tues_menu)
fri_menu = menu("friday")
print (fri_menu) 