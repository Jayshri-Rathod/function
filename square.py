def square_number(numbers):
    i=1
    a={}
    while i<=numbers:
        a.update(i,i)
        print(i,":",i**2, end=", ")
        i+=1
square_number(20)