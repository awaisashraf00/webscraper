import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
import pandas as pd



window = Tk()
window.geometry("400x600")
window.title("WEB SCRAP")
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
Label(window, text="Class:", font=('Arial', 12), fg="white", bg="black").grid(row=3, column=0, sticky=E, padx=10, pady=5)
########################
Label(window, text="Tag:", font=('Arial', 12), fg="white", bg="black").grid(row=2, column=0, sticky=E, padx=10, pady=5)
########################
Label(window, text="URL:", font=('Arial', 12), fg="white", bg="black").grid(row=1, column=0, sticky=E, padx=10, pady=5)


#####################button
my_button = Button(window,
                text="SCRAPE",
                command = url_locater,
                relief="raised",
                bd=10,

                )
my_button.place(x=170,y=450)

new_tag = Entry(window, width=30)
new_tag.grid(row=2, column=1, padx=50, pady=60)

new_class = Entry(window, width=30)
new_class.grid(row=3, column=1, padx=50, pady=10)

new_url = Entry(window, width=30)
new_url.grid(row=1, column=1, padx=50, pady=10)



window.mainloop()
