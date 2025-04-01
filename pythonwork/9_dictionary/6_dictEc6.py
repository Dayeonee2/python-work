num={1:'일',2:'이',3:'삼'};

print(f"num : {num}");
print(f"num.get(3) : {num.get(3)}")
print(f"num.get(9) : {num.get(9)}")
print(f"num.get(0,'없음') : {num.get(0,'없음')}") 
#'없음'은 없을 경우에 출력될 방법

su = int(input("검색할 키 입력 : "));

if num.get(su) ==None: 
    #Python에서 없는값(Null)이 None을 의미
    print("찾는 값이 없습니다.")
else :
    print(f"num.get(su) : {num.get(su)}");