# 서식 문자에 여러 값을 출력하기 위해서는 
#() 안에 출력할 값을 넣어야 한다.
print("%d %f %s "%(123,1.234,"안녕"));

print("%d"%1.234);
print("%f"%123);

#print("%d"%"문자");  error
#print("%f"%"문자");  error

print("%s"%123);
print("%s"%1.234);


# %c : 단일문자 출력
print("%c"%"a");
print("%c"%"한");
#print("%c"%"문자열")  error

print("%c"%65);  #ASCII,유니코드로 변환돼서 단일문자로 출력
print("%s"%65);

# 1byte 는 -128~127까지 표현
# Data = byte , 신호 = bit