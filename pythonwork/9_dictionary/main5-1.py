# SNS 검색 프로그램
# 게시물 저장 : 아이디, 태그, 게시물 내용
# 검색 기능 : 아이디, 태그, 게시물 내용 검색이 가능
# 사용자 계정 만들기 : 아이디, 비밀번호
# 로그인 - 로그인, 비밀번호 찾기, 비밀번호 수정
# 사용자 계정 삭제 : 삭제시 해당 아이디 게시물 삭제

# 사용자 계정 - 아이디, 비밀번호 저장
# 자료형 : list, dictionary
# list 로 사용했을 때
# 계정 저장 : [[아이디, 비밀번호], [아이디, 비밀번호]];
# 중복 아이디 찾기 : for i in 계정list :  if id == i[0] : 같다 else: 다르다
# 삭제 할때 : for i in 계정list : if id == i[0] : 삭제 else : pass
# dictionary 로 사용했을때
# 계정 저장 : {아이디:비밀번호, 아이디:비밀번호}
# 중복 아이디 찾기 : if 계정dict.get(id) != None : 있음 else : 없음
# 삭제 할때 : if 계정dict.get(id) != None : 삭제 else : 없음

# 게시물 저장 : {1:{아이디:[태그, 게시물내용]}, 2:{아이디:[태그, 게시물]} }

# 사용자계정 저장하는 자료형 - dictionary 
users = {"a":"1234"};
# 게시물 저장 하는 자료형 - dictionary 
contents = {};
# 로그인이 성공하면 로그인한 아이디를 저장
loginId='';
#등록할 게시물 번호를 저장
postNo = 1;

