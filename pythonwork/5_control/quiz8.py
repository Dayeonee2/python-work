ex=int(input('원하는 배수를 입력하세요 : '));

for i in range(1,101):
    if i%ex==0:
    print(i, end='  ');

print();

a1=int(input('첫 번째수를 입력하세요 : '));
a2=int(input('두 번째수를 입력하세요 : '));
sum=0
if a1<a2:
    for i in range(a1,a2+1):
        sum+=i;
elif a2<a1:
    for i in range(a2,a1+1):
        sum+=i;
print(f"두 숫자의 범위의 합은 {sum}입니다.");

#python은 참조 자료형이기 때문에 순서바꾸는게 가능
#if a1>a2:
    # a1,a2=a2,a1
#다른곳에서는 tmp=a1,a1=a2,a2=tmp 위랑 같은 말임<-자바나 씨에서 사용