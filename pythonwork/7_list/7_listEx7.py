ls = [1,2,3,4,5];

#인덱싱
print(ls[0]);
print(ls[1]);

str="slicing test";
print(str[3]);
print(str[8]);

#슬라이싱 : 원하는 데이터의 범위를 가져온다.
#ls[시작index: 끝-1 index] : 0~ 끝-1 인덱스 값을 가져온다.
#시작값은 0으로 생략가능하다.
#끝값도 생략 가능하다.
print(f"ls[0:3]: {ls[0:3]}");
print(f"ls[:3] : {ls[:3]}");
print(f"ls[:] : {ls[:]}");
print(f"ls[1:4] : {ls[1:4]}");
print(f"ls[3:] : {ls[3:]}");

print(f"str[0:3]: {str[0:3]}");
print(f"str[:3] : {str[:3]}");
print(f"str[:] : {str[:]}");
print(f"str[1:4] : {str[1:4]}");
print(f"str[3:] : {str[3:]}");