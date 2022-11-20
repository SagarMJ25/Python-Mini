from tkinter import *
from tkinter import messagebox as tmsg
root=Tk()
root.geometry("600x625+330+0")
root.minsize(600,625)
root.maxsize(600,625)
root.title("BASIC UNIT CONVERTER")
root.configure(bg="yellow")

def conv():
   if   (ip_value.get()).isalpha()==True:
            msg= tmsg.showinfo("Basic Unit Converter", "Please enter valid numbers")
   elif var.get()==0:
        msg1=tmsg.showinfo('Basic Unit Converter','Please select the unit to convert')
   else:
        if var.get()==1:
           global a 
           a = ip_value.get()
           a  = float(a)
           a = a*1000
        elif var.get()==2:  
            a = ip_value.get()
            a = float(a)
            a = a/1000
        elif var.get()==3:   
          a = ip_value.get()
          a = float(a)
          a = a*1000
        elif var.get()==4:  
          a = ip_value.get()
          a = float(a)
          a=a*1000     
        elif var.get()==5:      
          a = ip_value.get()
          a = float(a)
          a=a*100
        
        elif var.get()==6:
          a = ip_value.get()
          a = float(a)
          a=a*0.394
        
        elif var.get()==7:
           a = ip_value.get()
           a = float(a)
           a = a*60
        
        elif var.get()==8:
          a = ip_value.get()
          a = float(a)
          a = a*60
        
        elif var.get()==9:
          a = ip_value.get()
          a = float(a)
          a = a*3600
        
        elif var.get()==10:
          a = ip_value.get()
          a = float(a)
          a = (a*1.8)+(32)
        
        elif var.get()==11:
          a = ip_value.get()
          a = float(a)
          a = (a-32)/1.8
    
        elif var.get()==12:
          a = ip_value.get()
          a = float(a)
          a = a-273.15
        elif var.get()==13:
            a = ip_value.get()
            a = float(a)
            a = a*1000 
        elif var.get()==14:
            a = ip_value.get()
            a = float(a)
            a = a*1000 
        elif var.get()==15:
            a = ip_value.get()
            a = float(a)
            a = a*0.00134
        elif var.get()==16:
            a = ip_value.get()
            a = float(a)
            a = a*0.278
        elif var.get()==17:
            a = ip_value.get()
            a = float(a)
            a = a*3.6
        elif var.get()==18:
            a = ip_value.get()
            a = float(a)
            a = a*0.0328
        lbx.insert(END,f"{(a)}")  


def reset():
   ipbox.delete(0,END)
   lbx.delete(0,END)
   var.set(0)


#header
f1=Frame(root,bg="red",borderwidth=6)
f1.pack(side=TOP,fill=X)
Label(f1,text="Basic Unit Converter",bg="green",fg="white",font=("lucida 30 bold")).pack(fill=X)
#input side
f2=Frame(root,bg="yellow",borderwidth=6)
f2.pack(side=LEFT,fill=Y)
#input label
ip=Label(f2,text="Enter the value",bg="green", fg="white",font=("lucida 15 bold"),pady=5,padx=15)
ip.grid(row=0,column=0)
#input box
ip_value = StringVar()
ipbox=Entry(f2,borderwidth=3, textvariable=ip_value)
ipbox.grid(ipady=35)

#output side
f3=Frame(root,bg="yellow",borderwidth=6)
f3.pack(side=RIGHT,fill=Y)
#Answer
ans=Label(f3,text="Answer",font=("lucida 15 bold"),bg='green',fg='white',padx=50)
ans.grid(row=0,column=0)
#output box
lbx=Listbox(f3,)
lbx.grid()               

#convert frame
f4=Frame(root,bg="yellow",borderwidth=6)
f4.place(x=250,y=125)
#convert button
cb=Button(f4,text="Convert",bg="green",fg="white",font="lucida 15 bold",command=conv)
cb.grid()

#radio
var=IntVar()

