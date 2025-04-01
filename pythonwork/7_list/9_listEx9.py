ls = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

#얕은 복사(shallow copy) - 참조하는 주소가 동일하고 값이 동일하게 움직인다.
#깊은 복사(deep copy) - 참조하는 주소가 다르고 값만 동일

ls1 = ls[0];

print(f"수정하기 전 ls: {ls[0]}");
print(f"수정하기 전 ls1: {ls1}");

ls1[1]=200;

print(f"수정하기 후 ls: {ls[0]}");
print(f"수정하기 후 ls1: {ls1}");
#같이 수정됨

print(f"ls[0]이 참조하는 주소: {id(ls[0])}")
print(f"ls1이 참조하는 주소: {id(ls1)}")

import copy

ls2 = copy.deepcopy(ls[0]); #import 함수를 써야 copy.~()를 사용할 수 있음
print(f"수정하기 전 ls: {ls[0]}");
print(f"수정하기 전 ls2: {ls2}");

ls2[1]=400;

print(f"수정하기 후 ls: {ls[0]}");
print(f"수정하기 후 ls2: {ls2}");

print(f"ls[0]이 참조하는 주소: {id(ls[0])}")
print(f"ls2이 참조하는 주소: {id(ls2)}")

ls3=ls[0].copy();#deepcopy할 때 주로 사용
ls3[1]=2000

print(f"수정하기 후 ls: {ls[0]}");
print(f"수정하기 후 ls3: {ls3}");

print(f"ls[0]이 참조하는 주소: {id(ls[0])}")
print(f"ls3이 참조하는 주소: {id(ls3)}")