import random

strList = ["hello","sea","join","song","test","absolute"];

while True:
    n = random.randrange(len(strList));
    str=[];
    for i in (strList[n]):
        str.append(i);
    random.shuffle(str)    
    print(f"정답 {len(strList[n])} 자")
    for i in str:
        print(i,end=' ');
    
    result = input("정답 입력 :")
    
    if strList[n] == result:
        print("정답입니다.");
    else:
        print("틀렸습니다.");