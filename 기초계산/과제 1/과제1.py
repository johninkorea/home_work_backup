# 모듈 임포트
import numpy as np

# 파일 읽어 오기
with open("/home/yararal/python/com_mat_sci/기초계산/과제 1/cfa2.dat",'r') as ta:
    a=ta.readlines()
    

del a[:11]    # 맨윗쪽에 불필요한 부분 지우기
calunms=a[0]   # 칼럼 이름 저장
calunms=calunms.split()
del a[:2]   # 칼럼 지우기


# 거리 구하는 함수 정의   1Mpc=1, 1s=1
km=3.0862e-19  #Mpc
H0=70*km  #/s/(Mpc)
def Vh(v):
    V=v*km
    D=V/H0
    if D<0:
        D=0
    return D
# 실린더 좌표 구하기
def RZ(ra,dec,d):
    R=float(d*np.cos(ra))
    Z=float(d*np.sin(dec))
    return R,Z
# 실린더 좌표계에서 인덱싱을 해야히기때문에 담을 시스트를 만든다
R_list=[]
Z_list=[]
D_list=[]

# 파일 만들엇 작성하기
file=open("new_tabel.txt",'w')

# 칼럼 먼저 입력
# file.write(f"{calunms[0]}\t{calunms[1]}\t\t{calunms[3]}\t\t{calunms[5]}\n")

# 0번째 줄부터 순차적으로 인덱싱 및 좋지 않은 데이터 지우고 계산 하기
print("기존에 cfa2.dat에서 데이터를 구분한결과")
z=0
while z<len(a):
    if (a[z][31:36]=='     ' ) or (a[z][0:10]=='01124+0010') :  # 속도 부분이 비어있으면 넘기기(저장도 안하는것)
        # print(z+14,end=',')
        pass 
    else:
        a_list=a[z].split()    # 하나의 줄에서 띄어쓰기로 분리하기
        if len(a_list[0])>11:  # 앞에 이름이 길어서, 특정 길이 이상이면 순서대로 자름; 근데 여기서 N이 방향인가?
            a1,a2=a_list[0][:11],a_list[0][11:]
            a_list[0]=a1
            a_list.insert(1,a2)
        if len(a_list[0])<2:  # 이름이 잛고 쪼개진거 다시 붙이기
            a_list_alpha=a_list
            a_list[0]=a_list_alpha[0]+a_list_alpha[1]
            a_list[1]=a_list_alpha[2]
            a_list[2]=a_list_alpha[3]
            a_list[3]=a_list_alpha[4]
        if  '-' in a_list[1]:  #좌표중에 -기호가 듸어쓰기가 안되어있음; 이거뜯기
            a3,a4=a_list[1][:8],a_list[1][8:]
            a_list[1]=a3
            a_list.insert(2,a4)
        if  '+' in a_list[1]:  #좌표중에 -기호가 듸어쓰기가 안되어있음; 이거뜯기
            a3,a4=a_list[1][:8],a_list[1][8:]
            a_list[1]=a3
            a_list.insert(2,a4)
        if len(a_list[2])>11:  # 앞에 이름이 길어서, 특정 길이 이상이면 순서대로 자름;
            a5,a6=a_list[2][:11],a_list[2][11:]
            a_list[2]=a5
            a_list.insert(3,a6)
        

        # 변환전         이름          적경          적위       시선속도(km/s)
#         file.write(f"{a_list[0]}\t{a_list[1]}\t{a_list[2]}\t{a_list[3]}\n") # 파일에 작성

        # 계산 파트
        # 적경 계산하기
        RA_h=float(a_list[1][:2])
        RA_m=float(a_list[1][2:4])
        RA_s=float(a_list[1][4:])
        RA=RA_h*15+RA_m*15/60+RA_s*15/3600
        # 적위 계산하기
        if '-' in a_list[2]:
            Dec_d=float(a_list[2][:3])
            Dec_m=float(a_list[2][3:5])
            Dec_s=float(a_list[2][5:7])
        else:
            Dec_d=float(a_list[2][:2])
            Dec_m=float(a_list[2][2:4])
            Dec_s=float(a_list[2][4:6])
        Dec=Dec_d+Dec_m*15/60+Dec_s*15/3600

        D=Vh(float(a_list[3][:7]))

        #               이름       적경    적위   거리
        file.write(f"{a_list[0]}\t{RA}\t{Dec}\t{D}\n") # 파일에 작성
        R,Z=RZ(RA, Dec, D)
        R_list.append(R)
        Z_list.append(Z)
        D_list.append(D)
    z+=1
    
#파일 닫기
file.close() 



print("모든 데이터 수: ",len(a))
print("정제 후 데이터 수: ",len(R_list))
print("정제되어 없어진 데이터 수: ",len(a)-len(R_list))




with open("new_tabel.txt",'r') as ta:
    b=ta.readlines()
len(b)




R=np.array(R_list)
Z=np.array(Z_list)
D=np.array(D_list)


# 오름 차순으로 리스트를 만들어 D_list2에 대입
np.sort(D)
D_list2=np.sort(D)[::-1]
D_lank=D_list2[0:3] # 순위권 3개 인덱싱




print("\n","="*30)


print("정제된 데이터에서 가장 먼 은하 1~3위는 다음과 같습니다.")
z=0
while z<3:
    n,=(np.where(D==D_lank[z]))
    n=int(n)
    print(f"{int(n)}\t번째 데이터 이름 :{b[n].split()[0]}, 속도: {b[n].split()[3]}\t(Mpc/s)")
    z+=1
    

# R과 Z중에서 원하는 기준으로 마스킹
mask1=(R>150)
mask2=(0<Z)&(Z<50)
mask=mask1*mask2
mask=list(mask)

# mask에서 1의 갯수를 할수없으니 where함수로 1의 위치를 찾아서 그의 길이를 계산해보려했지만 불가능.....


print("\n","="*30)
print(f"문제에 주어진 기준에 맞는 은하는 {mask.count(1)}개입니다.")

