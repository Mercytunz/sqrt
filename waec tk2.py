from tkinter import *
waec = Tk()
waec.title("Waec Registry")
waec.geometry("700x700")
waec["bg"]="green"

name = StringVar()
centreNo = StringVar()
subject1 = StringVar()
subject2 = StringVar()
subject3 = StringVar()
subject3 = StringVar()
subject4 = StringVar()
subject5 = StringVar()
subject6 = StringVar()
subject7 = StringVar()
subject8 = StringVar()
subject9 = StringVar()


Label(waec,text = "Waec Registration form",bg = waec["bg"],\
               font = "Calibri 24 bold italic",\
               ).grid(row = 1,column = 1,columnspan =2)

Label(waec, text = "Full Name:",font = "Calibri 13",bg = waec["bg"]).\
              grid(row = 3, column =1,padx = 7, pady = 3)


txtn = Entry(waec, textvariable = name,font = "Calibri 13",\
             width = 30).grid(row = 3,column = 2,padx = 7, pady = 3)

Label(waec, text = "Centre Number:",font = "Calibri 13",bg = waec["bg"]).\
              grid(row = 4, column = 1, padx = 7, pady = 3)


txtr =Entry(waec, textvariable =centreNo,font = "Calibri 13",\
            width = 15).grid(row = 4, column = 2,padx = 7, pady = 3)
            
Label(waec, text = "subjects:",font = "Calibri 13",bg = waec["bg"]).\
              grid(row = 5, column = 1, padx =7, pady = 3)
txtt = Entry(waec, textvariable = subject1, font = "Calibri 13",\
             width =15).grid(row = 5, column = 2,padx =7, pady = 3)
txtt2 = Entry(waec, textvariable = subject2, font = "Calibri 13",\
             width =15).grid(row = 6, column = 2,padx =7, pady = 3)
txtt3 = Entry(waec, textvariable = subject3, font = "Calibri 13",\
             width =15).grid(row = 7, column = 2,padx =7, pady = 3)
txtt4 = Entry(waec, textvariable = subject4, font = "Calibri 13",\
             width =15).grid(row = 8, column = 2,padx =7, pady = 3)
txtt5 = Entry(waec, textvariable = subject5, font = "Calibri 13",\
             width =15).grid(row = 9, column = 2,padx =7, pady = 3)
txtt6 = Entry(waec, textvariable = subject6, font = "Calibri 13",\
             width =15).grid(row = 10, column = 2,padx =7, pady = 3)
txtt7 = Entry(waec, textvariable = subject7, font = "Calibri 13",\
             width =15).grid(row = 11, column = 2,padx =7, pady = 3)
txtt8 = Entry(waec, textvariable = subject8, font = "Calibri 13",\
             width =15).grid(row = 12, column = 2,padx =7, pady = 3)
txtt9 = Entry(waec, textvariable = subject9, font = "Calibri 13",\
             width =15).grid(row = 14, column = 2,padx =7, pady = 3)


























waec.mainloop()
