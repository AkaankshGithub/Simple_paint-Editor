from tkinter import*
from tkinter.ttk import Scale
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import END
import PIL.ImageGrab as imagegrab

class paint:
  def __init__(self) -> None:
    self.root=Tk()
    self.root.geometry('700x600')
    self.root.title("Paint")
    self.root.resizable(0,0)
    self.colorfram=LabelFrame(self.root,text='color',width=700,height=600,border=5,relief=SUNKEN)
    self.colorfram.place(x=170,y=0)

    self.by=Button(self.root,text=' ',width=4,height=2,relief=SUNKEN,border=4,command=self.hj)
    self.by.place(x=80,y=20)

    self.goo='black'       
    colors=["#00ffff","#F08080","#DFFF00","#DE3163","#6495ED",'#FF0000','#00FF00','#800080','#800000','#FFFFFF','#000000','#00FF00','#FF00FF','#008080','#00FFFF','#008000']
    i=j=0
    for color in colors:
           color=Button(self.colorfram,bg=color,width=3,bd=2,relief=RIDGE,command=lambda coll=color:self.colorr(coll))
           color.grid(row=i,column=j)
           j+=1
           if j==8:
              i=1
              j=0

    self.pensize=LabelFrame(self.root,text='Size',width=150,height=200)
    self.pensize.place(x=4,y=0)
    self.size=Scale(self.pensize,from_=50 ,to=1,orient=VERTICAL)
    self.size.grid(row=0,column=0)
    self.canv=Canvas(self.root,relief=GROOVE,border=4,width=650,height=400,bg='white')
    self.canv.place(x=30,y=125)
    self.canv.bind('<B1-Motion>',self.paint)
    Button(self.root,text='Save',command=self.savefile).place(x=570,y=30)
    self.root.mainloop()

  def paint(self,event):
      x1,y1=(event.x),(event.y)  
      x2,y2=(event.x),(event.y)  

      self.canv.create_oval(x1,y1,x2,y2,fill=self.goo,outline=self.goo,width=self.size.get())

  def colorr(self,coll):
      self.goo=coll

  def hj(self):
      self.goo='white'
  
  def savefile(self):

    filenam=filedialog.asksaveasfilename(defaultextension='.jpg')
    x=self.root.winfo_rootx()+self.canv.winfo_x()
    y=self.root.winfo_rooty()+self.canv.winfo_y()
    x1=self.canv.winfo_width()
    y1=self.canv.winfo_height()
    imagegrab.grab().crop((x,y,x1,y1)).save(filenam)

    
    

paint()