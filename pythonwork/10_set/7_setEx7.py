set1 = {1,2,3};
set2 = {'a','b','c'};

print(set1);

# set1.update(4,5,6); 에러
# print(set1);


#update() : set에 set을 합친다.
set1.update({4,5,6});
print(set1);


set1.update(set2);
print(set1);

