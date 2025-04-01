# 문제 
# MP3 플레이어 만들어 보기
# 1. 재생 2. 정지 3. 다음곡 4. 이전곡 5. 곡 추가 6. 곡 삭제 0. 종료

# 음악을 저장하는 리스트
index = 0; # 현재 재생중인 노래 키 값 저장
start=[];
playlist={} 
stop=False
com=True
song = {
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
import os #콘솔 제어
while True:
    keys=list(song.keys())
    if stop:
        print("###################");
        print("####### ■  ########");
        print("###################");
        print(f"{start[1]} - {start[0]}");
    elif len(start) != 0: 
        print("###################");
        print("####### ▷  ########");
        print("###################");
        print(f"{start[1]} - {start[0]}");
    print("1. 재생 2. 정지 3. 다음곡 4. 이전곡 5. 곡추가 6. 곡삭제 7. 플레이리스트 0. 종료");
    select = input("메뉴 선택 : ");
    
    if select == "1":
        if len(start) == 2 and stop:
            stop = False;
        else:
            for i in song.keys():
                print(f"{i}. {song[i][1]} - {song[i][0]}")
            select = input("재생할 노래 번호 입력 : ");
            if select.isdigit():
                if int(select) in keys:
                    start= song[int(select)]
                    index=int(select)
                    stop=False;
                else:
                    print('없는 노래 번호입니다.')
    elif select == "2":
        print(f"{start[1]} - {start[0]} 정지");
        stop=True
    elif select == "3": # song의 키를 저장한 keys index활용해야함
        idx=keys.index(index)
        if len(song)==0:
            print(f"재생 목록이 없습니다.");
        elif idx==len(keys)-1:  # 즉 키값을 길이==키 index의 길이
            index=keys[0]
        else: ## 1 5 7 9
            index=keys[idx+1];
        start = song[index];#song의 index키값의 value
        print(f"다음곡 : {start[1]} - {start[0]}");
    elif select == "4":
        idx=keys.index(index)
        if len(song)==0:
            print(f"재생 목록이 없습니다.");
        else:
            index=keys[idx-1];#키값의 인덱스
            if index==0:
                index=keys[len(keys)-1];
        start = song[index];
        print(f"이전곡 : {start[1]} - {start[0]}");
    elif select == "5":
        print("######곡추가######");
        singer=[];
        singer.append(input("가수 이름 입력 : "));
        singer.append(input("제목 입력 : "));
        singer[0],singer[1]=singer[1],singer[0]
        song[len(song)+1]=singer;
        for i in song.keys():
            print(f"{i}. {song[i][1]} - {song[i][0]}")        
    elif select == "6":
        print("######곡삭제######");
        for i in song.keys():
                print(f"{i}. {song[i][1]} - {song[i][0]}")
        subject = input("삭제할 제목 입력 : ");
        for i in range(len(song)):
            if subject == song[i+1][0]:
                print(f"{subject} 곡을 삭제합니다.");
                song.pop(i+1)
                com=False
        if com==True:
            print("해당하는 곡이 존재하지 않습니다.")#자꾸 출력됨, 해당키 삭제후 키가 빈다.
    elif select == "7":
        print('1. 플레이리스트 추가 2. 플레이리스트 삭제 3. 플레이리스트 출력 4. 플레이리스트 재생')
        selec=input('메뉴 입력 : ');
        key=list(playlist.keys())
        if selec=='1':
            name=input('플레이리스트 이름 입력 : ');  
            for i in song.keys():
                print(f"{i}. {song[i][1]} - {song[i][0]}")
            while True:
                num=input('저장하고 싶은 곡의 번호를 입력하세요(0을 누루면 종료됩니다.) : ')
                if num.isdigit():
                    if int(num)==0:
                        break;
                    elif int(num) in list(song.keys()):
                        if playlist.get(name) == None:                           
                            playlist[name]=[int(num)]
                        else:
                            playlist[name].append(int(num));
                    else:
                        print('해당 번호의 곡이 존재하지 않습니다.')
                else:
                    print('숫자로 입력하세요.')
            print(playlist)    
        elif selec=='2':
            print("#### 플레이 리스트 목록 ####"); 
            for i in range(len(key)):
                print(f"{i+1} : {key[i]}")
            name=input('플레이리스트 이름 입력 : ');
            if name in key:
                playlist.pop(name);
            else:
                print('해당하는 플레이리스트는 없습니다.')
        elif selec=='3':
            if len(playlist)> 0:
                for i in range(len(key)):
                    print(f"{i+1} : {key[i]}")
            else:
                print('존재하는 플레이리스트가 없습니다.')
        elif selec=='4':
            for i in range(len(key)):
                print(f"{i+1} : {key[i]}")
            choose= input('재생할 플레이리스트를 선택하세요 : ');
            
            if choose in key:
                for i in range(len(playlist[choose])):
                    print(f"{playlist[choose][i]}. {song[playlist[choose][i]][1]} - {song[playlist[choose][i]][0]}")
                select = input("재생할 노래 번호 입력 : ");
                if select.isdigit():
                    if int(select) in playlist[choose]:
                        start= song[int(select)]
                        index=int(select)
                        stop=False;
                    else:
                        print('없는 노래 번호입니다.')
                else:
                    print('숫자로 입력해주세요.')
            else:
                print('존재하지 않는 플레이리스트입니다.')
                
        else:
            print("선택된 메뉴가 없습니다.")    
    elif select == "0":
        print("MP3를 종료합니다.");
        break;
    else :
        print("선택된 메뉴가 없습니다.");
    os.system("pause");
    os.system("cls");