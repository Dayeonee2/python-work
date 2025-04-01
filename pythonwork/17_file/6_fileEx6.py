file = open("C:\\20240416\\pythonwork\\17_file\\bbb",'r',encoding='utf-8');

text=file.readlines();

for i in text: #파일에서 읽어온 데이터의 type은 전부 문자열
    name,age,address,email = i.split(",");
    print(f"{name}\t{age}\t{address}\t{email}",end ='');