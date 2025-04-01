#선생님 mp3풀이 
# 문제
# MP3 플레이어 - 딕셔너리로 구현
allSong = { # 키 : [제목, 가수]
1 : ["Be There For Me","NCT 127"],
2 : ["Drama", "aespa"],
3 : ["Closer Than This","지민"],
4 : ["To. X", "태연"],
5 : ["Love 119","RIIZE"],
6 : ["UNTOUCHABLE","ITZY"],
7 : ["DASH", "NMIXX"],
8 : ["Love wins all","아이유"],
9 : ["UGLY","EVNNE"],
10 : ["Super Lady", "(여자)아이들"],
11 : ["첫 만남은 계획대로 되지 않아", "TWS"],
12 : ["EASY","LE SSERAFIM"],
13 : ["밤양갱", "비비"],
14 : ["나는 아픈 건 딱 질색이니까", "(여자)아이들"],
15 : ["Magnetic", "ILLIT"],
16 : ["Smoothie", "NCT DREAM"],
17 : ["Deja Vu", "투모로우바이투게더"],
18 : ["Bye My Monster", "온앤오프"]
}
# 플레이스 리스트를 딕셔너리 저장
# { "신나는 노래" : [1,2,3,4,5], "우울할때 듣는 노래" : [3,4,5] }
playlist = {'신나는 노래' :[1,2,3]};
# 현재 재생 중인 노래 키 값 저장 
nowPlay = 0;
# 메뉴 내용 저장 튜플
menu = "재생", "정지", "다음곡", "이전곡", "곡추가", "곡삭제", "Playlist", "종료";
song = list(allSong.keys())
# 콘솔화면 제어 - 운영체제 콘솔 명령어 실행
import os

selectPlay='';
playSelect='';


