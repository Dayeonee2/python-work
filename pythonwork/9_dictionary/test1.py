import tkinter

count=0;

def countplus():
    global count;
    count+=1;
    label.config(text=str(count));
    
def countminus():
    global count;
    count-=1;
    label.config(text=str(count));



root = tkinter.Tk();
root.title("테스트 창");
label = tkinter.Label(root, text="0" , width=20,height=10,fg="red",relief="solid");
label.pack(); #화면에 배치
button1= tkinter.Button(root, width=20, height=10, text="plus", overrelief='solid', command=countplus)
button2= tkinter.Button(root, width=20, height=10, text="minus", overrelief='solid', command=countminus)
button1.pack();
button2.pack();
root.geometry("800x600+100+100");
root.resizable(False, True);
root.mainloop();