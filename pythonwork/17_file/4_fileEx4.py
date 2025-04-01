file = open("C:\\20240416\pythonwork\\17_file\\aaa",'w',encoding="utf-8");

file.write("4번째 줄\n");
# file.write("2번째 줄");
# file.write("3번째 줄");

#close():파일 닫기
file.close()
# 수정 후 파일 닫기를 실행한 후 파일을 다시 불러와야 읽을 수 있음
file = open("C:\\20240416\pythonwork\\17_file\\aaa",'r',encoding="utf-8");

text= file.readlines()
print(text)