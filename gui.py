from tkinter import *
from PIL import ImageTk, Image
import cartoonifyimg as ci
import cartoonifyvid as cv
import sketchifyimg as si
import sketchifyvid as sv

def image():
    ci.cartoonimg()
def video():
    cv.cartoonvid()
def skimage():
    si.sketchimg()
def skvideo():
    sv.sketchvid()
    
window=Tk()
window.geometry('450x450')
window.title('Cartoonify And Sketchify Your Images and Videos!')
window.configure(background='white')
label=Label(window,background='#CDCDCD', font=('calibri',30,'bold'))

#Create canvas
my_canvas = Canvas(window,width=450,height=450)
my_canvas.pack(fill="both", expand=True)

img= Image.open(r"C:\Users\HP\Desktop\cartoon\b1.jpeg")
img = img.resize((500, 460), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(img)

#Set image in canvas
my_canvas.create_image(0,0,anchor="nw",image=bg)

pic=Button(window,text="Cartoonify Image",command = image, padx=10,pady=5)
pic.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
pic.pack(side=TOP,pady=50)
pic.place(x=45, y=120)

vid=Button(window,text="Cartoonify Video",command = video, padx=10,pady=5)
vid.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
vid.pack(side=TOP,pady=50)
vid.place(x=45, y=160)

vid=Button(window,text="Sketchify Image  ",command = skimage, padx=10,pady=5)
vid.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
vid.pack(side=TOP,pady=50)
vid.place(x=45, y=200)

vid=Button(window,text="Sketchify Video  ",command = skvideo, padx=10,pady=5)
vid.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
vid.pack(side=TOP,pady=50)
vid.place(x=45, y=240)
