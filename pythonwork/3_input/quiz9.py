f1 = input('첫번째 물건 무게 입력 :');
f2 = input('두번째 물건 무게 입력 :');
print(f'현재 남은 무게 : {600-(float(f2)+float(f1)):.1f} kg')

name = input("이름 입력 : ");
kor = input("국어 점수 입력 : ");
eng = input("영어 점수 입력 : ");
math = input("수학 점수 입력 : ");
print('='*10,'학생 정보','='*10);
print("이름\t국어\t영어\t수학\t합계\t평균");
print(f'{name}\t{kor}\t{eng}\t{math}\t{int(kor)+int(eng)+int(math)}\t{(float(kor)+float(eng)+float(math))/3:.6f}')
