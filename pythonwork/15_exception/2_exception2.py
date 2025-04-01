try:
    num = int(input("정수 입력 : "));
    print(num * num);
    print(num/0); # 0 으로 나눌 수 없다.
    #숫자가 아닌 문자로 넣었을 때 에러 = ValueError
except ValueError as e: # except 만 되어 있으면 else 의 개념;
    print(f"예외 발생 : {e}")
    print("문자는 입력 하시면 안됩니다.");
   
except ZeroDivisionError as e:
    print(f"예외 발생 : {e}");
    print("0으로 나눌 수 없습니다.")
    
except Exception as e: #Exception 은 모든 에러를 포함하는 최상위 개념
    #다른 에러를 사용할 때는 맨 아래에 있어야함. 순서대로 작동하기 때문
    print(f"예외 발생 : {e}");
    print("잘못된 사용으로 에러가 났습니다.")

finally : # try~except 문이 종료되면 반드시 실행되는 부분
    print("예외처리 종료");





