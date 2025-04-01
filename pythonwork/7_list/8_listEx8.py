ls = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

# 일차원 list - for 문으로 반복
# 이차원 list - 이중 for문으로 반복
# 외부 for문 1번 돌때 내부 for문 시작 ~ 끝까지 진행
# 외부 for문 행을 의미
# 내부 for문 열을 의미
for i in range(len(ls)): #행
    for j in range(len(ls[i])):
        print(f'ls[{i}][{j}] : {ls[i][j]}',end='\t');
    print()