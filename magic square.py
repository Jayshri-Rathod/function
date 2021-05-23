def magic_square(): 

    def square():
        magic= [[8, 3, 4],
        [1, 5, 9],
        [6, 7, 2]]
        return magic
    a=square()   
    i=0
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    while i<len(a):
        row=0
        sum=0
        while row<len(a):
            sum+=a[i][row]
            row+=1
        print(sum)
        dignomal=0
        while dignomal<len(a):
            if i==dignomal:
                sum1+=a[i][dignomal]
            dignomal+=1
        col1=0
        while col1<1:
            sum2+=a[i][col1]
            col1+=1
        col2=1
        while col2<2:
            sum3+=a[i][col2]
            col2+=1
        col3=2
        while col3<len(a):
            sum4+=a[i][col3]
            col3+=1
        i+=1
    print(sum1)
    print(sum2)
    print(sum3)
    print(sum4)
    if sum==sum1==sum2==sum3==sum4:
        print("magic square")
    else:
        print('not a magic square')
magic_square()