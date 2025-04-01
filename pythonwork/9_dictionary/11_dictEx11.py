num={1:"일", 2:"이"};
update={3:'삼', 4:'사'};

print(num);
num.update(update); # 리스트의 extend함수와 같이 두 개의 딕셔너리를 합쳐줌
print(num); #{1: '일', 2: '이', 3: '삼', 4: '사'}

#pop(키값): 해당 키와 값 삭제
num.pop(2);
print(num); #{1: '일', 3: '삼', 4: '사'}