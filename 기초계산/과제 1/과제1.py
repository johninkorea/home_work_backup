# 모듈 임포트
import numpy as np

# 파일 읽어 오기
with open("/home/yararal/python/com_mat_sci/기초계산/과제 1/cfa2.dat",'r') as ta:
    a=ta.readlines()  # a라는 개체에 순서대로 저장
    

del a[:11]    # 맨윗쪽에 불필요한 부분 지우기
calunms=a[0]   # 칼럼 이름 저장
del a[:2]   # 칼럼 지우기

# 함수 정의하기
km=3.0862e-19  #Mpc   # 1Mpc=1, 1s=1을 기준
H0=70*km  #/s/(Mpc)
def Vh(v):
    V=v*km
    D=V/H0
    if D<0:
        D=0
    return D
def RZ(Dec,d):
    Dec=Dec*np.pi/180
    R=float(d*np.cos(Dec))
    Z=float(d*np.sin(Dec))
    return R,Z

# 계산된 결과를 저장할 리스트 생성
R_list=[]
Z_list=[]
D_list=[]


# 작성할 파일 만들기
file=open("new_tabel.txt",'w')

# 칼럼 먼저 입력
file.write(" Name       RA       Dec     D\n")

# 0번째 줄부터 순차적으로 인덱싱및 계산 하기

no_v_data_error=0  # 속도가 비어있는 부분의 개수를 카운트 하기위한 인자
z=0
while z<len(a):
    if (a[z][31:36]=='     ' )   :  # 속도 부분이 비어있으면 넘기기(저장도 안하는것),  or (a[z][0:10]=='01124+0010') 만약 특정한 은하를 제거하려면 
        no_v_data_error+=1
        pass 
    else:
        a_list=[]    # 인덱싱한 정보를 담을 리스트
        a_list.append(a[z][:11])   # 은하이름
        a_list.append(a[z][11:19])  # 적경
        a_list.append(a[z][19:26])  # 적위
        a_list.append(a[z][31:36])  #속도
        
        # 계산 파트 #
        
        # 적경 계산하기
        RA_h=float(a_list[1][:2])
        RA_m=float(a_list[1][2:4])
        RA_s=float(a_list[1][4:])
        RA=RA_h*15+RA_m*15/60+RA_s*15/3600
        # 적위 계산하기
        if '-' in a_list[2]:
            Dec_d=float(a_list[2][0:3])
            Dec_m=float(a_list[2][3:5])
            Dec_s=float(a_list[2][5:7])
            alpha=1
        elif '+' in a_list[2]:
            Dec_d=float(a_list[2][0:3])
            Dec_m=float(a_list[2][3:5])
            Dec_s=float(a_list[2][5:7])
            alpha=4
        else:
            Dec_d=float(a_list[2][:2])
            Dec_m=float(a_list[2][2:4])
            Dec_s=float(a_list[2][4:6])
            alpha=2
        Dec=(Dec_d+Dec_m*15/60+Dec_s*15/3600)*((-1)**alpha)
        D=Vh(float(a_list[3]))
        R,Z=RZ(Dec, D)
        R_list.append(R)
        Z_list.append(Z)
        D_list.append(D)
        # 소수점 네자리까지 나오도록 설정
        #               이름                   적경                      적위                        거리
        file.write(f"{a_list[0]}"+"\t{0:06.4f}".format(RA)+"\t{0:08.4f}".format(Dec)+"\t{0:06.4f}\n".format(D))
    z+=1
    
#파일 닫기
file.close() 


# 결과 데이터가 누락 없이 정확하게 입력 되었는지 확인하기
with open("new_tabel.txt",'r') as ta:
    b=ta.readlines()
print("\n\n***결과 데이터가 누락 없이 정확하게 입력 되었는지 확인***\n")
print("들어온 모든 데이터수: ",len(a))
print("정제 후 저장하는 데이터 수: ",len(a)-no_v_data_error)
print("정제 후 저장된 데이터 수: ",len(b)-1)
print("no_v_data: ",no_v_data_error)

if len(a)-no_v_data_error==len(b)-1:
    print("데이터의 누락이나 초과가 없습니다.")

# 리스트를 어레이로 변환
R=np.array(R_list)
Z=np.array(Z_list)
D=np.array(D_list)

# 내림 차순으로 리스트를 만들어 D_list2에 대입
D_list2=np.sort(D)[::-1]
D_lank=D_list2[0:3] # 순위권 3개 인덱싱하여 저장

print("\n\n***데이터 중에서 가장 먼 은하의 1~3위는 다음과 같습니다.***\n")
print(f"{b[0]}")

z=0
while z<3:
    n,=(np.where(D==D_lank[z]))
    n=int(n)
    print(f"{b[n+1]}")  # 맨위에 칼런을 저장햇기대문에 +1
    z+=1

# 문제 3, 마스킹하기
# 델타(적위)의 범위는 -pi<=적위<=+pi이고 D>0이다.
# R(=D*cos)은 양의 값을, Z(=D*sin)은 양과 음의 값을 둘 다 가진다.\
# 그런데 문제에서 북반구 하늘이라고했으므로 델타>0이다
# 즉, Z=D*sin(Dec)>0이라는 조건이 필요하다.
mask1=(R<150)
mask2=(0<Z)&(Z<50)
mask=mask1*mask2  #F*F=F, F*T=F, T*T=T
mask=list(mask)

print("\n\n***문제 3번에서 조건을 만족하는 은하의 수는 다음과 같습니다.***\n")
print("결과: ",mask.count(1))