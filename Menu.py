from tkinter import Tk, Canvas, Frame, BOTH, Label

def mainMenu():
  class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

      self.master.title("Welcome to UULUR, GUI!")
      self.pack(fill=BOTH, expand=1)

      canvas = Canvas(self)

    
      canvas.create_rectangle(0, 0, 250, 800,
          outline="#15277a", fill="#15277a")
      canvas.create_rectangle(250, 0, 800, 500,
          outline="#444c73", fill="#444c73")

    
      canvas.pack(fill=BOTH, expand=1)


  def main():
  
    root = Tk()
    ex = Example()
    root.geometry("500x200+300+300")
    Label(text="U.U.L.U.R", bg="#15277a",
         font=("Terminal", 20)).place(relx=0.1,rely=0.15)
    Label(text="The", bg="#15277a",
         font=("Terminal", 10)).place(relx=0.225,rely=0.35)
                                
    root.mainloop()
  
  
  
  main()
