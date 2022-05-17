from tkinter import *
from tkinter import ttk, filedialog, messagebox
from ttkthemes import ThemedTk 
import cv2
import util

# create instance for window
root=ThemedTk(theme="radiance")
# set window geometry
root.geometry("300x160")
# set window title
root.title("Encrypt Image")
# make window unresizable
root.resizable(0, 0)
def encrypt():
    if key_entry.get() != '':
        # open image files 
        file1 = filedialog.askopenfile(mode="r", filetype=[("JPG file", "*.jpg"),
                                                           ("All files", "*.*")])
        if file1 is not None:
            # return image file name
            filename = file1.name
            # get key value
            key = key_entry.get()
            # read image data
            f = open(filename, "rb")
            image = cv2.imread(filename, 0)
            image = f.read()
            # close image file
            f.close()
            # convert image data into bytearray
            image = bytearray(image)
            for index, values in enumerate(image):
                # perform XOR operation on
                # image data with key values
                image[index] = values^int(key)
            # write image data 
            f1 = open(filename,"wb")
            f1.write(image)
            f1.close()
    else:
        # create messagebox
        messagebox.showinfo("Image Encrypter", "Please enter key value")
# label to display text
key_label = Label(root, text="Enter key:", font=("haveltica 15 bold"))
key_label.place(x=45, y=40)
# entry to get the key value from user
key_entry = Entry(root, width=15)
key_entry.place(x=155, y=46)
# button for encryption of an image
btn = ttk.Button(root, text="Encrypt/Decrypt", command=encrypt)
btn.place(x=75, y=90)
root.mainloop()