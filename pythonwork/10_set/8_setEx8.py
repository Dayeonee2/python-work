set1={1,2,3};
print(set1);

#remove(값) : 집합에서 요소 제외 - 없는값은 에러
set1.remove(1);
print(set1);

# set1.remove(5) 
# print(set1)

#discard(값) : 값을 집합에서 버린다. - 없는 값도 에러가 나지 않는다.
set2={4,5,6};
set2.discard(4);
print(set2);

set2.discard(9);
print(set2);
