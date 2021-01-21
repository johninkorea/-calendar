
import math
import numpy as np

def df (a):
    s=a//1
    return s



YMD=[]

while True:
    YMD[0:]=input("년도와 월 일을 순서대로 입력").split()
    
    y0=YMD[0].isdigit()              
    z0=YMD[0].isalpha()
    y1=YMD[1].isdigit()              
    z1=YMD[1].isalpha()
    y2=YMD[2].isdigit()              
    z2=YMD[2].isalpha()
    
    y=y0 or y1 or y2
    z=z0 or z1 or z2
    
    if y==True and z==False:                  #숫자를
       break
    
    else:
        print("정수로 입력해야합니다.")
        
Y=int(YMD[0])
M=int(YMD[1])
D=int(YMD[2])




e=df((M+9)/12)
f=df(7*(Y+e)/4)
g=df((275*M)/9)
h=np.sign(100*Y+M-190002.5)
JD=(367*Y-f+g+D+1721013.5-0.5*h+0.5)
W=JD%7//1

day_of_the_week={1.:'수', 2.:'목', 3.:'금', 4.:'토', 5.:'일', 6.:'월', 0.:'화'}

W=day_of_the_week[W]
    
print(f"해당 날은 {W}요일입니다.")


JD0=(367*Y-f+g+1+1721013.5-0.5*h+0.5)
W0=JD0%7//1
print(f"입력한 날짜에 해당하는 달은 {W}요일에 시작합니다.")

###########################################################
#윤년 계산

m=[31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if Y/400%1==0:
    m[1]=29
    print("해당년은 윤년이며")
elif Y/100%1==0:
    m[1]=28
    print("해당년은 평년이며")
elif Y/4%1==0:
    m[1]=29
    print("해당년은 윤년이며")
else:
    m[1]=28
    print("해당년은 평년이며")

print("해당 년에 월별 일수",m)


#[일 월   화   수   목   금   토]
#[5 6   0   1   2   3   4]
#[0 1   2   3   4   5   6]

if W0==5 or W0==6:
    W0=W0-5
else:
    W0=W0+2


print("\n","*"*40,"\n해당 날짜의 달력을 출력합니다\n일\t월\t화\t수\t목\t금\t토")
MF=[]
z=0
while z<W0:
    MF.insert(z,0)
    z+=1


x=1
while x<m[M-1]+1:
    MF.append(x)
    x+=1



#리스트를 해당월에대해 시작요일 부터 숫자를 채워서 마지막까지 한번에 리스트를 만들고
#일정하개 7번째 마다 줄을 띄울수있다면?
#리스트를 만들때 insert하던가 m[0:a]=insert(0), m[a:]insert(x)-->whil ansdmfh m[a]몃번째 달까지해서 대입쭉

for k,v in enumerate(range(len(MF)),1):
    print("{}\t".format(MF[v]), end='\n' if k%7==0 else '  ' )

