add=[[],[],[],[],[],[],[],[],[]]
import random
for i in range(9):
    for j in range(9):
        add[i].append(random.randrange(1,100))
        #랜덤하게 91개 뽑기
print()
for i in range(len(add)):
    print(add[i]);#9*9로 출력
    
add_=[] # 각 인덱스 마다의 max값
for i in range(len(add)):
    max1=max(add[i])
    add_.append(max1)
print(f"각 행의 max 값 : {add_}")
print()
print(f"전체 행열의 max 값 : {max(add_)}")# 전체 max 값
print()
for i in range(len(add[i])):
    for j in range(len(add[i])):
        if max(add_) ==add[i][j]:
            print(f"max 값은 {i+1} 행 {j+1} 열")
print()
minus_=[]
for i in range(len(add)):
    min1=min(add[i])
    minus_.append(min1)
print()
print(f"각 행의 min 값 : {minus_}")
print()
print(f"전체 행열의 min 값 : {min(minus_)}")