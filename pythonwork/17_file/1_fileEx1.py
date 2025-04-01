#open("파일명", "열기 옵션")
file = open("C:\\20240416\pythonwork\\17_file\\aaa",'r',encoding="utf-8");
#파일 경로 복사 후 \ 두개로 만들기

# file.read() : 파일 내용 가져오기
text = file.read();
print(text);