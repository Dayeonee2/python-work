class TextError(Exception):
    def __init__(self):
        super().__init__("내가 출력하고자 하는 에러 메시지");
try:
    num = input("입력 : ")
    if not num.isdigit():
        raise TextError;
    print(num);
except TextError as t:
    print(t);