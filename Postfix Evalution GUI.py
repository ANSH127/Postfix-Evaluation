from tkinter import *
t=0
x2=''
def call():
    global t,x2,l1,l2
    x2=''
    if t==1:
        l1.destroy()
        l2.destroy()
        
        
    x1=x.get()
    lst1=[]
    p=0
    lst=x1.split()
    #print(lst)
    for i in range(len(lst)):
        if str(lst[i]).isdigit():
            lst1+=lst[i],
            p+=1
           # print(p)
           # print(lst1)
        else:
            y=lst[i]
            
            if y=='+': 
                lst1[p-2]=int(lst1[p-2])+int(lst1[p-1])
                lst1.pop()
                p-=1
                #print(p)
                #print(lst1)
                
            elif y=='-':
                lst1[p-2]=int(lst1[p-2])-int(lst1[p-1])
                lst1.pop()
                p-=1
                #print(p)
                #print(lst1)
            
            
            
            elif y=='*':
                lst1[p-2]=int(lst1[p-2])*int(lst1[p-1])
                lst1.pop()
                p-=1
                #print(p)
               # print(lst1)
               
               
            elif y=='^':
                lst1[p-2]=int(lst1[p-2])**int(lst1[p-1])
                lst1.pop()
                p-=1
                
               
               
               
            else:
                lst1[p-2]=int(lst1[p-2])//int(lst1[p-1])
                lst1.pop()
                p-=1
    #print(lst1)
    l1=Label(root,text='Your Result Is...',font='papyrue 15 bold',bg='yellow',fg='black')
    l1.place(x=130,y=290)        
    t+=1
    for i in lst1:
        x2+=str(i)
        x2+=' '
    l2=Label(root,text=x2,font='papyrue 15 bold',bg='yellow',fg='black')
    l2.place(x=170,y=320)        
        
        













root=Tk()
root.title('Postfix Evalution')
root.geometry('400x400')
root.configure(bg='green2')

Label(root,text='POSTFIX EVALUTION',font='Lato 18 bold',bg='green2',fg='red2').place(x=75,y=60)

Label(root,text='Enter Your Postfix',font='papyrue 10 bold',bg='green2',fg='black').place(x=145,y=130)

x=Entry(root,font=10)
x.place(x=90,y=160)
Button(root,text='SUBMIT',fg='red',bg='black',padx=25,pady=10,command=call).place(x=150,y=210)


Label(root,text='',font='papyrue 10 bold',bg='yellow',fg='black',padx=300,pady=200).place(x=0,y=280)








root.mainloop()