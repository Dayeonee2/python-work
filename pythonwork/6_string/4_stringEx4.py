# split() : 공백 문자를 기준으로 문자들을 분리해서 List로 변환
str = '바나나 사과 딸기 망고';
print(str);
print(str.split());

# split('문자') : 문자를 기준으로 문자들을 분리해서 List 로 변환
str1 = '바나나,사과,딸기,망고';
print(str1);
print(str1.split(','));


# splitlines() : 행을 기준으로 문자열을 분리해서 List로 변환
str2 = '바나나\n사과\n딸기\n망고';
print(str2);
print(str2.splitlines());

# "", '' : 문자열을 구분하는 기호
# 문장을 저장하기 위해서는 \n을 이용하여 한줄에 기술해야 한다.
# '''문장''',"""문장""" : 문장을 저장하는 기호
str3 = '''
바나나
딸기
사과
망고
'''
print(str3.splitlines());
# 이 기호는 다른 강의에서는 문장으로 된 주석 쓸 때
'''
내용을 기술 했다.
'''

#join(): 뒤문자열의 한글자씩과 첫문자열 전체를 반복 실행
str4 = "***"
str5 = "hello"
print(str4.join(str5))