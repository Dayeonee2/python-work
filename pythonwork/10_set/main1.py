#문제
#0~9 까지의 수 중 컴퓨터가 5개의 숫자를 가지고 있다.
#사용자가 입력한 값에서 컴퓨터가 가진 수를 맞추는 게임
#사용자가 한번 입력할 때마다 맞춘 수의 갯수를 출력해준다.
#순서와 상관없이 있는 숫자로 맞추는 게임

set1={1,4,5,9,0};#컴퓨터 값
set2=set();#사용자 값

import os
while True:
    number=set()
    for i in range(5): 
        num= input("0~ 9 사이의 숫자를 입력하세요 : ");
        if num.isdigit():
            if 0<=int(num)<=9:
                number.add(int(num));
            else:
                print("0~9사이의 숫자로 입력하세요. 처음부터 다시 입력해주세요.")
                break;
        else:
            print("잘못입력하셨습니다. 처음부터 다시 입력해주세요.")
            break;
        
    if len(number)==5:
        set2.update(number);
        
        if set1==set2:
            print(f"정답입니다.");
            break;
        elif set1.isdisjoint(set2):
            print("같은 숫자가 없습니다.")
        else:
            print(f"컴퓨터가 가진 수 와 동일한 숫자는 {len(set1 & set2)} 입니다.")
    
    os.system("pause");
    os.system("cls");