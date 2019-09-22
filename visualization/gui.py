from tkinter import *
from PIL import ImageTk,Image
def main():
    root = Tk()
    canvas = Canvas(root, width=600, height=600)
    canvas.pack()
    button = Button(canvas, text='Generate QR Code', fg='black')
    button.pack(side=BOTTOM)
    img = ImageTk.PhotoImage(Image.open("test.png"))
    canvas.create_image(0,0,anchor=NW, image=img)
    mainloop()

if __name__ == '__main__':
    main()