# 성적 관리 프로그램 
# 이름, 국어, 영어, 수학 입력
# 출력 : 이름, 총점, 평균 - 점심시간전에 끝날 것 같으면 성적순위
import os
scores = {};
menu = "성적입력", "성적수정", "성적출력", "성적검색", "프로그램종료"; #튜플!
stuId = 20240001; # 학번 - 키값

while True : 
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}");
    select = input("메뉴 입력 : ");#튜플로 메뉴출력->한줄 내려서 나옴

    if select == "1":
        print("##### 성적 입력 #####");
        name = input('이름 입력 : ');
        kor = input("국어 점수 입력 : ");
        eng = input("영어 점수 입력 : ");
        math = input("수학 점수 입력 : ");
        if kor.isdigit() and eng.isdigit() and math.isdigit(): # 입력값이 정수일 때
            if 0<=int(kor)<=100 and 0<=int(eng)<=100 and 0<=int(math)<=100:
                score=[name,int(kor),int(eng),int(math)];
                scores[stuId]= score.copy() #딕셔너리 저장 key값=stuId, vaulu값= score// value는 리스트로 들어감
                #{20240001: ['홍길동', 100, 90, 70]}로 출력
                print(f"{stuId} 학번의 성적이 입력되었습니다.")
                stuId+=1
            else:#점수가 정상이 아닐 때 100보다 크고 0보다 작고
                print('점수는 0~100사이의 값만 입력됩니다. 다시 입력하세요.')
        else: # 입력값이 정상이 아닐 때
            print("점수는 숫자로만 입력 가능합니다.")
    elif select == "2":
        print("##### 성적 수정 #####");
        for i in range(20240001,20240001+len(scores)): #명부에 존재하는 학생 이름 출력
            print(f"{i} 학번 : {scores[i][0]}") #0번이 이름
        findId= input("수정할 학번 입력 : ");
        
        if findId.isdigit():
            if scores.get(int(findId)) != None: #입력한 학번이 있을 때
                kor = input("국어 점수 입력 : ");
                eng = input("영어 점수 입력 : ");
                math = input("수학 점수 입력 : ");
                if kor.isdigit() and eng.isdigit() and math.isdigit(): # 입력값이 정수일 때
                    if 0<=int(kor)<=100 and 0<=int(eng)<=100 and 0<=int(math)<=100:
                        score=[scores[int(findId)][0],int(kor),int(eng),int(math)];
                        #scores[int(findId)][0] ::::scores[int(findId)]는 value값을 반환 ::value값의 첫번째 인덱스를 의미
                        scores[stuId]= score.copy()
                        print(f"{findId}")
                    else:#점수가 정상이 아닐 때 100보다 크고 0보다 작고
                        print('점수는 0~100사이의 값만 입력됩니다. 다시 입력하세요.')
                else: # 입력값이 정상이 아닐 때
                    print("점수는 숫자로만 입력 가능합니다.")
            else:
                print('입력하신 학번은 존재하지 않습니다.');  
        else:
            print("학번은 숫자만 가능합니다.")

    elif select == "3":
        print("##### 성적 출력 #####");
        for i in range(20240001,20240001+len(scores)):
            score=scores[i]; # [name,kor,eng,math]
            scoreSum=0;
            for j in range(1,4): #국어~수학 1~3번 인덱스
                scoreSum+=score[j]
            avg = scoreSum/3
            print(f"== {i} 학번== ");
            print(f"이름 : {score[0]}")
            print(f"총점 : {scoreSum} 점");
            print(f"평균 : {avg:.2f} 점 \n");

    elif select == "4":
        print("##### 성적 검색 #####");
        for i in range(20240001,20240001+len(scores)): #명부에 존재하는 학생 이름 출력
            print(f"{i} 학번 : {scores[i][0]}") #0번이 이름
        findId= input("수정할 학번 입력 : ");
        if findId.isdigit(): # 입력값이 정수일 때
            if scores.get(int(findId)) != None: # 학번이 존재할 때
                score = scores.get(int(findId));
                print(f"== {findId} ==");
                print(f"이름 : {score[0]}");
                print(f"국어 : {score[1]}");
                print(f"영어 : {score[2]}");
                print(f"수학 : {score[3]}");
                print(f"총점 : {score[1]+score[2]+score[3]}");
                print(f"총점 : {(score[1]+score[2]+score[3])/3:.2f}");
            else: #학번이 존재하지 않을 때
                print("입력한 학번은 존재하지 않습니다.")    
        else: #입력값이 정수가 아닐 때
            print("학번은 정수만 입력 가능합니다.")
    elif select == "5":
        print("프로그램을 종료합니다.")
    else:
        print("없는 메뉴 번호 입니다. 다시 입력 하세요.");
    print(scores);
    os.system("pause");
    os.system("cls");
    