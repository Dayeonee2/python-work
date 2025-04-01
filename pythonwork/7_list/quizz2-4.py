data = '''3 23 85 34 17 74 25 52 65
10 7 39 42 88 52 14 72 63
87 42 18 78 53 45 18 84 53
34 28 64 85 12 16 75 36 55
21 77 45 35 28 75 90 76 1
25 87 65 15 28 11 37 28 74
65 27 75 41 7 89 78 64 39
47 47 70 45 23 65 3 41 44
87 13 82 38 31 12 29 29 80'''

data = data.replace('\n', ' ') #줄바꿈 공백으로 대치
ls = data.split(' ')
ls2 = []
temp = []
maxNum = []

for i in range(0,len(ls),9): #9개씩 잘라서 행렬list로 정렬
    for j in range(9):
        temp.append(ls[i+j])
    ls2.append(temp)
    temp = []  
for i in range(len(ls2)):
    print(ls2[i])
    
import copy
#최댓값 찾기-----------------------------------------
ls3 = copy.deepcopy(ls2)  #깊은복사: 정렬하여 최댓값 찾기위함
for a in range(len(ls3)):
    ls3[a].sort(reverse=True)  #오름차순정렬
    ls3[a] = ls3[a]
    maxNum.append(ls3[a][0])
maxNum.sort(reverse=True) #오름차순 정렬

#인덱스 값 찾기--------------------------------------
indexNum = []
for i, row in enumerate(ls2):  #행
    for j, num in enumerate(row):  #열
        if num == maxNum[0]:
            indexNum.append((i,j))
            

#결과출력--------------------------------------------
print(f'최댓값: {maxNum[0]}')

for i in range(len(indexNum)):  #중복 값 존재할 경우 고려
    print(f'최댓값의 위치: {indexNum[i][0]+1}행 {indexNum[i][1]+1}열')