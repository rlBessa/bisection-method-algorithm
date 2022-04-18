#---------------------------------------------------------
# Given a continuous function f:[a,b]->R, with f(a)*f(b) <= 0,
# this program,
# using the bisection method,
# returns a real root (or an approximate real root) for f,
# with maximum absolute error given by tol
#---------------------------------------------------------

import math
import numpy

def bisection(f,a,b,tol):
    if a >= b or tol<= 0:
        return('This procedure does not apply for a >= b or precision <= 0')
    elif f(a) == 0.0:
        return a
    elif f(b) == 0.0:
        return b
    elif numpy.sign(f(a)) == numpy.sign(f(b)):
        return('The function has no root in the range')
    else:
        n = int(math.ceil(math.log((b-a)/tol)/math.log(2)))+1     #associated with the theoretical estimate numberof iterations
        i = 1                                                    
        while i <= n:
            p = (a+b)/2
            if f(p) == 0.0 or (b-a)/2<tol:
                return p
            elif numpy.sign(f(a)) == numpy.sign(f(p)):
                a = p
            else:
                b = p
            i += 1
        return p
        

#---------------------------------------------------------
#                         Examples
#---------------------------------------------------------


# def f(x):
#     return x**3-20*x**2
# print(bisection(f,10,40,1.0e-15))

# def f(x):
#     return x**3+4*x**2-10
# y = bisection(f,1,2.0,1.0e-4)
# print(y)


#def f(x):
#    return -x**2+1
#y = bisection(f,-1.0,1.0,1.0e-4)
#print(y)

# def f(x):
#     return -x**2
# y = bisection(f,1.0,2.0,1.0e-4)
# print(y)
        
# def f(x):
#     return x - 2**(-x)
# y = bisection(f,0.0,1.0,1.0e-5)
# print(y)

# def f(x):
#     return x**3 - 25
# y = bisection(f,2.0,3.0,1.0e-5)      
# print(y)


# def f(x):
#     return numpy.sin(x)
# y = bisection(f,-0.5,1.5,1.0e-5)
# print(y)

# def f(x):
#     return numpy.sin(x)
# y = bisection(f,-0.5,1.5,2)
# print(y)

# def f(x):
#     return x**2-x
# print(bisection(f,1.0,0.0,1.0e-5))


