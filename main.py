from tkinter import *
import socket
from tkinter import filedialog 
from tkinter import messagebox 
import os
import tkinter as tk
from tkinter import ttk


root=Tk()
root.title("Shareit")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable (False, False) 

var=tk.StringVar()
var.set("Selected File")
def Send():
   window=Toplevel(root)
   window.title("send")
   window.geometry('450x560+500+200')
   window.configure(bg='#f4fdfe')
   window.resizable(False,False)
   
   def select_file():
       global filename
       filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                       
       title='Select Image File',
       filetype=(('file_type','.*'), ('all files','.*')))
       var.set(str(filename).split("/")[-1])
       
       
   
      

   def sender():
       s=socket.socket()
       host=socket.gethostname()
       port=8080
       s.bind((host, port))
       s.listen(1)
       print(host)
       print('waiting for any incoming connections....')
       conn, addr=s.accept()
       file=open(filename, 'rb')
       file_data=file.read(6048576)
       conn.send(file_data)
       var.set("Successful Transfered")
       print("Data has been transmitted successfully..")

#icon
   image_icon1=PhotoImage(file="Image/send.png") 
   window.iconphoto (False, image_icon1)
   Sbackground=PhotoImage(file="Image/sender.png")
   Label (window, image=Sbackground).place (x=-2,y=0)
   Mbackground=PhotoImage(file="Image/id.png")
   Label (window, image=Mbackground, bg='#f4fdfe').place(x=100,y=260)
   Label(window, textvariable=f'{var}',border=0,fg='black',bg='#12b2f1', font=('Microsoft Yahei UI Light',12, 'bold')).place(x=135,y=100)
   host=socket.gethostname()
   Label(window, text=f'ID:{host}',bg='white',fg='black').place(x=140,y=290)
   

   Button (window, width=15,pady=7, text='Select File', bg='#4E0CDD',fg= 'white', border=0,command=lambda:[select_file()]).place(x=160,y=150)
   Button (window, width=15,pady=7, text='Send', bg='#4E0CDD',fg= 'white', border=0,command=sender).place(x=300,y=150)

   window.mainloop()


def Receive():
   global drop
   main=Toplevel (root) 
   main.title("Receive")
   main.geometry('450x560+500+200')
   main.configure(bg="#f4fdfe")
   main.resizable (False, False)

   def receiver():
      ID=menu.get()
      filename1=incoming_file.get()
      s=socket.socket()
      port=8080
      s.connect((ID, port))
      file=open(filename1, 'wb')
      file_data=s.recv(6048576)
      file.write(file_data)
      file.close()
      Label (main, text="Select sender id", fg='#371065',bg='#f4fdfe', font=('Microsoft Yahei UI Light',12, 'bold')).place(x=130,y=220)
      print("File has been received successfully")

  


#icon
   image_icon1=PhotoImage(file="Image/receive.png") 
   main.iconphoto (False, image_icon1)
   Hbackground=PhotoImage(file="Image/receiver.png")
   Label (main, image=Hbackground).place(x=-2,y=0)
   logo=PhotoImage(file="Image/profile.png")
   Label (main, image=logo, bg="#f4fdfe").place(x=10,y=250)
   Label (main, text="Receive", font=('arial', 20), bg="#f4fdfe").place(x=100,y=280)
   Label (main, text="Select sender id", fg='#371065',bg='#f4fdfe', font=('Microsoft Yahei UI Light',12, 'bold')).place(x=20,y=340)

   menu= StringVar()   
   drop= ttk.Combobox(main,textvariable=menu,width=27)
   drop["values"]=("MSI","DESKTOP-612LELU")
   drop.place(x=20,y=370)
   drop.focus()
   Label (main, text="Enter file Name (with extn)", fg='#371065',bg='#f4fdfe', font=('Microsoft Yahei UI Light',14, 'bold')).place(x=20,y=420)
   incoming_file=Entry (main,width=25, fg='black', border=0, bg='#f4fdfe',font=('Microsoft Yahei UI Light',11))
   incoming_file.place(x=20,y=450)
   Frame(main,width=208, height=2, bg='black').place(x=20,y=475)

   rr=Button(main,width=15,pady=7, text='Recieve', bg='#57a1f8',fg= 'white', border=0, command=receiver) 
   rr.place(x=20,y=500)
   
   
   #Button(main,width=15,pady=7, text='Add more ID', bg='#f4fdfe',fg= '#57a1f8', border=0,command=add).place(x=310,y=390)

   main.mainloop()

image_icon=PhotoImage(file="Image/icon.png")
root.iconphoto (False, image_icon)
Label (root, text="File Transfer", fg='#57a1f8',bg='white', font=('Microsoft Yahei UI Light',18, 'bold')).place(x=20,y=30)
Frame (root, width=400, height=2, bg="#f3f5f6").place(x=25,y=80)
send_image=PhotoImage(file="Image/send.png")
send=Button(root, image=send_image, bg="#f4fdfe", bd=0, command=Send) 
send.place(x=50,y=100)
receive_image=PhotoImage(file="Image/receive.png")
receive=Button (root, image=receive_image, bg="#f4fdfe", bd=0,command=Receive) 
receive.place(x=300,y=100)
#label
Label (root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=65,y=200) 
Label(root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=300,y=200)

background = PhotoImage(file="Image/background.png")
Label(root,image=background).place(x=2,y=323)

root.mainloop()