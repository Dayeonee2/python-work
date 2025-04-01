#은행 계좌 프로그램

#은행에서 할 수 있는 업무
#1.입금
#2.출금
#3.대출
#4.계좌이체
#5.적금
#6.세금
#계획후에는 데이터저장을 어떻게 할 것인지 생각해야함// 리스트인지 딕셔너리인지?
#개인정보(계좌번호:[이름,주민,주소]) dict 계좌정보(계좌번호:[잔액,거래내역,입출금]) dict

#Sns검색 프로그램
#게시물저장: 아이디, 태그, 게시물제목, 게시물내용
#검색기능
#사용자 계정 만들기{사용자계정(key):[태그,게시물내용]}
#1.사용자계정생성
#2.게시글 업로드--업로드 할때 게시글내용에 태그
#3.검색기능
menu1= "ID 만들기" , "로그인", "로그아웃" , "종료" ;
menu2= "게시글 업로드", "게시글 수정", "게시글 삭제", "게시글 검색", "돌아가기";
account={1:{"happy__you":[["ff","f4f","강남"],["강남 맛집 방문기"]]}} #1:{아이디:[태그,게시글]}
personal={"happy__you":['홍길동','01011112222','12345']}#이름,전화번호, 비번


import os

while True:
    
    accountkey=list(account.keys());
    for i in range(len(menu1)): #메뉴1번 목록 출력
        print(f"{i+1}. {menu1[i]}");
    select= input("메뉴 번호를 입력하세요 : ");
    
    
    if select == '1':
        com=[]; #personal 에 입력될 value 리스트 [id, name]
        print("#"*5,"ID 생성", "#"*5);
        id= input("아이디 입력 : ");
        password=input("비밀번호 입력(4자리 이상) : ");
        name= input("이름 입력 : ");
        phone=input('핸드폰 번호 입력 (- 제외) : ')
        if not phone.isdigit():
            print('핸드폰번호는 숫자로 입력하세요.'); 
        else: 
            if len(phone)==11 and len(password)>=4: # 번호가 11자리 입력되었을때 account와 personal에 각각 저장
                com.append(name);
                com.append(phone);
                com.append(password)
                account[id]=[]
                personal[id]=com;
            else:   
                print("잘못입력하셨습니다.\n비밀번호는 4자리 이상, 핸드폰번호는 11자리를 입력하세요.")          
    
                         
    elif select == '2':
        id=input("로그인할 아이디 입력 : ");
        password=input("비밀번호 입력 : ");
        if id not in accountkey:
            print(f"존재하지 않는 계정입니다.");
        else:
            if password:
                for i in range(len(menu2)):
                    print(f"{i+1}. {menu2[i]}");
                select=input("메뉴 번호 입력 : ");
                if select=="1":
                    com=[]
                    print("#"*5,"게시글 생성", "#"*5);
                # =input("")
            # elif select == "2":
            # elif select == "3":
            # elif select == "4":
            # elif select == "5":
                # break;
            else:
                print("존재하지 않는 메뉴번호입니다.")
    
    # elif select=='3':
        
    elif select == '4':
        print('종료합니다.');
        break;
    else:
        print('잘못입력하셨습니다. 메뉴 번호를 입력해주세요.');
    os.system("pause");
    os.system("cls");