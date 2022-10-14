from tkinter import *
import rotatescreen

root = Tk()
root.geometry('500x500')
root.resizable(False, False)
root.bg = ("blue")
root.title('ScreenRotate')
root.configure(bg = "#54c5d1")

#Adding background
photo = PhotoImage(file= "background_image.png")
myimage = Label(image = photo)
myimage.pack(padx=2, pady = 1)
#myimage.place(x = 20, y =20)

def Screen_rotation(enter):
    screen = rotatescreen.get_primary_display()

    if enter == "up":
        screen.set_landscape()
    elif enter == "right":
        screen.set_portrait_flipped()
    elif enter == "down":
        screen.set_landscape_flipped()
    elif enter == "left":
        screen.set_portrait()

    

#Creating buttons
Button(root, text = "Up", command = lambda: Screen_rotation("up"), bg = "#2f7bc2", font="curvy 18", width = 5).place(x = 210, y = 30)
Button(root, text = "Right", command = lambda: Screen_rotation("right"), bg = "#22974f", font="arial 18", width = 5).place(x = 405, y = 210)
Button(root, text = "Down", command = lambda: Screen_rotation("down"), bg = "#b9dd1a", font="monospace 18", width = 5).place(x = 210, y = 400)
Button(root, text = "Left", command = lambda: Screen_rotation("left"), bg = "#d8521d", font="arial 18", width = 5).place(x = 13, y = 210)


