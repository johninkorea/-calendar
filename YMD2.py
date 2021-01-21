
import math
import numpy as np

#input list 
YMD=[]

# Separate symbols and letters.
while True:
    YMD[0:]=input("Please enter the year and month dates in order. (Separated by Spaces)").split()
    
    y0=YMD[0].isdigit()              
    z0=YMD[0].isalpha()
    y1=YMD[1].isdigit()              
    z1=YMD[1].isalpha()
    y2=YMD[2].isdigit()              
    z2=YMD[2].isalpha()
    
    y=y0 or y1 or y2
    z=z0 or z1 or z2
    
    if y==True and z==False:   # break when all of input are numbers.
       break
    
    else:
        print("you have to enter numbers")   # print errer message

# take input to variable.
Y=int(YMD[0])
M=int(YMD[1])
D=int(YMD[2])



# calculate Julian Day
e=((M+9)/12)//1
f=(7*(Y+e)/4)//1
g=((275*M)/9)//1
h=np.sign(100*Y+M-190002.5)
JD=(367*Y-f+g+D+1721013.5-0.5*h+0.5)

# calculate day of week
W=JD%7//1    
DFW={1.:'wednes', 2.:'Thurs', 3.:'fri', 4.:'satur', 5.:'sun', 6.:'mon', 0.:'tues'}
W=DFW[W]

# print Day of week    
print(f"That day is {W}day.")


# calculate first day of month
JD0=(367*Y-f+g+1+1721013.5-0.5*h+0.5)
W0=JD0%7//1
print(f"The month that corresponds to the date you entered begins on {W0}day.")


# calculate if that year are leap year. 
m=[31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
if Y/400%1==0:
    m[1]=29
    print("The year is the leap year.")
elif Y/100%1==0:
    m[1]=28
    print("The year is the average year.")
elif Y/4%1==0:
    m[1]=29
    print("The year is the leap year.")
else:
    m[1]=28
    print("The year is the average year.")

print("Days per month in the year:",m)


#[일 월   화   수   목   금   토]
#[5 6   0   1   2   3   4]
#[0 1   2   3   4   5   6]

if W0==5 or W0==6:
    W0=W0-5
else:
    W0=W0+2



# print reult
print("\n","*"*40,"\nPrint calendar\nsun\tmon\ttue\twed\tthur\tfri\tsat")


# add zeros emty space
MF=[]
z=0
while z<W0:
    MF.insert(z,0)
    z+=1

# make day lost in one line
x=1
while x<m[M-1]+1:
    MF.append(x)
    x+=1


for k,v in enumerate(range(len(MF)),1):
    print("{}\t".format(MF[v]), end='\n' if k%7==0 else '  ' )

