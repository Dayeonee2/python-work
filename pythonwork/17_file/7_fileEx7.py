#파일에 입력(저장)하는 방법
file = open("C:\\20240416\\pythonwork\\17_file\\bbb",'a',encoding='utf-8');


name = input("이름 입력 : ");
age = input("나이 입력 : ");
address = input("주소 입력 : ");
email = input("이메일 입력 : ");

file.write(f"{name},{age},{address},{email}\n");

file.close();