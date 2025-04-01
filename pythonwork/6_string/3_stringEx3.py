# strip() : 앞뒤 공백을 제거
# rstrip() : 오른쪽(뒤) 공백을 제거
# lstrip() : 왼쪽 (앞) 공백을 제거
str= ' python ';
print(str.strip());
print(str.rstrip());
print(str.lstrip());


str1="#애완견#";
print(str1.strip("#"));
print(str1.rstrip("#"));
print(str1.lstrip("#"));

# replace('기존문자','변경할문자') : 기존문자를 변경할 문자로 변경
# 기존문자의 숫자랑 변경할 문자의 숫자가 같지 않아도 된다.
str2= "abcdef";
print(str2.replace('c','dddd'));

print(str);
print(str1);
print(str2);

# 문자열 함수에서 변경된 내용을 저장하려면 변수에 저장해야한다.

str2 = str2.replace('c','d');
print(str2);