# 문제 
# 학생 성적 프로그램
# 입력 : 순번, 이름, 국어, 영어, 수학
# 입력 후 연산 : 총점, 평균 
# 위의 내용을 score.txt 파일에 저장
# 입력, 검색, 삭제, 수정이 가능하도록 만들어보세요 
# 출력시에는 순번, 이름, 총점, 평균 출력
import os
filedir = "C:\\20240416\pythonwork\\17_file\\score.txt";

def screenCls():
    os.system("pause");
    os.system("cls");

def fileRead():
    with open(filedir, 'r', encoding="utf-8") as f:
        student = f.readlines(); # 한줄씩 가져오기
        return student;

def delmod(sub, select):
    print(f"### 학생 성적 {sub} ###");
    name = input(f"{sub}할 학생 이름 입력 : ");

    student = fileRead(); #함수로 파일 읽기, student에 한줄씩 읽어짐
    chgStudent = ''; 
    b = True;
    for s in student:
        stu = s.split(",");
        if name == stu[1] and select == "3":
            print(f"{name} 학생의 성적을 삭제합니다.");
            b = False;
        elif name == stu[1] and select == "4":
            kor = int(input("국어 점수 입력 : "));
            eng = int(input("영어 점수 입력 : "));
            math = int(input("수학 점수 입력 : "));
            sumScore = kor + eng + math;
            avgScore = sumScore / 3;
            chgStudent += f"{stu[0]},{name},{kor},{eng},{math},{sumScore},{avgScore:.2f}\n"; 
            b = False;
        else:   
            chgStudent += s;
    if b :
        print(f"{name} 이름을 찾을 수 없습니다.");
    with open(filedir, 'w', encoding="utf-8") as f:
        f.write(chgStudent);
    
student = fileRead();
stuNo = int(student[-1].split(",")[0])+1;##이거 뭐징

while True:
    print("1. 학생 성적 입력");
    print("2. 학생 성적 검색");
    print("3. 학생 성적 삭제");
    print("4. 학생 성적 수정");
    print("5. 학생 정보 전체 출력");
    print("0. 종료");
    select = input("선택 : ");

    screenCls();

    if select == "1":
        try:
            print("### 학생 성적 입력 ###");
            name = input("이름 입력 : ");
            kor = int(input("국어 점수 입력 : "));
            eng = int(input("영어 점수 입력 : "));
            math = int(input("수학 점수 입력 : "));
            if (0 <= kor <= 100) and (0 <= eng <= 100) and (0 <= math <= 100):
                sumScore = kor + eng + math;
                avgScore = sumScore / 3;
                with open(filedir, 'a', encoding="utf-8") as f: #입력저장
                    f.write(f"{stuNo},{name},{kor},{eng},{math},{sumScore},{avgScore:.2f}\n");
                stuNo+=1;
            else:
                print("점수는 0 ~ 100점 사이만 가능합니다.");
        except:
            print("점수는 숫자만 가능 합니다.");
    elif select == "2":
        print("### 학생 성적 검색 ###");
        name = input("검색할 학생 이름 입력 : ");

        student = fileRead();
        for stu in student:
            stu = stu.split(",");
            if name == stu[1]:
                print(f"=== {stu[0]}번 ===");
                print(f"이름 : {name}");
                print(f"총점 : {stu[-2]} 점");
                print(f"평균 : {stu[-1].split("\n")[0]} 점");
                break;
        else:
            print(f"{name} 이름을 찾을 수 없습니다.");
    elif select == "3":
        delmod("삭제", select);
    elif select == "4":
        delmod("수정", select);
    elif select == "5":
        print("### 학생 성적 전체 출력 ###");
        student = fileRead();
        for stu in student:
            stu = stu.split(",");
            print(f"=== {stu[0]}번 ===");
            print(f"이름 : {stu[1]}");
            print(f"총점 : {stu[-2]} 점"); #뒤에서 두번쨰
            print(f"평균 : {stu[-1].split("\n")[0]} 점"); #뒤에서 첫번째
    elif select == "0":
        print("프로그램을 종료합니다.");
        break;
    else:
        print("선택된 메뉴 번호가 없습니다.");
    
    screenCls();