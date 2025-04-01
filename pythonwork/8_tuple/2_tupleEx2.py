# tuple 에서 값이 하나인 경우에 반드시 뒤에 , 를 붙여야 한다.
tp1= (10);
print(tp1);
tp2= (10,);
print(tp2)
#괄호를 생략하고 , 를 뒤에 붙여도 tuple이 됨
tp3= 10,;
print(tp3);
print(type(tp1));
print(type(tp2));
print(type(tp3));
print(len(tp2))
print(len(tp3))