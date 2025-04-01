str = "NeVer EvEr give up"
str=str.replace(' ','-')
str=str.title()
print(str)

str1='2020/01/23'
str1=str1.split('/')
for i in range(len(str1)):
    print(str1[i]);

for i in str1:
    print(i);
    
for i,s in enumerate(str1):
    #enumerate() : 반복자로 첫번째 변수에는 인덱스번호, 두번째 list의 인덱스 값
    print(f"{i} 인덱스 번호 : {s}");


for i,s in zip(range(len(str1)),str1):
    print(f"{i} 인덱스 번호 : {s}");
    