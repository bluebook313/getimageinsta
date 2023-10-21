from tkinter import *
from instaloader.instaloader import *
from urllib.request import urlopen
import urllib
from PIL import Image,ImageTk
import io


window = Tk()

window.maxsize(1300,700)
window.minsize(400,400)
window.geometry('800x600')
window.title(" mohammad yasin")

def get_pic():
    L = Instaloader()
    profile_insta= Profile.from_username(L.context,str(input.get()))
    pic_url = profile_insta.get_profile_pic_url()
    a = urlopen(pic_url)
    data = a.read()
    a.close()
    image = Image.open(io.BytesIO(data))
    pic = ImageTk.PhotoImage(image)
    lablePicture.config(image=pic)
    lablePicture.image = pic
    lablePicture.pack()








Label(text='put your username to see your picture !!! ' ,fg='black').pack()
input = Entry(window)
input.pack()


lablePicture = Label(window)
lablePicture.pack()

btn = Button(window,text='send',fg = 'red' , bg='yellow',command=get_pic)
btn.pack()


















window.mainloop()






