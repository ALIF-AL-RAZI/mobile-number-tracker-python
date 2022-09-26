from tkinter import *
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier



main_sc= Tk()
main_sc.geometry("500x700+400+80")
main_sc.resizable(False,False)
main_sc.title("Phone Number Tracker")
main_sc.configure(background="#AAF0D1")




def get_location():
    number = str(my_number.get())
    #my_number = "+8801872792494"
    ch_numbr = phonenumbers.parse(number, "CH")
    loc=geocoder.description_for_number(ch_numbr, "en")
    Label(text=loc, font="arial 30 bold", background='#AAF0D1', fg='#2554C7').pack(pady=10)




def get_srvc_prvdr():
    number = str(my_number.get())
    srvc_prvdr = phonenumbers.parse(number, 'RO')
    srvc=carrier.name_for_number(srvc_prvdr, "en")
    Label(text=srvc, font="arial 30 bold", background='#AAF0D1', fg='#2554C7').pack(pady=10)




Label(text="Enter your Number", font="arial 30 bold", background='#AAF0D1',fg='#2554C7' ).pack()
my_number=StringVar()
entry= Entry(main_sc, textvariable=my_number, font="arial 30 bold",width=15).pack(pady=10)

loc_button= Button(main_sc, font= "arial 20", text="Find Location", bg="#111111", fg="white", border=0, command=get_location).pack(pady=30)

serv_button = Button(main_sc, font="arial 20", text="Find Service Provider", bg="#111111", fg="white", border=0,
                        command=get_srvc_prvdr).pack(pady=30)

#Label(text=, font="arial 30 bold", background='#AAF0D1',fg='#2554C7' ).pack()


main_sc.mainloop()