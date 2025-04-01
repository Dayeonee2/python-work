num1=320.00
num2=520.33
print('건물의 높이 =', round((num1*14+num2)/100,1),'m 입니다.');

#풀이
height= num1*14+num2
print('건물의 높이 = %.1fm 입니다.'%(height/100));
print('건물의 높이 = {}m 입니다.'.format(round(height/100,1)));
print(f'건물의 높이는 {round(height/100,1)}m 입니다.');