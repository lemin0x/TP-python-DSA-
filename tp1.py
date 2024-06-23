def doubleVAlue(x):
    x *= 2
    return x
doubleVAlue(5)

def appendlst(lst, value):
    lst.append(value)
    return lst

def modifylst(lst):
    lst[:] = [1, 2, 3]
    return None

x = [4, 5,76 ,5]

# print(modifylst(x))


def swap(a, b):
   a , b = b ,a 
   return a ,b 


# print(swap(5,6))



def max2(x, y):
    if x > y:
        return x
    else :
        return y

def max3(x, y, z):
    mn = max2(x, y)
    return max2(mn, z)

print(max3(14, 15, 23))


def max4(x, y, z):
    if x > y and y >  z :
        return x
    elif y > x  and y > z:
        return y
    else :
        return z
    

# print(max4(414, 223, 124))

# def f(n):
#     if n == 0:
#         return 1
#     else :
#         return n * f(n-1)
# print(f(5))

# import math

# print(math.factorial(5))

def divs(x):
    d = []
    for i in range (1, x):
        if x % i == 0:
            d.append(i)
    return d[::-1]
    
# print(divs(8))

def somD(x):
    return sum(divs(x))

print(somD(8))