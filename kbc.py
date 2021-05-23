# def kbc():

#     def question():

#         question_list = ["1.How many continents are there?",
#         "2.What is the capital of India?",
#         "3.NG mei kaun se course padhaya jaata hai?"]
#         return question_list
#     que=question()

#     def option():

#         options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],
#         ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
#         ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
#         return options_list
#     opt=option()

#     def solution():

#         solution_list = [3, 4, 1]
#         return solution_list
#     sol=solution()

#     def answer():
#         answer_list=[["(1)Four","(3)Seven",],
#         ["(2)Bhopal","(4)Delhi"],
#         ["(1)software engineering","(3)Tourism"]]
#         return answer_list
#     ans=answer()

#     print("-:WELCOME TO KBC GAME:-")
#     print()
#     i=0
#     sum=0
#     count=0
#     while i<len(que):
#         print(que[i])
#         j=0
#         a=i
#         while j<len(opt[i]):
#             print(opt[a][j])
#             j+=1
#         if count<1:
#             num=input("do you want 5050 lifeline?")
#             if num=="yes":
#                 print(ans[i])
#                 ans=int(input("enter your option number"))
#                 if ans==sol[i]:
#                     sum+=10000
#                     print("Congratualation, your answer is correct")
#                     print("you won Rs/",sum)
#                 else:
#                     print("your answer is wrong")
#                     print("Sorry, you can't play now")
#                     print("you won Rs/",sum)
#                     break
#                 count+=1
#             else:
#                 pass
#                 ans=int(input("enter your option number"))
#                 if ans==sol[i]:
#                     sum+=10000
#                     print("Congratualation, your answer is correct ")
#                     print("you won Rs/",sum)
#                 else:
#                     print("your answer is wrong")
#                     print("Sorry, you can't play now")
#                     print("you won Rs/",sum)
#                     break
#         else:
#             pass
#             ans2=int(input("enter your answer number"))
#             if ans2==sol[i]:
#                 sum+=10000
#                 print("Congratualation, your answer is correct ")
#                 print("you won Rs/",sum)
#             else:
#                 print("your answer is wrong")
#                 print("Sorry, you can't play now")
#                 print("you won Rs/",sum)
#                 break
#         i+=1
#     print("Thank you for playing game with me.")
# kbc()



def kbc():

    def question():

        question_list = ["1.How many continents are there?",
        "2.What is the capital of India?",
        "3.NG mei kaun se course padhaya jaata hai?"]
        return question_list
    que=question()

    def option():

        options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],
        ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
        ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
        return options_list
    opt=option()

    def solution():

        solution_list = [3, 4, 1]
        return solution_list
    sol=solution()

    def answer():
        answer_list=[["(1)Four","(3)Seven"],
        ["(2)Bhopal","(4)Delhi"],
        ["(1)software engineering","(3)Tourism"]]
        return answer_list
    ans=answer()

    print("-:WELCOME TO KBC GAME:-")
    print()
    i=0
    sum=0
    count=0
    while i<len(que):
        print(que[i])
        j=0
        a=i
        while j<len(opt[i]):
            print(opt[a][j])
            j+=1
        if count<1:
            num=input("do you want 5050 lifeline?")
            if num=="yes":
                k=0
                while k<len(ans[i]):
                    print(ans[a][k])
                    k+=1
                num1=int(input("enter your option number"))
                if num1==sol[i]:
                    sum+=10000
                    print("Congratualation, your answer is correct")
                    print("you won Rs/",sum)
                else:
                    print("your answer is wrong")
                    print("Sorry, you can't play now")
                    print("you won Rs/",sum)
                    break
                count+=1
            else:
                pass
                num2=int(input("enter your option number"))
                if num2==sol[i]:
                    sum+=10000
                    print("Congratualation, your answer is correct ")
                    print("you won Rs/",sum)
                else:
                    print("your answer is wrong")
                    print("Sorry, you can't play now")
                    print("you won Rs/",sum)
                    break
        else:
            pass
            num3=int(input("enter your answer number"))
            if num3==sol[i]:
                sum+=10000
                print("Congratualation, your answer is correct ")
                print("you won Rs/",sum)
            else:
                print("your answer is wrong")
                print("Sorry, you can't play now")
                print("you won Rs/",sum)
                break
        i+=1
    print("Thank you for playing game with me.")
kbc()