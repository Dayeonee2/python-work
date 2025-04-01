ls = [10,20,30];
ls.append(40);
print(f"추가 후 ls : {ls}");


# pop() : 마지막 데이터를 제거하고 반환
print(f"pop() 으로 마지막 데이터 삭제 : {ls.pop()}");
print(f"삭제 후 ls : {ls}");


ls1=[1,5,3,2,4];
# reverse() : 역순으로 변경
ls1.reverse();
print(f"역순 변경 후 ls1 : {ls1}");
# sort() : list의 값을 정렬한다. - 오름차순
ls1.sort()
print(f"sort() 함수로 정렬된 ls1 : {ls1}");

# sort(reverse=True) : 내림차순
ls1.sort(reverse=True)
print(f"sort() 함수로 정렬된 ls1 : {ls1}");

# del() : 데이터를 제거하는 함수
del(ls1[1]);
print(f"del(ls[1]) 후의 ls1 : {ls1}");

