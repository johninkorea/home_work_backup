# import numpy as np
# from decimal import Decimal as D
# from time import *

# x=[1., 2., 3., 4.]
# y=[3., 5., 7., 9.]



# L=len(x)

# # def H(x, w, b):
# #     h=w*x+b
# #     return h



# def d_H_w(x, y, w, b):
#     a=D(2*(x**2)+2*x*b-2*x*y)
#     return a
# def d_H_b(x, y, w, b):
#     a=D(2*x*b-2*y+2*b)
#     return a


# # def cost(w, b):
# #     z=0
# #     C=0
# #     while z<L:
# #         a=(H(x[z]-y[z]))**2
# #         C+=a
# #         z+=1
# #     return C

# def d_cost_w(w, b):
#     z=0
#     C=0
#     while z<L:
#         a=D(d_H_w(x[z], y[z], w, b))**2
#         C+=a
#         z+=1
#     return C

# def d_cost_b(w, b):
#     z=0
#     C=0
#     while z<L:
#         a=D(d_H_w(x[z], y[z], w, b))**2
#         C+=a
#         z+=1
#     return C



# def M(f):
#     if f<0:
#         F=True
#     elif f>0:
#         F=False
#     else:
#         F=0
#     return F








# #변수 초기화
# w=1
# b=0
# h_w=0.1
# h_b=0.1
# A=bool
# B=bool


# while True:
#     if A!=True:
#         a=d_cost_w(w, b)    
#         if M(a)==False:
#             w=w+h_w
#             h_w=h_w*0.5
#         elif M(a)==True:
#             w=w-h_w
#             h_w=h_w*0.5
#         else: #M(a)==0
#             A=True
    

#     if B!=True:
#         alpha=d_cost_b(w,b)    
#         if M(alpha)==False:
#             b=b+h_w
#             h_b=h_b*0.5
#         elif M(alpha)==True:
#             b=b-h_w
#             h_b=h_b*0.5
#         else: #M(a)==0
#             A=True
    
#     print(f"{w}\t{b}\t{a}\t{alpha}")
    
#     if A==True and B==True:
#         break
#     else:
#         pass

#     # sleep(1)



# print("="*30)
# print("result")
# print(f"w:{w}")
# print(f"b:{b}")

# print(f"y={w}*x+{b}")















#가져 온거

import numpy as np

x_train = np.array([1., 2., 3., 4.])
y_train = np.array([3., 5., 7., 9.])

W = 0.0
b = 0.0

n_data = len(x_train)

epochs = 5000
learning_rate = 0.01

for i in range(epochs):
    hypothesis = x_train * W + b
    cost = np.sum((hypothesis - y_train) ** 2) / n_data
    gradient_w = np.sum((W * x_train - y_train + b) * 2 * x_train) / n_data
    gradient_b = np.sum((W * x_train - y_train + b) * 2) / n_data

    W -= learning_rate * gradient_w
    b -= learning_rate * gradient_b

    if i % 100 == 0:
        print('Epoch ({:10d}/{:10d}) cost: {:10f}, W: {:10f}, b:{:10f}'.format(i, epochs, cost, W, b))

print('W: {:10f}'.format(W))
print('b: {:10f}'.format(b))
print('result : ')
print(x_train * W + b)
