def read():
    with open("C:\\20240416\\pythonwork\\17_file\\bbb",'r',encoding='utf-8') as f:
        text = f.readlines();
        for i in text:
            print(i.split(","));
        return text;
        
def add():    
    with open("C:\\20240416\\pythonwork\\17_file\\bbb",'a',encoding='utf-8') as f: # 입력하는 애
        name = input("이름 입력 : ");
        age = input("나이 입력 : ");
        address = input("주소 입력 : ");
        email = input("이메일 입력 : ");
        f.write(f"{name}, {age}, {address}, {email}\n");

def mod():
    text=read();    
    with open("C:\\20240416\\pythonwork\\17_file\\bbb",'w',encoding='utf-8') as f: # 수정
        name = input("이름 입력 : ");
        change='';
        for i in text:
            if name == i.split(",")[0]:
                age = input("나이 입력 : ");
                address = input("주소 입력 : ");
                email = input("이메일 입력 : ");
                change+=f"/n{name}, {age}, {address}, {email}"
            else:
                change+=i
        f.write(change)
        
def rem():
    text = read();
    with open("C:\\20240416\\pythonwork\\17_file\\bbb",'w',encoding='utf-8') as f: # 수정
        name = input("이름 입력 : ");
        change='';
        for i in text:
            if name == i.split(",")[0]:
                print(f"{name} 정보 삭제");
            else:
                change+=i
        f.write(change)

read();
add();
mod();
rem();