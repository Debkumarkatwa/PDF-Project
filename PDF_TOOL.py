from pypdf import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

window=Tk()
window.title("All in one pdf tool")
window.geometry("440x200")
# pic = PhotoImage(file = "bg.png")
# lbl=Label(window,image=pic).place(x=0,y=0)
window.configure(bg="dark green")
window.iconbitmap("th.ico")
# window.resizable(False,False)

def file_open():
    
    global fileContents, filename
    filePath = askopenfilename(
        initialdir='C:/', title='Select a File', filetype=(("pdf File", ".pdf"), ("All Files", "*.*")))
    with open(filePath, 'r+') as askedFile:
        fileContents = askedFile.name
    print(fileContents)
    
    filename="" # to get the name of the file
    for i in fileContents[::-1]:
        if i=="/":
            break
        filename+=i
    filename=filename[::-1]
    file_name.set(filename)

def marge_file_open():

    filePath = askopenfilename(
        initialdir='C:/', title='Select a File', filetype=(("pdf File", ".pdf"), ("All Files", "*.*")))
    with open(filePath, 'r+') as askedFile:
        fileContents = askedFile.name
    print(fileContents)
    
    filename="" # to get the name of the file
    for i in fileContents[::-1]:
        if i=="/":
            break
        filename+=i
    filename=filename[::-1]
    file_name_show.insert(0,filename+" , ")
    pathlist.append(fileContents)
    passw.set(str(len(pathlist)))

def reduce_size():
    if fileContents==None:
        messagebox.showerror("Error","Choose a file first")
        return 
    if a.get()=="":
        messagebox.showerror("Error","Enter the name of the file")
        return 

    execute_name = a.get()
    if execute_name.endswith(".pdf") == False:
        execute_name = execute_name+".pdf"

    # print(execute_name)
    pdf_reader = PdfReader(fileContents)
    pdf_writer = PdfWriter()

    for i in pdf_reader.pages:
        pdf_writer.add_page(i)
    pdf_writer.add_metadata(pdf_reader.metadata)

    with open(execute_name, "wb") as write:
        pdf_writer.write(write)
    lb=Label(win,bg="red",fg="white",text="Successfully reduced size of the pdf you gave \nIt saved into your current directory or current path.").pack(padx=10,pady=10)
    pdf_writer.close()
 
def merge_pdf():

    if a.get()=="":
        messagebox.showerror("Error","Enter the name of the file")
        return 
    if len(pathlist) == 0:
        messagebox.showerror("Error","Choose the pdfs correctly")
        return

    pdf_writer = PdfWriter()
    for i in range(len(pathlist)):
        execute_name=a.get()
        if execute_name.endswith(".pdf") == False:
            execute_name = execute_name+".pdf"
        string = pathlist[i]
        with open(string, "rb") as input_1:
            pdf_writer.append(input_1)

    with open(execute_name, "wb") as hello:
        pdf_writer.write(hello)
    pdf_writer.close()
    lb=Label(win,bg="red",fg="white",text="Successfully merged the pdfs you gave \nIt saved into your current directory or current path.").pack()

def encrypt_pdf():
    if fileContents==None:
        messagebox.showerror("Error","Choose a file first")
        return 
    if a.get()=="":
        messagebox.showerror("Error","Enter the name of the file")
        return 
    if passw.get()=="":
        messagebox.showerror("Error","Enter the password")
        return

    pdf_reader = PdfReader(fileContents)
    pdf_writer = PdfWriter()
    execute_name=a.get()
    if not execute_name.endswith(".pdf"):
        execute_name += ".pdf"

    for fuck in pdf_reader.pages:
        pdf_writer.add_page(fuck)

    pdf_writer.encrypt(passw.get())
    with open(execute_name, "wb") as helloworld:
        pdf_writer.write(helloworld)
    lb=Label(win,bg="red",fg="white",text="So the pdf is now successfully encrypted \nIt saved into your current directory or current path.").pack()
    pdf_writer.close()

def decrypt_pdf():
    if fileContents==None:
        messagebox.showerror("Error","Choose a file first")
        return 
    if a.get()=="":
        messagebox.showerror("Error","Enter the name of the file")
        return 
    if passw.get()=="":
        messagebox.showerror("Error","Enter the password")
        return 

    pdf_reader = PdfReader(fileContents)
    execute_name=a.get()
    if not execute_name.endswith(".pdf"):
        execute_name += ".pdf"

    pdf_reader.decrypt(passw.get())
    pdf_writer = PdfWriter()
    for fuck in pdf_reader.pages:
        pdf_writer.add_page(fuck)
    with open(execute_name, "wb") as helloworld:
        pdf_writer.write(helloworld)
    lb=Label(win,bg="red",fg="white",text="So the pdf is now successfully decrypted \nIt saved into your current directory or current path.").pack()
    pdf_writer.close()

def Extract_img():
    reader = PdfReader("addhar.pdf")
    page = reader.pages[0]
    count = 0

    for image_file_object in page.images:
        with open(str(count) + image_file_object.name, "wb") as fp:
            fp.write(image_file_object.data)
            count += 1
    lb=lb=Label(win,bg="red",fg="white",text="The Images of the pdf is now successfully Extracted.\nIt saved into your current directory or current path.").pack()

def next():
    pass

