# from math import sin
# from math import cos
# from math import acos

# pir=acos(-1)

# '''
# a,b=map(float,input("x_s, x_f:").split())

# c=float(input("rmsdml:"))
# #print(a,b)
# '''
# def f(x):
#     y=sin(2*x)-2*pir*x+(pir)**2/2
#     # y=100/(2*3.14)*(x-0.1*sin(x))-50
#     return y
    
# def bisection (f, x_s, x_f):
#     m=(f(x_f)-f(x_s))/(x_f-x_s)
    
#     z=0
#     while z<1000:
        
#         x_m=(x_s+x_f)/2
        
        
#         if x_s==x_f:
#             x_s=x_f=x_m
#             break
            
            
            
            
#         elif m>0:
#             if f(x_m)>0:
#                 x_f=x_m
#             elif f(x_m)<0:
#                 x_s=x_m
#         elif m<0:
#             if f(x_m)>0:
#                 x_s=x_m
#             elif f(x_m)<0:
#                 x_f=x_m
        
#         print("{}\t{}\t{}\t".format(x_s,x_f, z))
#         z+=1
#     return x_s, x_f   


# x,y=bisection(f,0,2*pir)
# print("="*40)
# print(x,y)
# print((x+y)/2)






from math import sin
from math import cos
from math import acos
import numpy as np

pir=acos(-1)


h=(6.6*(10e-27))  #erg s
c=2.99793458*(10**(10))  #cm/s
# c=(2.99793458*(10e18))  #A/s
k=(1.3*(10e-16) )  #erg/K
e=(np.e)

T=(5800)



def f(x):
    # B=(2*h*(c**2))*(x**-5)/(e**((h*c)/(x*k*T))-1)
    # A=(h*c)/(x*k*T)
    # y=(1/5)*e**(A)/(e**(A)-1)-(1/A)

    y=

    return y
    
def bisection (f, x_s, x_f):
    m=(f(x_f)-f(x_s))/(x_f-x_s)
    
    z=0
    while z<100:
        
        x_m=(x_s+x_f)/2
        
        
        if x_s==x_f:
            x_s=x_f=x_m
            break
            
            
            
            
        elif m>0:
            if f(x_m)>0:
                x_f=x_m
            elif f(x_m)<0:
                x_s=x_m
        elif m<0:
            if f(x_m)>0:
                x_s=x_m
            elif f(x_m)<0:
                x_f=x_m
        
        print("{}\t{}\t{}\t".format(x_s,x_f, z))
        z+=1
    return x_s, x_f   


x,y=bisection(f,0.001,60000)
print("="*40)
print(x,y)
print((x+y)/2)

