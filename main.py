from ctypes import alignment
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from ttkthemes import ThemedTk
import matplotlib.pyplot as plt 
import cv2
import util

# create instance for window
root=ThemedTk(theme="radiance")
# set window geometry
root.geometry("300x300")
# set window title
root.title("Image Encryption")
# make window unresizable
root.resizable(0, 0)
def encrypt():
    if key_entry.get() != '':
        # open image files 
        file1 = filedialog.askopenfile(mode="r", filetype=[("PNG file","*.png"),
                                                            ("JPG file", "*.jpg"),
                                                           ("All files", "*.*")])
        if file1 is not None:

            filename = file1.name
            img = cv2.imread(filename, 0)

            # get key value
            key = key_entry.get()

            confused_img = util.confusion(img,key)
            diffused_img = util.diffusion(confused_img,key)

            encrypted_image_name = filename.split('.')[0] + '_encrypted_' + key + '.' + filename.split('.')[1]
            cv2.imwrite(encrypted_image_name, diffused_img)

    else:
        # create messagebox
        messagebox.showinfo("Image Encrypter", "Please enter key value")

def decrypt():
    if key_entry.get() != '':
        # open image files 
        file1 = filedialog.askopenfile(mode="r", filetype=[("PNG file","*.png"),
                                                            ("JPG file", "*.jpg"),
                                                           ("All files", "*.*")])
        if file1 is not None:

            filename = file1.name
            img = cv2.imread(filename, 0)

            # get key value
            key = key_entry.get()
            
            decrypted_img = util.decrypt(img,key)

            decrypted_image_name = filename.split('.')[0] + '_decrypted_' + key + '.' + filename.split('.')[1]
            cv2.imwrite(decrypted_image_name, decrypted_img)

    else:
        # create messagebox
        messagebox.showinfo("Image Encrypter", "Please enter key value")

def getHistogram():
    file1 = filedialog.askopenfile(mode="r", filetype=[("PNG file","*.png"),
                                                            ("JPG file", "*.jpg"),
                                                           ("All files", "*.*")])
    if file1 is not None:

        filename = file1.name
        img = cv2.imread(filename, 0)

        plt.hist(img.ravel(), 256, [0, 256])
        plt.show()

# label to display text
key_label = Label(root, text="Enter key:", font=("haveltica 15 bold"))
key_label.place(x=45, y=40)
# entry to get the key value from user
key_entry = Entry(root, width=15)
key_entry.place(x=155, y=46)
# button for encryption of an image
btn = ttk.Button(root, text="Encrypt", command=encrypt)
btn2 = ttk.Button(root, text="Decrypt", command=decrypt)
btn3 = ttk.Button(root, text="Histogram", command=getHistogram)
btn.place(x=75, y=90)
btn2.place(x=75, y=130)
btn3.place(x=75, y=170)
l = Label(root, text = "Final year project made by \nJatin Singh Chug and Shuvrashish Roy",wraplength=260,justify=CENTER)
l.place(x=20,y=230)
root.mainloop()