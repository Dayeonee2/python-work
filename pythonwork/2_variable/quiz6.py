num1 = 7;
num2 = 5;
print(num1+num2);
print(num1-num2);
print(num1*num2);
print(num1/num2);

kor = 90
eng = 96
math = 93
print(f'total = {kor+eng+math}');
print('average = %.2f'%((kor+eng+math)/3));

#풀이
print('총점 : ', kor+eng+math);
print("평균 : ",(kor+eng+math)/3);#소수점자리 지정 안됨

print("총점 : %d"%(kor+eng+math));
print('평균 = %.2f'%((kor+eng+math)/3));

print("총점 : {} 점".format(kor+eng+math));
print("평균 : {:.2f}점".format((kor+eng+math)/3));

print(f"총점 : {(kor+eng+math)} 점");
print(f"평균 : {(kor+eng+math)/3:.2f}점");
