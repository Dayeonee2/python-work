a=0;
for i in range(5):
    for j in range(5):
        a+=1
        print("%3d"%a,end='');
    print()
#선생님 풀이
for i in range(1,26):
    if i%5==0:
        print("%3d"%i);
    else: 
        print("%3d"%i,end='');


for i in range(5):
    for j in range(1,6):  
            print("%3d"%(i*5+j),end='');
    print();

for i in range(5):
    for j in range(5):
            if i%2==0:
                print("%3d"%(i*5+j),end='');
            else:
                print("%3d"%(i*10-j),end='');
    print()


##선생님 풀이
for i in range(5):
    for j in range(0,5):
            if i%2==0:  
                print("%3d"%(i*5+j+1),end='');
            else: 
                print("%3d"%(i*5+5-j),end='');
    print();
