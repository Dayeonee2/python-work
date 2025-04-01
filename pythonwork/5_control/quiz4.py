saveid = 'ekdus';
savepw = '0101';
id= input('아이디 : ');
pw= input('비밀번호 :');

if id == saveid:
    if pw == savepw :
        print('로그인에 성공했습니다.');
    else:
        print("비밀번호가 일치하지 않습니다.");
else:
    print('등록되지 않은 아이디입니다.');