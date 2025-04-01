#민정언니 풀이
numData='''3 23 85 34 17 74 25 52 65
10 7 39 42 88 52 14 72 63
87 42 18 78 53 45 18 84 53
34 28 64 85 12 16 75 36 55
21 77 45 35 28 75 90 76 1
25 87 65 15 28 11 37 28 74
65 27 75 41 7 89 78 64 39
47 47 70 45 23 65 3 41 44
87 13 82 38 31 12 29 29 80'''

# 문자 데이터를 숫자 데이터 리스트로 정제하기
numList=numData.split("\n")  #줄바꿈 기호 제거
dataLst=[]  # 전체 리스트

#숫자 사이 공백제거
for i in numList:
    dataLst.append(i.split(" "))     

#형변환 (문자에서 정수로 변환)
for data in dataLst:
    for idx, val in enumerate(data):
        val=int(val)
        data[idx]=val
print(data)
#깊은 복사
dataLst_copy=dataLst.copy()

#---------------------
#내부의 각 리스트 값들 중 가장 큰 값을 비교
column_max=[]  #각 행의 큰 수만 모은 리스트
for data in dataLst:
    new_data=data.copy()   #리스트 값 복사
    data.sort(reverse=True)   #리스트 내부 값 내림차순 정렬
    column=new_data.index(data[0])   #몇 열의 값이 최댓값인지 알 수 있다.
    column_max.append([column+1,data[0]])

print(f'큰 숫자 list(column,max number): {column_max}')


row=[]  #행 별 가장 큰 숫자를 알아낼 리스트
for i in column_max:
    row.append(i[1])
row_max=row.copy()
row.sort(reverse=True)   #각 행별로 큰 숫자들 내림차순 정렬 (첫번째 값이 가장 큰 값)
print(column_max)
rowNum=row_max.index(row[0])


print(f'전체에서 가장 큰 수: {row[0]}')
print(f'가장 큰 수의 행: {rowNum+1}')   
print(f'가장 큰 수의 열: {column_max[4][0]}')
