phonebook = {"홍길동" : "010-1111-1111", '이순신': '010-2222-2222'};
for i in phonebook.keys():
    #i :키값
    #phonebook[i] :값
    print(f"{i} : {phonebook[i]}");
    
if '홍길동' in phonebook.keys():
    print(f" 홍길동 : {phonebook['홍길동']}");

ls= phonebook.keys()
print(type(ls))

if '홍길동' in ls:
    print(f" 홍길동 : {phonebook['홍길동']}");