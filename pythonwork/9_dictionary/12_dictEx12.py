num = {1:'일', 2:'이', 3:'삼'};
#딕셔너리의 키가 필요할 때 fromkeys를 사용
ls=num.fromkeys(num);#{1: None, 2: None, 3: None} 키값만 가져온 딕셔너리 생성
print(ls);
ls2=num.fromkeys(num,1); #{1: 1, 2: 1, 3: 1} 1로 value값이 채워짐
print(ls2);

scores = {20240001: ["이름", 100, 90, 100]};
rank = scores.fromkeys(scores, []);
print(scores);
print(rank);