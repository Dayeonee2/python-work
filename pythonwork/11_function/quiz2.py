#아르바이트 월급 계산기
#최저시급:10000원

def time(sub):
    num=int(input(f"{sub}을 입력하세요"));
    return num;
num1=time("시급");
num2=time("일한 시간")

if num1<10000:
    print("최저시급보다 높은 시급을 입력하세요 : ");
else:
    print(f"월급은 {num1*num2*30} 입니다.")
