import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
import pandas as pd



window = Tk()
window.geometry("400x600")
window.title("WEB SCRAPER")
window.config(background="black")



def url_locater():

    url = new_url.get()
    tag = new_tag.get()
    class_1 = new_class.get()

    if not url.startswith("https://"):
        url = "http://" + url

    r =requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all(tag, class_= class_1)
    names = []

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve the page: {e}")
        return

    for i in links:
        info = i.text
        names.append(info)

    panda = pd.DataFrame({"product names":names})


    panda.to_csv("New_wala.csv")


#####################
label_1 = Label(window,
              font=('arial',30,'italic'),
              fg="white",bg='black',
              text="URL",
              relief="sunken",
               bd =10,
              )
label_1.place(x=150,y=200)
########################
label_2 = Label(window,
              font=('arial',15,'italic'),
              fg="white",bg='black',
              text="TAG::",
              relief="sunken",
              bd =4,
              )
label_2.place(x=150,y=350)
########################
label_3 = Label(window,
              font=('arial',15,'italic'),
              fg="white",bg='black',
              text="CLASS::",
              relief="sunken",
              bd =4,
              )
label_3.place(x=150,y=400)


#####################button
my_button = Button(window,
                text="SCRAPE",
                command = url_locater,
                relief="raised",
                bd=10,

                )
my_button.place(x=170,y=450)

new_tag = Entry(window,width=5,bg="white")
new_tag.place(x=250,y=360)

new_class = Entry(window,width=5,bg="white")
new_class.place(x=250,y=400)

new_url = Entry(window,width=25,bg="white")
new_url.place(x=120,y=300)



window.mainloop()
