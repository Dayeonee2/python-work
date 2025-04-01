import random

ls = ['a','b','c','d','e'];

# list 의 값의 위치를 랜덤하게 변경한다.
random.shuffle(ls);
print(ls);

str = "hello";
strList = [];
for i in str:
    strList.append(i);
random.shuffle(strList);
print(strList);