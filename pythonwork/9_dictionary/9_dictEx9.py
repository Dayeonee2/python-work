student = {"학번":1234,"이름":"홍길동","학과":"컴퓨터공학과"};
key=list(student.keys());
value= list(student.values());

for i in range(len(student)):
    print(f"{key[i]} : {value[i]}");
    
for k,v in student.items(): # 키값, 밸류값 불러오기
    print(f"{k} : {v}");
    
for i,(k,v) in enumerate(student.items()): # 이때 k,v는 튜플로 받아짐. 괄호가 있어서
    print(f"{i}. {k} : {v}");
    
ls=student.items(); #dict_items([('학번', 1234), ('이름', '홍길동'), ('학과', '컴퓨터공학과')])
print(ls);

ls=list(student.items()); 
print(ls[0]); #('학번', 1234)

student[ls[0][0]]='학년' #ls[0][0]는 student의 첫번째 키 student의value를 의미
print(student) #{'학번': '학년', '이름': '홍길동', '학과': '컴퓨터공학과'}

student.clear();
print(student);