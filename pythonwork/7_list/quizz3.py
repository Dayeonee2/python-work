# 문제 
# MP3 플레이어 만들어 보기
# 1. 재생 2. 정지 3. 다음곡 4. 이전곡 5. 곡 추가 6. 곡 삭제 0. 종료

# 음악을 저장하는 리스트
song = [["아일릿", "Magnetic"], ["여자아이들", "나는 아픈 건 딱 질색이니까"]];
index = 0;
start=[];
stop=False

while True:
    if stop:
        print("###################");
        print("####### ■  ########");
        print("###################");
        print(f"{start[0]} - {start[1]}");
    elif len(start) != 0: 
        print("###################");
        print("####### ▷  ########");
        print("###################");
        print(f"{start[0]} - {start[1]}");
    print("1. 재생 2. 정지 3. 다음곡 4. 이전곡 5. 곡추가 6. 곡삭제 7. 곡 수정 0. 종료");
    select = input("메뉴 선택 : ");
    
    if select == "1":
        if len(start) == 2 and stop:
            stop = False;
        else:
            for i,s in enumerate(song):
                print(f"{i+1}. {s[0]} - {s[1]}")
            select = input("재생할 노래 번호 입력 : ");
            if select.isdigit():
                if len(song)>= int(select):
                    index= int(select)-1;
                    start= song[index]
                    stop=False;
                else:
                    print('없는 노래 번호입니다.')
    elif select == "2":
        print(f"{start[0]} - {start[1]} 정지");
        stop=True
    elif select == "3":
        if len(start)==0:
            print(f"재생 목록이 없습니다.");
        elif index==(len(song)-1):
            index=0
        else:
            index+=1;
        start = song[index];
        print(f"다음곡 : {start[0]} - {start[1]}");
    elif select == "4":
        if len(start)==0:
            print(f"재생 목록이 없습니다.");
        else:
            index-=1;
            if index<0:
                index=(len(song)-1);
        start = song[index];
        print(f"이전곡 : {start[0]} - {start[1]}");
    elif select == "5":
        print("######곡추가######");
        singer=[];
        singer.append(input("가수 이름 입력 : "));
        singer.append(input("제목 입력 : "));
        song.append(singer)
    elif select == "6":
        print("######곡삭제######");
        subject = input("삭제할 제목 입력 : ");
        for i in range(len(song)):
            if subject == song[i][1]:
                print(f"{subject} 곡을 삭제합니다.");
                song.remove(song[i])
            elif subject!=song[i][1] and i == (len(song)-1):
                print("해당하는 곡이 존재하지 않습니다.")
            else:
                pass
    elif select == "7":
        print("######곡 수정######");
        for i in range(len(song)):
            print(song[i]);
        print("1. 가수 이름 수정 2. 곡 제목 수정 0. 돌아가기")
        choice_= input(" 메뉴 입력 :");
        if choice_=='1':
            bull=False
            subj=input("수정할 가수 입력 : ");
            for i in range(len(song)):
                if subj in song[i][0]:
                    subp=input('수정 후 가수 이름 입력 : ');
                    index=i
                    start = song[index];
                    song.pop(i)
                    song.insert(i,[subp,start[1]])
                    print(f"{subj}를 {subp}로 수정했습니다.")
                    index=0
                    start=song[index]
                    bull=True
                    break;#break로 for문 종료
                else:
                    pass;
            if bull == False:
                print("해당하는 가수가 존재하지 않습니다.")

        elif choice_=='2':
            stop=False
            bull=False#논리형 자료를 사용하여 for문 종료
            subj=input("수정할 곡 제목 입력 : ");
            for i in range(len(song)):
                if subj in song[i][1]:
                    subp=input('수정후 곡 제목 입력 : ');
                    index=i
                    start = song[index];
                    song.pop(i)
                    song.insert(i,[start[0],subp])
                    print(f"{subj}를 {subp}로 수정했습니다.")
                    index=0
                    start=song[index]
                    bull=True #if문 실행못하게 함
                    break;
            if bull == False:
                print("해당하는 곡이 존재하지 않습니다.")
                
        elif choice_=='0':
            pass;
        else:
            print('메뉴 번호를 정확히 입력해주세요.')
        
    elif select == "0":
        print("MP3를 종료합니다.");
        break;
    else :
        print("선택된 메뉴가 없습니다.");