#left frame
f5=Frame(root,bg="yellow",borderwidth=6)
f5.place(x=0,y=200)
mass=Label(f5,text="Mass Conversions",bg='blue',fg='white',font=("lucida 15 bold"))
mass.grid()
Radiobutton(f5,text="Kg--->grams",bg='yellow',font="lucida 10 bold",variable=var,value=1,borderwidth=6 ).grid()
Radiobutton(f5,text="grams--->Kg",bg='yellow',font="lucida 10 bold",variable=var,value=2,borderwidth=6).grid()
Radiobutton(f5,text="grams--->milligrams",bg='yellow',font="lucida 10 bold",variable=var,value=3,borderwidth=6).grid()

length=Label(f5,text="Length Conversions",bg='blue',fg='white',font=("lucida 15 bold"))
length.grid()
Radiobutton(f5,text="Kilometers--->meters",bg='yellow',font="lucida 10 bold",variable=var,value=4,borderwidth=6 ).grid()
Radiobutton(f5,text="meter--->centimeter",bg='yellow',font="lucida 10 bold",variable=var,value=5,borderwidth=6).grid()
Radiobutton(f5,text="centimeter--->inch",bg='yellow',font="lucida 10 bold",variable=var,value=6,borderwidth=6).grid()

pw=Label(f5,text="Current and Voltages",bg='blue',fg='white',font=("lucida 15 bold"))
pw.grid()
Radiobutton(f5,text="ampere--->miliampere",bg='yellow',font="lucida 10 bold",variable=var,value=13,borderwidth=6 ).grid()
Radiobutton(f5,text="volts--->millivolts",bg='yellow',font="lucida 10 bold",variable=var,value=14,borderwidth=6).grid()
Radiobutton(f5,text="watt--->hp",bg='yellow',font="lucida 10 bold",variable=var,value=15,borderwidth=6).grid()


#Right frame
f6=Frame(root,bg="yellow",borderwidth=6)
f6.place(x=410,y=200)
tm=Label(f6,text="Time Conversions",bg='blue',fg='white',font=("lucida 15 bold"))
tm.grid()
Radiobutton(f6,text="hours--->minutes",bg='yellow',font="lucida 10 bold",variable=var,value=7,borderwidth=6).grid()
Radiobutton(f6,text="minutes--->seconds",bg='yellow',font="lucida 10 bold",variable=var,value=8,borderwidth=6).grid()
Radiobutton(f6,text="hours--->seconds",bg='yellow',font="lucida 10 bold",variable=var,value=9,borderwidth=6).grid()


temp=Label(f6,text="Temperature",bg='blue',fg='white',font=("lucida 15 bold"))
temp.grid()
Radiobutton(f6,text="°C--->°F",bg='yellow',font="lucida 10 bold",variable=var,value=10,borderwidth=6 ).grid()
Radiobutton(f6,text="°F--->°C",bg='yellow',font="lucida 10 bold",variable=var,value=11,borderwidth=6).grid()
Radiobutton(f6,text="K--->°C",bg='yellow',font="lucida 10 bold",variable=var,value=12,borderwidth=6).grid()


speed=Label(f6,text="Speed Conversion",bg='blue',fg='white',font=("lucida 15 bold"))
speed.grid()
Radiobutton(f6,text="m/s--->km/hr",bg='yellow',font="lucida 10 bold",variable=var,value=16,borderwidth=6 ).grid()
Radiobutton(f6,text="km/hr--->m/s",bg='yellow',font="lucida 10 bold",variable=var,value=17,borderwidth=6).grid()
Radiobutton(f6,text="cm/s--->ft/s",bg='yellow',font="lucida 10 bold",variable=var,value=18,borderwidth=6).grid()


#close frame
cl=Button(root,text='Reset',bg='black',fg='white',font='lucida 10 bold',command=reset)
cl.place(x=285,y=190)
cb=Button(root,text=" CLOSE ",bg="red",fg="white",font="lucida 15 bold",command=root.destroy)
cb.place(x=260,y=580)


root.mainloop()