import os
while True:
    if loginId == '':
        print("##### 케이지 SNS #####");
        print("1. 로그인");
    else:
        print("##### 케이지 SNS #####");
        if len(contents) !=0:
            print("="*20);
            for k,v in contents.items(): #{1:{id:[태그,내용]}}
                print('-'*20);
                key = list(contents.keys());
                for i in range(len(contents)-1,-1,-1):  #[0,1,2,3,4] 4~0까지 거꾸로                
                    c=contents.get(key[i]); # [(id : [태그, 내용])]
                    con=list(c.items()); #con의 0번 인덱스를 언팩 con[0][0]=id, con[0][1]=content
                    id,content=con[0];
                    print(f"아이디 : {id}\n태그 : {content[0]}\n게시글 : {content[1]}");
            print("="*20);
        print(f"1. {id} 로그아웃");
        print("2. 게시글 작성");
        print("3. 게시글 검색");
        print("4. 마이페이지");
    select = input("선택 : ");
    
    if select == "1":
        if loginId=='':
            print("##### 로그인 페이지 #####");
            print("1. 로그인");
            print("2. 회원가입");
            print("3. 비밀번호 찾기");

            subSelect = input("선택 : ");

            if subSelect == "1":
                id = input("아이디 입력 : ");
                pwd = input("암호 입력 : ");
                
                if users.get(id) != None:
                    if pwd==users.get(id):
                        print(f"{id} 님 환영합니다.");
                        loginId = id;
                    else:
                        print("아이디나 비밀번호가 틀립니다. 다시 입력하세요");
                else:
                    print("아이디나 비밀번호가 틀립니다. 다시 입력하세요");
            elif subSelect=='2':
                print("##### 회원 가입 #####");
                id=input("사용할 아이디 입력 : ");
                
                if id.isspace() or id=="":
                    print("공백을 아이디로 사용이 불가능합니다.")
                elif users.get(id) != None:
                    print(f"{id} 는 이미 사용중입니다.");
                else:
                    pwd=input("사용할 암호 입력 : ");
                    pwdCh=input("암호 확인 입력 : ");
                    if pwd== pwdCh and pwd != '' and not pwd.isspace():
                        users[id]=pwd;
                        print(f"{id} 님의 회원 가입이 완료되었습니다.")
                    else:
                        print("암호를 다시 확인하세요.");
            elif subSelect=='3':
                print("##### 비밀 번호 찾기 #####");
                id= input("비밀번호 찾을 아이디 입력 : ");
                
                if users.get(id) !=None:
                    print(f"{id} 님의 암호는 {users.get(id)} 입니다.");
                else:
                    print(f"{id} 는 존재하지 않습니다. 회원가입하세요.");
            else:
                print("없는 메뉴 번호입니다.");
        else:
            print(f"##### {id} 로그아웃 ####");
            loginId='';
    
    elif select=="2" and loginId !='':
        c={}
        print("##### 게시물 작성 페이지 #####");
        con= input("게시글 내용 입력 : ");
        li=con.split();
        tag='';
        content='';
        for i in li:
            if i.startswith("#"):
                i=i.split("#");
                # #봄#여름 = ['', '봄', '여름']
                for j in i:
                    if j!='': 
                        tag+="#"+j+" ";
            else:
                content+=i+" ";
        c[loginId]=[tag,content]
        contents[postNo] =c.copy();
        print(f"{postNo} 번 게시글이 작성되었습니다.");
        postNo+=1;
    
    elif select=='3'and loginId !='':
        print("##### 게시글 검색 #####");
        key= input("검색할 단어 입력 : ");
        # @ - 아이디, # - 태그, 게시글(전체) 검색
        check= True;
        if key.startswith("@"):
            id = key[1:];
            
            if users.get(id) != None:
                for k,v in contents.items():
                    for user,content in v.items():
                        if id == user:
                            print(f"아이디 : {user}\n태그 : {content[0]}\n게시글 : {content[1]}");
                            print('-'*20);                         
            else:
                print(f"{id}님은 존재하지 않는 아이디입니다.")

            print("아이디");
        elif key.startswith("#"):
            tag= key[1:];
            
            for k,v in contents.items():
                for users, content in v.items():
                    if tag in content[0]:
                        print(f"아이디 : {user}\n태그 : {content[0]}\n게시글 : {content[1]}");
                        print('-'*20);
                        check = False;
            if check:
                print(f"검색한 {tag} 가 존재하지 않습니다.");
        else:
            for k,v in contents.items():
                for users, content in v.items():
                    if key in content[1]:
                        print(f"아이디 : {user}\n태그 : {content[0]}\n게시글 : {content[1]}");
                        print('-'*20);
                        check=False;
            if check:
                print(f"검색한 {key} 가 존재하지 않습니다.");
                
    elif select=='4'and loginId !='':
        print("##### 마이 페이지 #####");
        print("1. 비밀번호 변경");
        print("2. 회원 탈퇴");
        subSelect=input("선택 : ");
        
        if subSelect=="1":
            nowpwd=input("현재 비밀번호 입력 : ");
            if users.get(loginId) == nowpwd:
                changepwd=input("변경할 비밀번호 입력 : ");
                users[loginId]=changepwd;#새 비번으로 덮어씌우기
            else:
                print("현재 비밀번호가 틀립니다. 다시 확인하세요.");
        
        elif subSelect=="2":  # 실행이 안됨
            nowpwd=input("현재 비밀번호 입력 : ");
           
            if users.get(loginId) == nowpwd:
                out = input("회원을 탈퇴하시겠습니까? (y/n) : ");
                
                if out=='y' or 'Y':
                    print("회원 정보가 삭제되었습니다.");
                    keys = contents.keys();
                    for i in range(len(contents)):
                        con= contents[keys[i]];
                        for user, content in con.items():
                            if user==loginId:
                                contents.pop(keys[i]);
                    users.pop(loginId);
                    loginId='';
                    
                elif out=='n' or 'N':
                    print("회원 탈퇴가 취소되었습니다.");
                else:
                    print("잘못 입력하셨습니다. 다시 확인하세요.");
            else:
                print("현재 비밀번호가 틀립니다. 다시 확인하세요.");
    else:
        print("없는 메뉴 번호입니다.")
    os.system("pause");
    os.system("cls");
        
