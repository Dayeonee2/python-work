# 파일 내용을 삭제하는 방법

file = open("C:\\20240416\\pythonwork\\17_file\\bbb",'r',encoding='utf-8');

text = file.readlines();

name = input("이름 입력 : ");

change = '';
for i in text: 
    if name in i.split(",")[0]:
        print("있음")
    else:
        change +=i; # 해당줄 제외 하고 저장
        
print(change)

file.close()

file = open("C:\\20240416\\pythonwork\\17_file\\bbb",'w',encoding='utf-8');
file.write(change); # 나머지 다시 쓰기

file.close;