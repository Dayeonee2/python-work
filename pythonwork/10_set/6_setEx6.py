set1 = {1,2,3};
print(set1);
# set1 +={4}; #set과 set은 + 가 지원되지 않는다.
# print(set1);

# 요소에 추가 : add() 여러개가 안됨.
set1.add(4);
print(set1);

#set은 중복값을 허용 안한다.
#에러는 없고 추가되지 않음
set1.add(4);
print(set1);

set1.add('5'); #문자열도 중복값은 추가되지 않음
print(set1);

set1.add('5');
print(set1);