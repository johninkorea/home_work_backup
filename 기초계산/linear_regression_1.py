import numpy as np
# from decimal import Decimal as D



#변수 먼저 결정
dot=10000     #점갯수
h=0.1       #미소 미분


# 가정 시작
w=1.000011
b=0

#불특정 점을 찍어서 dat파일로 저장
# np.random.seed(829551)
# x=np.linspace(0,10, num=dot)
# y=np.linspace(0,10, num=dot)
x=np.random.rand(dot)*10
y=np.random.rand(dot)*10

file=open("asd.dat", 'w')
z=0
while z<dot:
    file.write(f"{x[z]}\t{y[z]}\n")
    z+=1
file.close()


# 점 잘 나왔는지 확인
'''
print(x)
print(y)
print(len(x))
print(len(y))
'''

def f(x, w, b): #일단 가정한 함수
    y=w*(x)+b
    return y

def cost(w, b):  #손실함수
    z=0
    sum=0
    while z<dot:
        cost_n=(f(z, w, b)-y[z])**2
        sum+=cost_n
        z+=1
    return sum



# 먼저 기울기(w)를 변화해보자

def m(w, h):  # cost(w) 함수의 기울기 구하기
    asd=np.sign((cost(w+h, b)-cost(w, b))/(h))
    return asd

m_list=[m(w-h,h)]  
# 기울기가 0인 지점을 찾으면서 0을 지날때
# h의 간격을 줄이면서 정확도를 높일것이다.
# 다라서 전의 기울기와 비교를 해야하므로 리스트를 만들어준다

z=1
while True:
    a=m(w, h)
    m_list.append(a)
    
    if (m_list[z]*m_list[z-1])<0:
        h=h*0.5 #구간을 좁히는 부분
    if a<0:
        w+=h
    elif a>0:
        w-=h
    if a==0:
        break
    print(f"{w}\t{a}")
    z+=1

# print(m_list)
print(w)





x_mean=np.mean(x)
y_mean=np.mean(y)
print(x_mean, y_mean)


# 미소 단위를 보고 미분을  하는데 이때 0이 되지 않아 코드가 먼추지를 않는다 그래서
# 미분된 식을 적용해보도록 하자
# 그리고 w뿐아니라 b의 갑도 루프에 얺어 같이 수정해보자

































