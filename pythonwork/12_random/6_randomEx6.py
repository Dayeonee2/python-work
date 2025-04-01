#문제
#점심 메뉴 랜덤 선택 프로그램

menu={"한식":["김치찌개","된장찌개","순두부찌개","참치김밥과 라면"],
      "중식":["짜장면","짬뽕","볶음밥","탕수육"],
      "일식":["연어초밥(10개)","모듬초밥세트","런치세트"]}

for i,(k,v) in enumerate(menu.items()): # 메뉴 출력
    print(f"{i+1}. {k} : {v}")

key=list(menu.keys()) # 메뉴 키 리스트로 변환
    
from random import randrange   
    
choice = input("\n점심 메뉴 종목 ( 1 ~ 3번 외 다른 키 입력시 종목 랜덤) : ")

if choice == '1' or choice =='2' or choice =='3':
    select=int(choice)-1
    num2=randrange(0,len(menu[key[select]]))
    print(f"\n#### 점심메뉴 : {menu[key[select]][num2]}");
    
else:
    num1=randrange(0,len(menu)) # 메뉴 종목 선택 안할시 사용할 종목고르기
    num2=randrange(0,len(key[num1]))# 종목안에서 메뉴고르기
    print(f"\n#### 점심메뉴 : {key[num1]} - {menu[key[num1]][num2]}");