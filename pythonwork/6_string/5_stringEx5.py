# isdigit() : 전체가 숫자로 되어 있으면 True 아니면 False
# while True:
#     select = input('1. 입력 2. 출력 3. 수정 4. 삭제 0. 종료 : ');
    
#     if select.isdigit():
#         select = int(select);
#         if 0<=select<=4:# 정상적인 메뉴 번호 입력했을 때
#             print(f"{select} 번을 선택했습니다.");
#         else: # 없는 메뉴 번호를 입력했을 때 
#             print(f'{select} 번은 없는 메뉴 번호 입니다.');
#     else: #숫자가 아닌 문자를 입력했을 때
#         print('숫자로 입력하세요.')
        
# isalpha() : 전체가 문자로 되어 있으면 True 아니면 False
# 영어, 한글 등 언어만 가능(기호 제외, 숫자 제외, 공백 제외)
str= "abcde안녕하세요";
if str.isalpha():
    print('문자로만 구성되어 있습니다.');
    
# isalnum() : 전체가 문자와 숫자로 되어 있으면 True 아니면 False
str1 = "abcde1안녕하세요1";
if str1.isalnum():
    print('문자와 숫자로 구성 되어 있습니다.');
    
# islower(), isupper() : 전체가 소문자 또는 대문자로 되어 있으면 True 아니면 False
# 영어, 숫자, 공백, 기호 상관없지만 영어는 소문자 또는 대문자로 되어 있어야 한다.
str2= "abcde ";
str3= "AB CDE";

if str2.islower():
    print('전체 소문자로 구성되어 있습니다.');
if str3.isupper():
    print('전체 대문자로 구성되어 있습니다.');
    
# isspace() : 전체가 공백문자로 되어 있으면 True 아니면 False
# 공백 문자만 있어야 한다.
str4="       ";
if str4.isspace():
    print('전체 공백으로 구성되어 있습니다.')