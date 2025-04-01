ls=[10,5,20,7,9,31,12,11,19,32];
odd=[];
even=[];
sumodd=0;
sumeven=0;
for i in range(len(ls)):
    if i%2==0:
        even.append(ls[i])
        sumeven+=ls[i]
    else:
        odd.append(ls[i]);
        sumodd+=ls[i]
print(f"짝수인덱스 : {even}");
print(f"홀수인덱스 : {odd}");
print(f"짝수인덱스의 합 : {sumodd}");
print(f"홀수인덱스의 합 : {sumeven}");
if sumodd>=sumeven:
    print(sumodd-sumeven);
else:
    print(sumeven-sumodd);

inverLs= ls
print(inverLs)

ls.sort()
sortls=ls
print(sortls)

ls.sort(reverse=True)
reversels=ls
print(reversels);

print(ls)
print(inverLs)
print(sortls)
print(reversels)   
#얇은 복사 
        