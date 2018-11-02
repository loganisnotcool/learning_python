import tkinter
import time
import threading

global clicked
clicked = 0

def clickFunc():
    global clicked
    clicked += 1
    changeText()
    print(f'times clicked {str(clicked)}')

def changeText():
    if text.get() == 'Water World!':
        text.set('Water Water!!')
    elif text.get() == 'Water Water!!':
        text.set('Hello Water!')
    elif text.get() == 'Hello Water!':
        text.set('Water World!')
    print('Changing text now...')


def threadFunc():
    while True:
        time.sleep(2)
        changeText()    


root = tkinter.Tk()
root.title('Water GUI')
root.minsize(width=500, height=500)

text = tkinter.StringVar()
text.set('Water World!')

message = tkinter.Message(root,textvariable=text, font=('Times', 50), width=600)
message.grid(in_=root, column=0, row=0)

button = tkinter.Button(root, text='Press Me', command=lambda: clickFunc())
button.grid(in_=root, column=0, row=1)

threading.Thread(target=threadFunc).start()

root.mainloop()