# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
import pydicom as dicom
import numpy as np
import tensorflow as tf
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename


window = tk.Tk() 

    
frame0 = tk.Frame(master=window,
                  width=1024,
                  height=25)
frame0.pack(fill=tk.Y, side=tk.TOP)

label1 = tk.Label(master=frame0,
                  text="RED-CNN Denoiser")
label1.place(x=0,y=5)

main_frame = tk.Frame(master=window,
                      width=1024,
                      height=512)
main_frame.pack(fill=tk.Y, side=tk.TOP)

frame1 = tk.Frame(master=main_frame,
                  width=512,
                  height=512,
                  bg="gray",
                  relief=tk.RIDGE,
                  borderwidth=3)
frame1.pack(fill=tk.X, side=tk.LEFT)

canvas1 = tk.Canvas(master=frame1,
                    width=512,
                    height=512)
canvas1.pack()

frame2 = tk.Frame(master=main_frame,
                  width=512,
                  height=512,
                  bg="gray",
                  relief=tk.RIDGE,
                  borderwidth=3)
frame2.pack(fill=tk.X, side=tk.RIGHT)

frame3 = tk.Frame(master=window,
                  width=1024,
                  height=100)
frame3.pack(fill=tk.Y, side=tk.BOTTOM)

image_id = canvas1.create_image(256,256)

def open_file():
    file_path = askopenfilename(
        filetypes = [("DICOM Files","*.dcm"),("All Files","*.*")]
        )
    
    if file_path:
        ds = dicom.read_file(file_path)
        img = ds.pixel_array
        imga = ((img-np.min(img))/(np.max(img)-np.min(img)))*255
        canvas1.image_tk = ImageTk.PhotoImage(image=Image.fromarray(imga))
        canvas1.itemconfigure(image_id, image=canvas1.image_tk)

btn_open = tk.Button(master=frame3,
                     text="Open",
                     command=open_file)
btn_open.place(x=25,y=50)

window.mainloop()

