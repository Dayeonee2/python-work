set1={1,2,3,4,5};
set2=set([4,5,6,7,8]);
print(set1 & set2) #{4, 5} 교집합
print(set1.intersection(set2))#{4, 5} 교집합

print(set1 | set2); #{1, 2, 3, 4, 5, 6, 7, 8} 합집합
print(set1.union(set2)); # 합집합

print(set1-set2); #{1, 2, 3} 차집합
print(set2-set1); #{8, 6, 7}
print(set1.difference(set2));
print(set2.difference(set1));


ls1=[1,2,3,4,5];
ls2=[4,5,6,7,8];

# print(ls1 & ls2) # 실행 안됨, 리스트는 교집합이 없다.