str = "Have a nice day";
print(f"{str}");

#count() : 문자열의 수를 센다.
print(f"str.count('a') : {str.count('a')}");
print(f"str.count('aaa') : {str.count('aaa')}");

#find() : 문자열의 위치를 처음부터 찾는다.
# 단어를 찾으면 단어의 시작위치가 나옴.
print(f"str.find('a') : {str.find('a')}");
print(f"str.find('nice') : {str.find('nice')}");
#없는 단어는 -1로 표시됨
print(f"str.find('are') : {str.find('are')}");

#rfind() : 문자열의 위치를 뒤부터 찾는다.
print(f"str.rfind('a') : {str.rfind('a')}");
#index() : 문자열의 위치를 처음부터 찾는다. 없으면 에러 발생
print(f"str.index('a') : {str.index('a')}");
#print(f"str.index('are') : {str.index('are')}");

#startswith() : 시작 문자열이 맞는지 알려준다.
print(f"str.startswith('Have') : {str.startswith('Have')}");
print(f"str.startswith('have'.title()) : {str.startswith('have'.title())}");

#endswith : 끝 문자열이 맞는지 알려준다.
print(f"str.endswith('day') : {str.endswith('day')}");