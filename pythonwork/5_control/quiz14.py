star = int(input("만들 별 수 : "));
for i in range(star):
    num = 1 + (i*2);
    if num < star:
        print(" " * (star-i),"☆" * (num)," " * (star-i)); 
        su = num;
        j = i;
    else : 
        su-=2;
        print(" " * (star-j+1),"☆" * (su)," " * (star-j+1)); 
        j-=1;