file = open("C:\\20240416\pythonwork\\17_file\\aaa",'w',encoding="utf-8");

file.write("5번째 줄\n");
file.write("6번째 줄\n");

file.close()
file = open("C:\\20240416\pythonwork\\17_file\\aaa",'r',encoding="utf-8");
print(file.readlines())