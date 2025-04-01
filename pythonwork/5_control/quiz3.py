saveStr="Hello Python Fun";
for i in range(3):
    find= input('찾고자 하는 문자열 입력 : ');
    if find in saveStr:
        print("찾는 문자열이 포함되어 있습니다.");
    else:
        print('다시 입력해주세요.');
