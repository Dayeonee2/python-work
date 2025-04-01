class PhoneBook:
    name = '';
    telnum = '';
    email = '';

    def init(self):
        self.name = input("이름 입력 : ");
        self.telnum = input("전화번호 입력 : ");
        self.email = input("이메일 입력 : ");
    def output(self):
        print(f"#### {self.name} ####")
        print(f"전화전호 : {self.telnum}");
        print(f"이메일 : {self.email}");

phoneBookList = [];

for i in range(3):
    p = PhoneBook();
    p.init();
    phoneBookList.append(p);

for i in range(3):
    phoneBookList[i].output();

print(phoneBookList);
# phone1 = PhoneBook();
# phone2 = PhoneBook();
# phone3 = PhoneBook();

# phone1.init();
# phone2.init();
# phone3.init();

# phone1.output();
# phone2.output();
# phone3.output();