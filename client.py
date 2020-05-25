import json, requests
import sentry_sdk
from sentry_sdk import configure_scope
import logging

sentry_sdk.init("https://f8774516c21f40938838bfe22005ae38@o392992.ingest.sentry.io/5252335")

with configure_scope() as scope:
    scope.set_tag("Project", "IKSiS")
    scope.set_tag("Lab", "3")

try:
    r=requests.get("http://127.0.0.1:5000/CollectionApi")
    if r.status_code == 200:
        post=r.json()
        self.inf(post)
                else:
                    logging.error("Connection error")
                    lbl.config(text="Connection error: " +str(r.status_code))
            except requests.exceptions.ConnectionError as e:
                sentry_sdk.capture_exception(e)
                r="The destination computer rejected the connection request"
                lbl.config(text=r, wraplength=200)

global lbl, lbl1

class Cont():
    def __init__(self, root):
        self.root=root
        self.post=""

    def config(self):
        self.but = Button(self.root, text="FIND", command=lambda: self.ok()).place(x=250, y=0)

    def ok(self):
        if variable.get()== "Select title":
            lbl.config(text="First select a title")
        else:
            try:
                r=requests.get("http://127.0.0.1:5000/CollectionApi")
                if r.status_code == 200:
                    self.post=r.json()
                    self.inf(self.post)
                else:
                    logging.error("Connection error")
                    lbl.config(text="Connection error: " +str(r.status_code))
            except requests.exceptions.ConnectionError as e:
                sentry_sdk.capture_exception(e)
                r="The destination computer rejected the connection request"
                lbl.config(text=r, wraplength=200)

    def inf(self, post):
        if lbl != " ":
            lbl.config(text=" ")
        j=2
        for i in range(len(self.post["_items"])):
            if variable.get() == self.post["_items"][i]["post"]["title"]:
                lbl1 = Label(self.root, text="Username: " +str(self.post["_items"][i]["userName"])).place(x=50, y=20+j*20)
                lbl1 = Label(self.root, text="Post Content: " +str(self.post["_items"][i]["post"]["content"])).place(x=50, y=40+j*20)
                j+=2
    
root = Tk()
root.title("DATA")
root.geometry('500x500')
root.resizable(width=False, height=False)

variable = StringVar(root)
variable.set("Select title")
w = OptionMenu(root, variable, "Title1", "Title2", "Title3").place(x=150, y=0)
lbl=Label(root, text=" ")
lbl.place(x=150, y=100)

x=Cont(root)
x.config()

root.mainloop()
