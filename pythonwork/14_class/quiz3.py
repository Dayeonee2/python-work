# 문제
# 은행 계좌 
# 1. 입금/출금
# 2. 이체
# 3. 잔액조회
# 4. 계좌 개설
# from random import randrange

# class Bank:
#     name='';
#     number='';
#     account='';
#     def new(self):
#         self.name = input("이름 입력 : ");
#         self.number = input("주민등록번호 입력 : ");
#         for i in range(12):
#             self.account+=str(randrange(1,10));
            
#     def in_(self):
#         self.account= input("본인의 계좌번호 입력 : ");
        
# user=[];#[이름,주민,잔액]        
# dict={};#계좌:[이름,주민,잔액]
# menu = "입금/출금", "이체", "잔액조회", "계좌 개설"

# while True:
#     for i in range(len(menu)):
#         print(f"{i+1}. {menu[i]}")
#     print("0. 종료");
#     select = input("메뉴선택 : ");
#     if select =='4':
#         b=Bank();
#         b.new();
#         user.append[b];
#         print(user)
    
#     elif select == "0":
#         print("프로그램 종료");
#         break;
#     else:
#         print("없는 메뉴 번호 입니다.");
    
class Bank():
    accountNo='';
    name='';
    jumin='';
    balance=0;
    
    def init(self,accountNo,name,jumin):
        self.accountNo=accountNo;
        self.name=name;
        self.jumin=jumin;
    def deposit(self,money):
        self.balance += money;
    def withdrawal(self,money):
        self.balance -= money;
        
menu = "1. 입금/출금", "2. 이체", "3. 잔액조회", "4. 계좌 개설";

bankList=[];

startAcc=10000001;

def inoutMoney(select):
    sub = '출금';
    if select =='1' or select =='2':
        if select =='1':
            sub= '입금';
        accountNo=input("계좌번호 입력 : ");
        i= findAccountNo(accountNo); #findAccountNo 실행 계좌번호 있는지 확인
        if i !=None:
            money = input(f"{sub}액 입력 : ");
            if money.isdigit():
                if select == '1':
                    bankList[i].deposit(int(money));
                elif select == '2':
                    bankList[i].withdrawal(int(money));
                print(f"잔액 : {bankList[i].balance}")
            else:
                print("숫자만 입력 가능합니다.")
    else:
        print("입력한 메뉴 번호가 없습니다.");      
        
def findAccountNo(accountNo):
    for i in range(len(bankList)):
        if int(accountNo) == bankList[i].accountNo:
            return i;
    else:
        print(f"{accountNo} 계좌가 없습니다. 다시 확인하세요.");
        return None;

while True:
    for i in menu:
        print(f"{i}");
    print("0. 종료")
    select = input(" 메뉴 선택 : ");

    if select == "1":
        print("### 입금/출금 ###")
        inoutMoney();
        
        
    elif select =="2":
        print("### 이체 ###");
        sender = input("보내시는분의 계좌번호 입력 : ");
        senderId=findAccountNo(sender);
        if senderId != None:
            print(f"잔액 : {bankList[senderId].balance} 원");
        else:
            continue;
        receiver = input("받는 분의 계좌번호 입력 : ");
        receiverId = findAccountNo(receiver)
        if receiverId != None:
            print(f"잔액 : {bankList[receiverId].name} 원");
        else:
            continue;
        money = input("이체 금액 입력 : ");
        if money.isdigit():
            bankList[senderId].withdrawal(int(money));
            bankList[receiverId].deposit(int(money));
            print("이체가 완료되었습니다.");
        else:
            print("숫자만 입력 가능합니다.")
    elif select == "3":
        print("### 잔액조회 ###");
        sender = input("조회할 계좌번호 입력 : ");
        i=findAccountNo(sender);
        if i!= None:
            print(f"잔액 : {bankList[receiverId].name} 원");

    elif select == "4":
        print("### 계좌 개설 ###");
        name = input("이름 입력 : ");
        jumin = input("주민 번호 입력 : ");
        b=Bank();
        b.init(startAcc,name,jumin);
        bankList.append(b);
        startAcc+=1
        print(bankList);
        
    elif select == "0":
        print("프로그램 종료");
        break;
    else:
        print("입력한 메뉴 번호가 없습니다.")
    
    