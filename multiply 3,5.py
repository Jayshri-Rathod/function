def number_1(limit_name):
    i=1
    sum=0
    while i<=limit_name:
        if i%3==0 or i%5==0:
            print(i,end=" ")
            sum+=i
        else:
            pass
        i+=1
    print()
    print("sum of numbers",sum)
number_1(10)
