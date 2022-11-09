import sys
import os
from tkinter import filedialog
from tkinter import *
from PIL import Image
import re

# pillow library used
# tkinter library used


def browse_button():
    # user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)


    
def conv():
    print("\n TIFF to JPG Conversion\n")
    print("\n Date: 22 April 2022 \n\n")

    directory = "JPEG"
    output = filename + "/" + directory
    if os.path.exists(output):
        pass
    else:
        os.mkdir(output)

    f1 = os.listdir(filename) 
    for fname in os.listdir(filename):
        if not fname.endswith(".tif"):
            continue
        test = os.path.splitext(fname)[0]
        value1 = filename + '/' + fname

        # open the tif image
        image = Image.open(value1)

        # define jpg file name as same tif image name
        name1 = output + '/' + test + ".jpg"
        print(name1)

        # get the tif image resolution value
        img_dpi = str(image.info['dpi'])
        patn = re.sub(r"[\(\)]", "", img_dpi)
        sp = patn.split(",")[0]
        dpi_val = round(float(sp))  

        # convert to jpeg image, resolution value assigned from tiff image
        image.save(name1, 'jpeg', dpi=(dpi_val,dpi_val), quality=90)
    messagebox.showinfo("TIFF to JPG", "Completed")
    
root = Tk()
root.geometry("400x350")
root.title("TIFF to JPEG Converter")
root.config(bg='#ffcc00') 

img = "logo.png"
logo = PhotoImage(file=img)
label1 = Label(root, image = logo) 
label1.pack(pady=20)

folder_path = StringVar()
lbl1 = Label(root, text='TIFF to JPEG Converter', font='helvetica 15', bg='#ffcc00')
lbl1.pack(pady=10)
button2 = Button(text="Browse", command=browse_button, bg='royalblue', fg = 'white').pack(pady=25)
button3 = Button(text="Submit", command=conv, bg='royalblue', fg = 'white').pack(pady=25)
lbl2 = Label(root, textvariable=folder_path, font='helvetica 12', bg='#ffcc00')
lbl2.pack(pady=10)

mainloop()

