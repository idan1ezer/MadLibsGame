from tkinter import *

root = Tk()
root.title("Mad Libs Generator")
root.geometry('650x350')
root.resizable(False, False)
values = [None] * 7
entries = []


#fields = "Crush's name: ", "Verb: ", "Favorite room: ", "Plural noun: ", "Body part: ", "Piece of furniture: ", "Adjective: "
frame1 = Frame(root)
frame2 = Frame(root)

def show_frame(frame):
    frame.tkraise()

#creating function for the buttom
def letsGo_click():
    for i,entry in enumerate(entries):
        values[i] = entry.get()
    textUpdate()
    show_frame(frame2)


for frame in (frame1,frame2):
    frame.grid(row=0,column=0,sticky='nsew')


################### First Frame ###################
#creating the labels, buttons and entries
LblIntroduction = Label(frame1, text = "Mad Libs Introduction:\n \n Mad Libs is a phrasal template word game created by Leonard Stern and Roger Price.\n It consists of one player prompting others for a list of words to substitute for blanks in a story before reading aloud.\n The game is frequently played as a party game or as a pastime.\n")
BtnBegin = Button(frame1, text = "Lets go!", padx = 20, pady = 5, fg = "blue", command = letsGo_click)
LblPleaseFill = Label(frame1, text = "Please enter values for each row")

LblcrushName = Label(frame1, text = "Crush's name: ")
EcrushName = Entry(frame1, width=20)
Lblverb = Label(frame1, text = "Verb: ")
Everb = Entry(frame1, width=20)
LblFavRoom = Label(frame1, text = "Favorite room: ")
EfavRoom = Entry(frame1, width=20)
LblPluralNoun = Label(frame1, text = "Plural noun: ")
EpluralNoun = Entry(frame1, width=20)
LblBodyPart = Label(frame1, text = "Body part: ")
EbodyPart = Entry(frame1, width=20)
LblPieceOfFurniture = Label(frame1, text = "Piece of furniture: ")
EpieceOfFurniture = Entry(frame1, width=20)
LblAdjective = Label(frame1, text = "Adjective: ")
Eadjective = Entry(frame1, width=20)


#adding entries to list
entries.extend([EcrushName, Everb, EfavRoom, EpluralNoun, EbodyPart, EpieceOfFurniture, Eadjective])


#positioning the labels, buttons and entries
LblIntroduction.grid(row = 0, column = 0, columnspan = 5)
LblPleaseFill.grid(row = 1, column = 0, columnspan = 4, pady = 10)
BtnBegin.grid(row = 9, column = 2, pady = 15)

LblcrushName.grid(row = 2, column = 1)
EcrushName.grid(row = 2, column = 2)
Lblverb.grid(row = 3, column = 1)
Everb.grid(row = 3, column = 2)
LblFavRoom.grid(row = 4, column = 1)
EfavRoom.grid(row = 4, column = 2)
LblPluralNoun.grid(row = 5, column = 1)
EpluralNoun.grid(row = 5, column = 2)
LblBodyPart.grid(row = 6, column = 1)
EbodyPart.grid(row = 6, column = 2)
LblPieceOfFurniture.grid(row = 7, column = 1)
EpieceOfFurniture.grid(row = 7, column = 2)
LblAdjective.grid(row = 8, column = 1)
Eadjective.grid(row = 8, column = 2)


################### Second Frame ###################
def textUpdate():
    LblText = Label(frame2, text = f"You were suddenly feeling frisky so you asked {values[0]} if he wanted to {values[1]} in the {values[2]} with you.\n Normally, you use this room to store your vast collection of {values[3]}, but this time you felt like switching things up.\n\n You just knew he was ready to go when he propped his {values[4]} up on the {values[5]} and gave you his {values[6]} bedroom eyes.")
    LblText.grid(row = 0, column = 0, columnspan = 5)
    BtnExit = Button(frame2, text = "Exit", command = root.quit)
    BtnExit.grid(row = 1, column = 1, columnspan = 5)



show_frame(frame1)
root.update()
root.mainloop()