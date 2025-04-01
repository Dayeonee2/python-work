#upper(): 모든 영문자를 대문자로
#lower(): 모든 영문자를 소문자로
str1 = "Hello";
print(str1.upper());
str2 = 'hello';
print(str2.lower());

# 영문 대소문자를 구분
if str1 == str2:
    print('문자열이 같다.');
else :
    print('문자열이 다르다.');
    
if str1.upper() == str2.upper():
    print("Upper 문자열이 같다.");
else :
    print("Upper 문자열이 다르다.");
    
if str1.lower() == str2.lower():
    print("lower 문자열이 같다.");
else :
    print("lower 문자열이 다르다.");

#swapcase(): 대문자는 소문자로 소문자는 대문자로 변경    
print(str1.swapcase());
print(str2.swapcase());

# title(): 단어의 첫글자는 대문자로
print(str1.title());
print(str2.title());
