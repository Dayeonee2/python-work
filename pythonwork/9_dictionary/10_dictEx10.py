num={1:'일', 2:'이', 3:'삼'};

num[4]='사';
print(num);
num[4]="4";
print(num);
num.setdefault(5,'오'); # 없으면 삽입
print(num);
num.setdefault(5,"5"); #기존에 있으면 변경되지 않음
print(num);
# {1: '일', 2: '이', 3: '삼', 4: '4', 5: '오'}
# {1: '일', 2: '이', 3: '삼', 4: '4', 5: '오'}