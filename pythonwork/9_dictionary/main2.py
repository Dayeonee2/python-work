#문제
#숫자를 5개 입력- 큰 수가 1~ 제일 작은 수가 5가 되도록 해보세요
####################################################################
# rank=[];
# number=[];
# for i in range(5):
#     number.append(int(input("정수 입력 : ")));
#     rank.append(1);
#     for j in range(len(number)):
#         if number[i]>number[j]:
#             rank[j]+=1;
#         elif number[i]<number[j]:
#             rank[i]+=1

# for i in range(5):
#     print(f"{rank[i]} 등 : {number[i]}");

####################################################################


# number=[];
# for i in range(5):
#     number.append(int(input("정수 입력 :")));
    
# rank=[1,1,1,1,1];
# for i in range(5):
#     for j in range(i,len(number)):
#         if number[i]>number[j]:
#             rank[j]+=1;
#         elif number[i]<number[j]:
#             rank[i]+=1;
# for i in range(len(number)):
#     print(f"{rank[i]} 등 {number[i]}")



############################################################
# # 선택 정렬
# number=[];
# for i in range(5):
#     number.append(int(input("정수 입력 :")));
# numberreverse=number.copy()   
# for i in range(5):
#     for j in range(i,len(number)):
#         if number[i]<number[j]: #내림차순 정렬
#             number[i], number[j] = number[j],number[i]
#         if numberreverse[i]>numberreverse[j]: #오름차순 정렬
#             numberreverse[i], numberreverse[j] = numberreverse[j],numberreverse[i]

# print(number);
# print(numberreverse);  
                     
                     
# #버블 정렬: 앞,뒤 두개 비교해서 큰애가 앞으로 가도록
# #5 8 2 3 1

# number=[];
# for i in range(5):
#     number.append(int(input("정수 입력 :")));
# numberreverse=number.copy()   
# for i in range(5):
#     for j in range(len(number)-1):
#         if number[j]<number[j+1]: #내림차순 정렬
#             number[j], number[j+1] = number[j+1],number[j]
#         if numberreverse[j]>numberreverse[j+1]: #오름차순 정렬
#             numberreverse[j], numberreverse[j+1] = numberreverse[j+1],numberreverse[j]

# print(number);
# print(numberreverse); 

##############################################
#삽입 정렬 
number=[]
for i in range(5):
    number.append(int(input("정수 입력 :")));
numberR=number.copy() ###5 8 2 3 1 ##
for i in range(len(number)-1):  #0123
    for j in range(i+1, 0,-1):   #2,0,-1  # 종료 1?
        if number[j-1] > number[j]:#2,1 1,0
            number[j-1],number[j] = number[j],number[j-1];
        if numberR[j-1] < numberR[j]:
            numberR[j-1],numberR[j] = numberR[j],numberR[j-1];
