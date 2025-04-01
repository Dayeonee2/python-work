#open("파일명", "열기 옵션")
file = open("C:\\20240416\pythonwork\\17_file\\aaa",'r',encoding="utf-8");


# file.readlines() : 파일 내용 한줄씩 가져와서 list 로 변환
text = file.readlines();
print(text);

for i in text:
    print(i);