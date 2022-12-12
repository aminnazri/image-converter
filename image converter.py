import tkinter as tk 
from tkinter import filedialog,StringVar,OptionMenu,messagebox,Checkbutton
import glob,os
import windnd,tkinter
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo

#================================================================
file_Name = ""
file_Dir = ""
tmp_name =""
extension = ""

r=255
g=255
b=255

root = tk.Tk()
root['bg'] = "white"
root.title('image converter')
# root.iconbitmap('C:/Users/User/Documents/education/py/yt_project/image_file_converter/man_ico.ico')
root.geometry('500x350')
root.resizable(width = False, height = False) 
#================================================================

option = ["png","jpeg","ico","pdf","jpg","svg"]
def convert_to():
    global img_export
    img_export = StringVar(root) 
    img_export.set(option[0])
    question_menu = OptionMenu(root, img_export , *option)
    question_menu.pack()

def transparent_colour():
    global tmp_name
    tmp_name = str(entry_field.get())
    return tmp_name  

def dragged_files(files):
    clear_history()
    global file_Dir
    file_Dir = '\n'.join((item.decode('gbk') for item in files))
    global file_Name
    file_Name = os.path.basename(file_Dir)  

    # saperate files and extension
    (files, ext) = os.path.splitext(file_Name)
    global extension
    extension = ext.replace('.', '')
    print(extension)

    img = Image.open(file_Dir) 
    img = img.resize((100, 100), Image.ANTIALIAS) 
    img = ImageTk.PhotoImage(img) 
    panel = tk.Label(root, image = img) 
    panel.image = img

    # place image in frame
    label1 = tk.Label(frame, image=img)
    label1.pack()

    # show file name
    label2 = tk.Label(frame, text=file_Name,fg="black")    
    label2.pack()

    # get the inserted color code
    exp = str(img_export.get())
    if extension == ("png") and exp == ("png"):
        transparent_colour() 

# remove everything in frame
def clear_history():    
    for widget in frame.winfo_children():
        widget.destroy() 

def convert_to_trasparent(exp):
    
    img = Image.open(file_Dir) 
    rgba = img.convert("RGBA") 
    datas = rgba.getdata() 
    
    # convert to the list
    list = transparent_colour()
    list1 = list.split (",") # seperate by comma

    # convert each element as integers
    li = []
    for i in list1:
        li.append(int(i))

    global r,g,b
    r = (li[0])
    g = (li[1])
    b = (li[2])
    print(r,g,b)
    newData = [] 
    for item in datas: 
        if item[0] == r and item[1] == g and item[2] == b:  # finding white colour by its RGB value 

            # storing a transparent value when we find a black colour 
            newData.append((255, 255, 255, 0)) 
        else: 
            newData.append(item)  # other colours remain unchanged 
    
    rgba.putdata(newData) 
    name = os.path.splitext(file_Dir)[0] # remove the current file extension
    
    if os.path.isfile(file_Name):
        i+=1
        name = name+i+".png"   # save as new name
    else:
        rgba.save(name, "PNG")
    print(name)
    

def convert_to_user_preference(exp):
    im = Image.open(file_Dir)   # open file
    rgb_im = im.convert('RGB')
    rgb_im.save(file_Dir.replace(extension,exp),quality = 95) # convert current  file according to the selected operation    




def convert_now():
    # using try, exccept, else is to display message box
    # try = all the operation stored there

    try:

        global exp
        exp = str(img_export.get())
        # remove background color condition
        if extension == ("png") and exp == ("png"):
            convert_to_trasparent(exp)
        else:
            convert_to_user_preference(exp)

    except:
        # error occur
        result="failed"
        messagebox.showinfo(result)

    else:
        result = "sucess"
        messagebox.showinfo("result",result)
    print(file_Dir)

tk.Label(text="",bg="white").pack()
a = tk.Label(text=" convert to png and select png image to remove plane bg color",bg="white",fg="grey", font=('Helvectia',12))
a.pack()

b = tk.Label(text="fill the blank with the background color code ",bg="white",fg="grey", font=('Helvectia',11))
b.pack()

tk.Label(text="convert to").pack()
convert_to()

entry_field = tk.Entry()
entry_field.pack() 

b = tk.Label(text="Drop your image here ",bg="white",fg="grey")
b.pack()

dragged_files
windnd.hook_dropfiles(root,func= dragged_files)

frame = tk.Frame(root, bg="#988c89") # create frame to insert selected picture
frame.place()
frame.pack()

convert = tk.Button(root, text="convert now", padx = 10, pady = 5, fg ="white",bg="#263D42",command=convert_now)
convert.pack()

root.mainloop()
print(r,g,b)
print(b)
print(g)

