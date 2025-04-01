#문제
#전화번호부 만들기
#1.연락처 저장
#2.연락처 검색
#0.프로그램 종료
print("#"*5,"전화번호부","#"*5);
number={'홍길동':'010-1111-2222','이순신':'010-9999-9999'}
while True:
    print('1. 연락처 저장 2. 연락처 검색 0. 프로그램 종료');
    select=input('메뉴 입력 : ');
    if select=='1':
        name=input('이름 입력 : ');
        phone=input('번호 입력 : ');
        number[name]=phone;
    elif select == '2':
        if len(number)==0:
            print('저장된 번호가 없습니다.')
        else:
            name=input('검색할 이름 입력 : ');
            if name in number:
                print(f'번호는 {number[name]}이다.')
            else:
                print('저장된 이름이 없습니다.')
        # for i in number: #i값이 key값(다른방법)
        #     if i==name:
        #         print(f"{name} : {number{name}}")
        #else:
        #   print('저장된 이름이 없습니다.')
            
    elif select == '0':
        break;
    else:
        print('제시된 메뉴 번호를 입력해주세요.')