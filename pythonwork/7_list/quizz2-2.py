add=[[],[],[],[],[],[],[],[],[]]
import random
for i in range(9):
    for j in range(9):
        add[i].append(random.randrange(1,100))
        #랜덤하게 91개 뽑기
print()
for i in range(len(add)):
    print(add[i]);#9*9로 출력
import copy
addTest = copy.deepcopy(add);

max_=[]    
for i in range(len(add)):
    add[i].sort(reverse=True);
    max_.append(add[i][0]);
      
max_.sort(reverse=True);
max = max_[0];
print()
print(max_)
print()
print(max)

for i in range(len(addTest)):
    if max in addTest[i]:
        print(f"max는 {i+1}행 {addTest[i].index(max)+1}열")
       
min_=[]    
for i in range(len(add)):
    add[i].sort();
    min_.append(add[i][0]);
    
min_.sort();
min = min_[0];
print()
print(min_)
print()
print(min);

for i in range(len(addTest)):
    if min in addTest[i]:
        print(f"min는 {i+1}행 {addTest[i].index(min)+1}열")   