name= input('이름: ');
kor = input('국어 성적 : ');
eng = input('영어 성적 : ');
math = input('수학 성적 : ');
total = int(kor)+int(eng)+int(math);
avg= round(total/3,1)
if 0 <= avg <= 100:
    print(f'합계 = {total} 평균 = {avg}');
    if avg >= 90 :
        print('A');
    elif avg>=80:
        print('B'); 
    elif avg>= 70:
        print('C');
    elif avg>= 60:
        print('D');
    else :
        print('F');
else: 
    print('정확한 성적을 입력하세요.')

print()
print()

dis= int(input("이동 거리(km)를 입력하세요 : "));
main= 3000;
if dis>0:
    if dis>=30:
        dis-=30
        main+=100*dis
    print(f'요금은 {main} 원 입니다.');
else:
    print('다시 입력하세요.')

