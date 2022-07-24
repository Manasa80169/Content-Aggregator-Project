from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import math,os
class News_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("CONTENT AGGREGATOR ")
        bg_color="#074465"
        title=Label(self.root,text="CONTENT AGGREGATOR  SOFTWARE",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=============Variables======================
        #=============News Update======================
        
        #self.Sports=StringVar()
        #self.political=StringVar()
        #self.education=StringVar()
        #self.economical=StringVar()
        #self.search_news=StringVar()
        #self.find_news=IntVar()
        #self.textarea=StringVar()
                
                
        #=============CONTENT AGGREGATOR SEARCH================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="CONTENT AGGREGATOR SEARCH",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=90,relwidth=1)

           
        news_lbl=Label(F1,text="News Search",fg="white",bg=bg_color,font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=5)
        #news_txt=Entry(F1,width=11,textvariable=self.search_news,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        news_btn=Button(F1,text="Search",command=self.find_news,width=10,bd=7,font="arial 12 bold").grid(row=0,column=1,padx=50,pady=10)
        
        #=============Select news================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Select news",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=3,y=205,width=325,height=380)
        sports_btn=Button(F2,text="Sports News",command=self.Sports,width=15,bd=7,font="arial 12 bold").grid(row=0,column=0,padx=50,pady=10)
        political_btn=Button(F2,text="Political News",command=self.Political,width=15,bd=7,font="arial 12 bold").grid(row=1,column=0,padx=50,pady=10)
        education_btn=Button(F2,text="Education News",command=self.Education,width=15,bd=7,font="arial 12 bold").grid(row=2,column=0,padx=50,pady=10)
        economical_btn=Button(F2,text="Economical News",command=self.Economical,width=15,bd=7,font="arial 12 bold").grid(row=3,column=0,padx=50,pady=10)
        Exit_app=Button(F2,text="Exit News",command=self.Exit_app,width=15,bd=7,font="arial 12 bold").grid(row=4,column=0,padx=50,pady=10)
        
           
        #=============News Display================
        F3=Frame(self.root,bd=10,relief=GROOVE)
        F3.place(x=350,y=205,width=850,height=450)
        news=Label(F3,text="Display News",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F3,orient=VERTICAL)
        self.textarea=Text(F3,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #=============Bottom Frame================
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Developed by Ms. Manasa",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=0,y=600,width=325,height=50)
    
        #=============file Code================

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()

    
    def Sports(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t \t SPORTS NEWS CONTENT AGGREGATOR \n \n")
        sports_btn=open("sports.txt",'r')
        f=sports_btn.read()
        self.textarea.insert(END,f)
        sports_btn.close()
        
    def Political(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t \t POLITICAL NEWS CONTENT AGGREGATOR \n \n")
        political_btn=open("political.txt",'r')
        f=political_btn.read()
        self.textarea.insert(END,f)
        political_btn.close()

    def Education(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t EDUCATIONAL NEWS CONTENT AGGREGATOR  \n\n ")
        education_btn=open("education.txt",'r')
        f=education_btn.read()
        self.textarea.insert(END,f)
        education_btn.close()

    def Economical(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t \t ECONOMICAL NEWS CONTENT AGGREGATOR \n \n")
        economical_btn=open("economical.txt",'r')
        f=economical_btn.read()
        self.textarea.insert(END,f)
        economical_btn.close()

    
    def find_news(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t \t NEWS CONTENT AGGREGATOR \n \n")
        news=filedialog.askopenfilename(initialdir = ("C:/Users/ADI-EPCH/Desktop/Project"),title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
        news_btn=open(news,'r')
        f=news_btn.read()
        self.textarea.insert(END,f)
        news_btn.close()

root=Tk()
obj=News_App(root)

root.mainloop()
