import math

def ex1():
    height = int(input("Enter height: "))
    base = int(input("Enter base: "))

    return (0.5 * base * height)

def ex2():
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))

    return(a + b + c)

def ex3():
    length = int(input("Enter length: "))
    width = int(input("Enter width: ")) 
    
    return [length * width, 2 * (length + width)] # area, perimeter

def ex4():
    radius = int(input("Enter radius: "))
    pi = 3.14
    return [pi * radius * radius, 2 * pi * radius] # area, circumference

def ex5():
    #y = 2*x - 2
    #x = 2*y - 2
    #Ham slope = y = 1/2*x + 1

    slope = 1/2
    b = 1
    
    #when y = 0
    if b > 0:
        x_intercept = -b/slope
    else: 
        x_intercept = b/slope

    #when x = 0
    y_intercept = slope*0 + b

    return [x_intercept, y_intercept]

def ex6():
    #Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
    x = [2, 2]
    y = [6, 10]

    slope = (y[1]-y[0]) / (x[1]-x[0])
    euclid_dist = math.sqrt(pow(x[1]-x[0], 2) + pow(y[1]-y[0], 2))
    return [slope, euclid_dist]

def ex7(slop1, slop2):
    if slop1 > slop2:
        return 'slope cua bai 5 lon hon cua bai 6'
    elif slop1 < slop2:
        return 'slope cua bai 5 nho hon cua bai 6'
    else:
        return 'slop cua 2 bai la bang nhau'
    
def ex8():
    x = int(input("Enter x: "))
    y = pow(x,2) + 6*x + 9
    return y

def ex9():
    len1 = len('python')
    len2 = len('dragon')

    return not len1 == len2

def ex10():
    return ('on' in 'python') and ('on' in 'dragon')

def ex11(sentence):
    return 'jargon' in sentence

def ex13(text):
    len_txt = len(text)
    fl_txt = float(len_txt)
    str_txt = str(fl_txt)

    return str_txt

def ex14(num):
    return num%2==0

def ex15():
    h = int(input("Enter hour(s): "))
    rate_per_h = int(input("Enter rate per hour(s): "))
    return h*rate_per_h

def ex16():
    yearold = int(input("Enter years: "))
    return yearold * 365 * 24 * 60 * 60 #seconds

sentence = 'I hope this course is not full of jargon'
print(ex11(sentence))