def choose():
    global a,win,file_name,passw,pathlist,file_name_show
    win=Tk()
    win.geometry("440x250")
    win.configure(bg="dark green")
    fr=Frame(win,width=360,height=180,bg="aquamarine",bd=10,relief="ridge")
    fr.place(anchor="center",relx=0.5,rely=0.5)
    #win.resizable(0,0)
    a=StringVar(win)
    passw=StringVar(win)
    file_name=StringVar(win)
    pathlist=[]

    if (drop.get()) =="Reduce size":
        window.destroy()
        win.title("Reduce size")

        # lb1=Label(fr,text="Choose the file").pack()
        file_name_show=Entry(fr,textvariable=file_name,width=40,bd=5,relief="sunken",state="disable")
        file_name_show.pack()
        file_name.set("Choose the file")
        btn=Button(fr,text="Open",command=file_open,bg="aqua",bd=5,relief="ridge").pack()

        lbl0=Label(fr,text="Enter the name of the executed pdf file",bg="aquamarine",bd=5,relief="sunken").pack()
        nn=Entry(fr,textvariable=a,bd=5,relief="sunken").pack()
        btn=Button(fr,text="Submit",command=reduce_size,bg="aqua",bd=5,relief="ridge").pack()     

    elif (drop.get()) =="Merge pdf":
        window.destroy()
        win.title("Merge pdf")

        en0=Entry(fr,textvariable=passw,bd=5,relief="sunken").pack()
        lb1=Label(fr,text="Choose the pdfs one by one",bg="aquamarine",bd=5,relief="sunken").pack()
        
        file_name_show=Entry(fr,width=65)
        file_name_show.pack(padx=5,pady=5)
        btn=Button(fr,text="Open",command=marge_file_open,bg="aqua",bd=5,relief="ridge").pack()

        lb3=Label(fr,text="Enter the name of the executed pdf file",bg="aquamarine",bd=5,relief="sunken").pack()
        en3=Entry(fr,textvariable=a,bd=5,relief="sunken").pack()
        bt=Button(fr,text="submit",command=merge_pdf,bg="aqua",bd=5,relief="ridge").pack()

    elif (drop.get()) =="Encrypt pdf":
        window.destroy()
        win.title("Encrypt pdf")

        # lb1=Label(fr,text="Choose the file").pack()
        file_name_show=Entry(fr,textvariable=file_name,width=40,bd=5,relief="sunken",state="disable")
        file_name_show.pack()
        file_name.set("Choose the file")
        btn=Button(fr,text="Open",command=file_open,bg="aqua",bd=5,relief="ridge").pack()

        lbl0=Label(fr,text="Enter the name of the executed pdf file",bg="aquamarine",bd=5,relief="sunken").pack(padx=5,pady=5)
        nn=Entry(fr,textvariable=a,bd=5,relief="sunken").pack()
        lb4=Label(fr,text="Enter the password",bg="aquamarine",bd=5,relief="sunken").pack()
        en4=Entry(fr,textvariable=passw,bd=5,relief="sunken").pack()
        bt=Button(fr,text="submit",command=encrypt_pdf,bg="aqua",bd=5,relief="ridge").pack()

    elif (drop.get()) =="Decrypt pdf":
        window.destroy()
        win.title("Decrypt pdf")
        
        # lb1=Label(fr,text="Choose the file").pack()
        file_name_show=Entry(fr,width=40,textvariable=file_name,bd=5,relief="sunken",state="disable")
        file_name_show.pack()
        file_name.set("Choose the file")
        btn=Button(fr,text="Open",command=file_open,bg="aqua",bd=5,relief="ridge").pack()

        lbl0=Label(fr,text="Enter the name of the executed pdf file",bg="aquamarine",bd=5,relief="sunken").pack(padx=5,pady=5)
        nn=Entry(fr,textvariable=a,bd=5,relief="sunken").pack()
        lb4=Label(fr,text="Enter the password",bg="aquamarine",bd=5,relief="sunken").pack()
        en4=Entry(fr,textvariable=passw,bd=5,relief="sunken").pack()
        bt=Button(fr,text="submit",command=decrypt_pdf,bg="aqua",bd=5,relief="ridge").pack()

    elif (drop.get()) =="Extract Images":
        window.destroy()
        win.title("Extract Images")

        file_name_show=Entry(fr,textvariable=file_name,width=40,bd=5,relief="sunken",state="disable")
        file_name_show.pack()
        file_name.set("Choose the file")
        bt=Button(fr,text="Open",command=file_open,bg="aqua",bd=5,relief="ridge").pack()
        btn=Button(fr,text="Submit",command=Extract_img,bg="aqua",bd=5,relief="ridge").pack(pady=5)

    else:
        win.destroy()
        messagebox.showerror("Error","Choose correct option")

    win.mainloop()

# main function starts here
frame=Frame(window,width=360,height=180,bg="aquamarine",bd=10,relief="ridge")
frame.place(anchor="center",relx=0.5,rely=0.5)

lbl=Label(frame,text="Welcome to The Application",font=("arial",15,"bold"),bg="aquamarine",bd=5,relief="sunken").pack(padx=5,pady=5)
lbl2=Label(frame,bg="aquamarine",text="Here You are able to ENCRYPT or DECRYPT PDFs\nAlso you can MARGE or RESIZE PDFs",font=("arial",12,"bold"),bd=5,relief="sunken").pack(padx=5,pady=5)
choices=["Reduce size","Merge pdf","Encrypt pdf","Decrypt pdf","Extract Images"]
drop=ttk.Combobox(frame,values=choices,state="readonly",width=20)
drop.set("Choose an option")
drop.pack()
button=Button(frame,text="Submit",command=choose,bg="aqua",bd=5,relief="ridge").pack(padx=5,pady=5)   

window.mainloop()
