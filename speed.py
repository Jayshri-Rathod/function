def drivers_speed(speed):
    a=int((speed-70)/5)
    if a>=12:
        print("points",a,"is greater than 12")
        print("license suspend")
    elif speed>70:
        a=int((speed-70)/5)
        print("point",a)
    else:
        print("ok")
drivers_speed(65)
        
   

