print("Making a function for the area of a Circle")
def area_of_circle(r):
    m = str(input("are you measuring in cm or m: "))
    if m =="cm":
        n =  "cm"
    elif m =="m":
        n =  "m"
    else:
        print("Please pick either cm or m")
        area_of_circle(r)
    area =  3.14 * (r **2)
    return ("The area of the circle is %d{}". format(n) %(area))
radius = int(input("What is the radius of the circle you would like to find it area\n "))
print(area_of_circle(radius))
