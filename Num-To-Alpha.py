import tkinter as tk
import inflect
#inflect used for convert number to word

frame = tk.Tk()
frame.title("Title.exe")
frame.geometry('400x200')
frame.configure(bg='gold')
frame1 = tk.Label(frame, text="NUMBERS ONLY !!!",background="gold")
frame1.pack()

def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        n2w = inflect.engine()
        xx = n2w.number_to_words(inp)
        lbl.config(text = "Provided Input: "+xx)
        inputtxt.delete("1.0","end")

# TextBox Creation
inputtxt = tk.Text(frame,height = 2,width = 25, foreground="black")
inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,text = "run",command = printInput)
printButton.pack()

# Label Creation  
lbl = tk.Label(frame, text = "",background="gold")
lbl.pack()
frame.mainloop()
