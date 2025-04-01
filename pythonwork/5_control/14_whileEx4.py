# break : for문이나 while문의 반복 실행 중에 반복을 종료할 때 사용
# continue: for 문이나 while문의 반복에서 진행하지 않고 처음으로 보낼 때 사용
i=0;
while True:
    if i==3:
        break;
    if i ==2:
        continue;
    # continue 사용은 조심해서 사용해야한다.
    
    print(i)
    i+=1;
else : # 조건이 거짓 실행이기 때문에 무한반복에서는 사용 불가능
    print("while문 종료")