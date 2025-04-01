#tuple 함수
tp = 100,200,"함수",100,"튜플";
#index()
print(f"tp의 100의 위치 : {tp.index(100)}");
#print(f"tp의 리스트의 위치 : {tp.index("리스트")}");--에러

#count()
print(f"tp 안의 100의 수 : {tp.count(100)}");
print(f"tp 안의 리스트의 수 : {tp.count("리스트")}");