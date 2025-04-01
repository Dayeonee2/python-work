set1={1,2,3,4,5}
set2={4,5,6,7,8}
set3={1,2,3,4,5}
set4={6,7,8,9,10}

if set1.isdisjoint(set2):
    print("set1과 set2는 같은 요소가 하나도 없다.");
else:
    print("set1과 set2는 같은 요소가 하나는 있다.");
    
if set1.isdisjoint(set3):
    print("set1과 set3는 같은 요소가 하나도 없다.");
else:
    print("set1과 set3는 같은 요소가 하나는 있다.");
    
    
if set1.isdisjoint(set4):
    print("set1과 set4는 같은 요소가 하나도 없다.");
else:
    print("set1과 set4는 같은 요소가 하나는 있다.");
    