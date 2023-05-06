from tkinter import *
from tkinter import messagebox
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import docx2pdf

app = Tk()
app.geometry('250x100')
app.resizable(0,0)
app.title("Alkan | DOCX To PDF Converter")
def targetpathway():
    return filedialog.askopenfilename()

def resultpathway():
    return filedialog.askdirectory()
def converter():
    try:
        targettedfile = targetpathway()
        resultpath = resultpathway()

        docx2pdf.convert(targettedfile,resultpath)
        messagebox.showinfo("Alkan | DOCX To PDF Converter",f"Dosya kaydedildi. \n Kaydedilen Dizin: {resultpath}")
    except Exception as e:
        messagebox.showerror("[HATA]","Desteklenmeyen Format! \n .docx uzantılı dosya seçtiğinden emin ol.")

baslik = Label(app,text="Alkan | DOCX To PDF Converter",font ="arial 13 bold",bg="cyan").pack()

convertbutton = ttk.Button(app,text="Çevir",command=converter).place(x=87,y=60)






app.mainloop()
