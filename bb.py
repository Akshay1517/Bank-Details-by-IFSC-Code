from Tkinter import *
import Tkinter
import json
import requests

def mainloop():
    root1 = Tk()
    root1.geometry("1500x880")
    root1.configure(background='#34495E')
    # photo = PhotoImage(file="2.gif")
    # w = Label (root1, image=photo)
    # w.place(x=0, y=0, relwidth=1, relheight=1)
    # w.photo = photo
    # w.pack()

    L1 = Label(root1, text="BANK", bg='black', fg='#36FD01', font=("Comic Sans MS", 25))
    L1.pack(anchor=CENTER)
    L1.place(height=70, width=300, x=540, y=50)

    B = Tkinter.Button(root1, text ="ENTER BANK IFSC CODE",cursor='plus',command=lambda:acnum(root1), activebackground='#01F5FD', activeforeground='blue', bd=10, bg='black', fg='#01F5FD', font=("Arial Black", 15))
    B.pack()
    B.place(bordermode=OUTSIDE, height=60, width=350, x=520, y=250)

    root1.mainloop()


def acnum(root1):
    root1.destroy()
    root = Tk()
    root.geometry("1500x880")
    root.configure(background='Black')
    L1 = Label(root, text="ENTER IFSC CODE HERE", bg='black', fg='#36FD01', font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=50, width=350, x=400, y=253)
    E8 = Entry(root, bd =5, font=("Hoefler Text", 19))
    E8.pack(anchor=CENTER)
    E8.place(height=55, width=300, x=800, y=250)
    B2 = Tkinter.Button(root, text ="ENTER",cursor='man', activebackground='#01F5FD',command=lambda:enter(E8), activeforeground='blue', bd=10, bg='black', fg='#36FD01', font=("Arial Black", 18))
    B2.pack(expand=True, fill='both')
    B2.place(height=60, width=250, x=600, y=400)

def enter(E8):
    value=E8.get()
    root2 = Tk()
    root2.geometry("1500x880")
    root2.configure(background='Black')
    str1 = "https://ifsc.razorpay.com/"
    fs = str1 + value
    # request = Request('fs')
    # response = urlopen(request)
    # kittens = response.read()
    # response = urllib2.urlopen(fs) 
 #    print ('response headers: "%s"' % response.info())
    # response = requests.get(fs)
    # print(response)
    # with urllib.request.urlopen(fs) as response:
    #    html = response.read()
    # mystr= html.decode('utf8')
    # print(type(mystr))
    # print(mystr)
    # try:
    #     l=eval(mystr)
    #     print(type(l))
    #     print(l["BANK"])
    # except:
    #     print("1")
    # L1 = Label(root2, text=m, bg='black', fg='#36FD01', font=("Comic Sans MS", 12))
    # L1.pack(anchor=CENTER)
    # L1.place(bordermode=OUTSIDE, height=50, width=500, x=400, y=253)

    req = requests.get(fs)
    # req.decode('utf-8')
    a=req.json()
    # print(a["BANK"])
    print("1")

    L1 = Label(root2, text="BANK NAME", font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=150, x=300, y=200)

    L1 = Label(root2, text=a["BANK"], font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=220, x=500, y=200)

    L1 = Label(root2, text="BRANCH", font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=150, x=300, y=250)

    L1 = Label(root2, text=a["BRANCH"], font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=300, x=500, y=250)

    L1 = Label(root2, text="ADDRESS", font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=150, x=300, y=300)

    L1 = Label(root2, text=a["ADDRESS"], font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=900, x=500, y=300)

    L1 = Label(root2, text="CITY", font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=150, x=300, y=350)

    L1 = Label(root2, text=a["CITY"], font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=150, x=500, y=350)

    L1 = Label(root2, text="IFSC", font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=100, x=300, y=400)

    L1 = Label(root2, text=a["IFSC"], font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=150, x=500, y=400)

    L1 = Label(root2, text="BANK CODE", font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=150, x=300, y=450)

    L1 = Label(root2, text=a["BANKCODE"], font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=150, x=500, y=450)

    L1 = Label(root2, text="STATE", font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=150, x=300, y=500)

    L1 = Label(root2, text=a["STATE"], font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=150, x=500, y=500)

    L1 = Label(root2, text="CONTACT NO", font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=150, x=300, y=550)

    L1 = Label(root2, text=a["CONTACT"], font=("Comic Sans MS", 12))
    L1.pack(anchor=CENTER)
    L1.place(bordermode=OUTSIDE, height=30, width=150, x=500, y=550)

    L1 = Label(root2, text="BANK DETAILS", bg='black', fg='#36FD01', font=("Comic Sans MS", 25))
    L1.pack(anchor=CENTER)
    L1.place(height=70, width=300, x=540, y=50)






mainloop()