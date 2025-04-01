tp = 10,20,30,"문자열",'1.234';

print(f"tp : {tp}");
print(f"tp type : {type(tp)}");
print(f"tp[0] : {tp[0]}");
print(f"tp[3] : {tp[3]}");

num= tp[0];
print(f"tp[0]에서 가져온 값 : {num}");

for i in tp:
    print(i);
    
#데이터를 수정할 수 없고 에러가 발생한다.
#tp[0]=10000