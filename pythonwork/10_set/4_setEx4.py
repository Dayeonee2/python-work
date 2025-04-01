set1={1,2,3};
set2={3,4,5};
set3={1,2,3};


#동일 집합인지를 구분, 모든 요소가 같아야 한다.
if set1==set2: # 다르다
    print("같다");
else:
    print("다르다");
    
if set1==set3: # 같다
    print("같다");
else:
    print("다르다");