while True:
    playkeys=list(playlist.keys());    
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}");
    select = input("메뉴 입력 : ");   
    if select == "1":
        if len(song)==0:
            print("저장된 노래가 없습니다. 저장 후 재생하세요.")
        else:
            page = 0;
            acount=5;
            while True:
                if selectPlay =='':
                    print("####플레이리스트 목록####");
                    for i,p in enumerate(playkeys):
                        print(f"{i+1} . {p}");
                    print("0. 전체");
                    
                    selectPlay = input("PlayList 선택 : ");
                    
                    if selectPlay.isdigit() and int(selectPlay) <= len(playkeys):
                        if int(selectPlay)!=0:
                            song= playlist[playkeys[int(selectPlay)-1]];
                            playSelect=playkeys[int(selectPlay)-1]
                        elif int(selectPlay)==0:
                            song= list(allSong.keys());
                        else:
                            print("없는 플레이리스트 번호입니다.")
                            continue;
                os.system("cls")
                print("#### 곡 정보 ####")       
                for i in range(page,len(song)):# 전체 노래 리스트 출력
                    if i != page and i%acount ==0:
                        break;
                    print(f"{song[i]}. {allSong[song[i]][0]} - {allSong[song[i]][0]}");
                    end=i
                idx = input("노래 번호 또는 검색할 단어 입력 : ");
                if idx == '이전':
                    if page==0:
                        print("이전 데이터가 없습니다.")
                        os.system("pause");#있어야 print값이 빛의 속도로 사라지지 않아 보임
                    else:
                        page-=acount;
                elif idx=='다음':
                    if end+1== len(song):
                        print("다음 데이터가 없습니다.")
                        os.system("pause");
                    else:
                        page+=acount
                else:
                    break;
            if idx.isdigit() and int(idx) in song: # 입력된 값이 정수 일때 재생
                nowPlay = int(idx);
                print(f"{nowPlay}. {allSong[nowPlay][0]} - {allSong[nowPlay][1]} - 재생");
            
            else: # 입력된 값이 없는 번호이거나 문자일 때 출력
                b=True;
                for i in song:
                    if (idx.lower() in allSong[i][0].lower()) or (idx.lower() in allSong[i][1].lower()): 
                        #문자열의 일부 검색시 리스트 안에 요소로 검색해야함
                        print(f"{i}. {allSong[i][0]} - {allSong[i][1]}");
                        b=False;
                if b:
                    print("노래 번호가 없는 번호이거나 검색어가 없습니다.. 다시 입력하세요.");
                else:
                    idx=input("노래 번호 입력 :")
                    if idx.isdigit() and int(idx) in song: # 입력된 값이 정수 일때 재생
                        nowPlay = int(idx);
                        print(f"{nowPlay}. {allSong[nowPlay][0]} - {allSong[nowPlay][1]} - 재생");
                    else:
                        print("없는 노래 번호 입니다.")
    elif select == "2":
        if nowPlay != 0:
            print(f"{nowPlay}. {allSong[nowPlay][0]} - {allSong[nowPlay][1]} - 정지");
        else:
            print("재생 중인 노래가 없습니다.");
    elif select == "3":
        if nowPlay!=0: ##[1,2,5,7]
            idx=song.index(nowPlay)
            if idx == len(song)-1:
                nowPlay=song[0]; 
                #재생중인 노래의 키값이 song키값의 첫번째 값이 된다.
            else:
                nowPlay=song[idx+1]
            print(f"{nowPlay}. {allSong[nowPlay][0]} - {allSong[nowPlay][1]} - 재생");
        else:
            print("재생중인 노래가 없습니다.")
        
    elif select == "4":
        if nowPlay!=0: ##[1,2,5,7]
            idx=song.index(nowPlay)
            if idx == 0:
                nowPlay=song[len(song)-1]; 
                #재생중인 노래의 키값이 song키값의 첫번째 값이 된다.
            else:
                nowPlay=song[idx-1]
            print(f"{nowPlay}. {allSong[nowPlay][0]} - {allSong[nowPlay][1]} - 재생");
        else:
            print("재생중인 노래가 없습니다.")
    elif select == "5":
        singer=[]
        singer.append(input("노래 제목 입력 : "));
        singer.append(input("가수 이름 입력 : "));
        allSong[song[len(song)-1]+1]=singer.copy() #keys[인덱스]=list인덱스 값
        
    elif select == "6":
        select= input("1. 곡 삭제 2. Playlist 삭제 : ");
        
        if select =='1':
            for i,n in allSong.items(): # 전체 노래 리스트 출력
                print(f"{i}. {n[0]} - {n[1]}");
            idx = input("삭제할 노래 번호 입력 : ");
            if idx.isdigit() and allSong.get(int(idx)) != None :
                print(f"{allSong.pop(int(idx))} 번호의 노래를 삭제합니다.")
                #print 안에 pop함수 있어도 삭제 가능
                for i in playkeys:
                    if int(idx) in playlist[i]:
                        playlist[i].remove(int(idx));
                
            else:
                print("없는 노래 번호이거나 문자입니다. 다시 입력하세요.")
        
        elif select =='2':
            for i in song: # 전체 노래 리스트 출력
                print(f"{i}. {allSong[i][0]} - {allSong[i][1]}");
            idx = input("삭제할 노래 번호 입력 : ");
            if idx.isdigit() and int(idx) in song:
                print(f"{allSong(int(idx))} 번호의 노래를 삭제합니다.")
                
                playlist[playSelect].remove(int(idx))
                #print 안에 pop함수 있어도 삭제 가능
                
                for i in playkeys:
                    if int(idx) in playlist[playkeys[int(idx)-1]]:
                        playlist[playkeys[int(idx)-1]].pop(int(idx));
            else:
                print("없는 노래 번호이거나 문자입니다. 다시 입력하세요.")
    elif select == "7":
        print("1. PlayList 생성/삭제 2. PlayList 보기 3. PlayList 노래 등록");
        select = input("메뉴 입력 : ");
        if select == '1':
            select=input("1. 생성 2. 삭제 : ");
            if select=='1':
                lsName = input("Playlist 이름 입력 : ");
                playlist[lsName]=[];
            elif select=='2':
                for i in range(len(playkeys)):
                    print(f"{i+1} . {playkeys[i]}");
                lsIdx= input("Playlist 선택 : ");
                if lsIdx.isdigit() and playlist.get(playkeys[int(lsIdx)-1]) != None:
                    check= input(f"{playkeys[int(lsIdx)-1]} Playlist를 삭제하시겠습니까? (y/n) :")
                    if check=="y" or 'Y':
                        print(f"{playkeys[int(lsIdx) - 1]} 삭제 완료했습니다.");
                        playlist.pop(playkeys[int(lsIdx) - 1]);
                    else:
                        print("삭제 취소 및 없는 메뉴번호입니다.")
            else:
                print("없는 메뉴 번호입니다.")
            
        elif select == '2':
            for i in range(len(playkeys)):
                print(f"{i+1} . {playkeys[i]}");
            lsIdx= input("Playlist 선택 : ");
            if lsIdx.isdigit() and playlist.get(playkeys[int(lsIdx)-1]) != None:
                 ##플레이리스트 value가ls,list형태
                ls = playlist[playkeys[int(lsIdx) - 1]];
                for i in ls:
                    print(f"{i}. {allSong[i][0]} - {allSong[i][1]}");                    
            else:
                print("선택된 번호가 없거나 문자입니다.")
                
        elif select == "3":
            select = input("1. 재생 중인 곡 등록 2. 목록에서 등록 : ");           
            if select == "1":
                if nowPlay == 0:
                    print("재생 중인 곡이 없습니다.");
                else:
                    print("#### PlayList 목록 ####");
                    for i in range(len(playkeys)):
                        print(f"{i+1}. {playkeys[i]}");
                    idx = input("PlayList 선택 : ");

                    if idx.isdigit() and int(idx)-1 < len(playkeys):
                        if nowPlay in playlist[playkeys[int(idx)-1]]:
                            print("이미 등록된 곡 입니다.");
                        else:
                            playlist[playkeys[int(idx)-1]].append(nowPlay);
                            print(f"{playkeys[int(idx)-1]} 리스트에 {allSong[nowPlay][0]} 등록되었습니다.");
                    else:
                        print("없는 PlayList 입니다.");
            elif select == "2":
                page = 0;
                acount = 5;
                while True:
                    os.system("cls");
                    for i in range(page, len(song)): # 전체 노래 리스트 출력
                        if i != page and i%acount == 0:
                            break;
                        print(f"{song[i]}. {allSong[song[i]][0]} - {allSong[song[i]][1]}");
                        end = i;
                    idx = input("노래 번호 입력 : ");

                    if idx == "이전":
                        if page == 0:
                            print("이전 데이터가 없습니다.");
                            os.system("pause");
                        else:
                            page -= acount;
                    elif idx == "다음":
                        if end+1 == len(song):
                            print("다음 데이터가 없습니다.");
                            os.system("pause");
                        else:
                            page += acount;
                    else:
                        if idx.isdigit() and int(idx) in song:
                            idx = int(idx);
                            break;
                        else:
                            print("없는 노래 번호 입니다.");
                
                print("#### PlayList 목록 ####");
                for i in range(len(playkeys)):
                    print(f"{i+1}. {playkeys[i]}");
                plidx = input("PlayList 선택 : ");

                if plidx.isdigit() and int(plidx)-1 < len(playkeys):
                    if idx in playlist[playkeys[int(plidx)-1]]:
                        print("이미 등록된 곡 입니다.");
                    else:
                        playlist[playkeys[int(plidx)-1]].append(idx);#idx = 노래번호 #plidx = 플레이리스트번호
                        print(f"{playkeys[int(plidx)-1]} 리스트에 {allSong[idx][0]} 등록되었습니다.");
                else:
                    print("없는 PlayList 입니다.");
            else:
                print("선택된 메뉴 번호가 없습니다.");
        else:
            print("없는 메뉴 번호 입니다. 메인 메뉴로 돌아 갑니다.");
    elif select == "8":
        print("MP3 플레이어를 종료합니다.");
        break;
    else:
        print("잘못 입력된 메뉴 번호 입니다. 다시 입력 하세요.");

    os.system("pause");
    os.system("cls");