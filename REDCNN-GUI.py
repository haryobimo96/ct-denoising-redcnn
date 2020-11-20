# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:24:52 2020

@author: User
"""

import tkinter as tk
import pydicom as dicom
import pickle
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

canvas2 = tk.Canvas(master=frame2,
                    width=512,
                    height=512)
canvas2.pack()

frame3 = tk.Frame(master=window,
                  width=1024,
                  height=100)
frame3.pack(fill=tk.Y, side=tk.BOTTOM)

dicomarray = np.zeros((512,512))

class Module():
        
    def open_file(self):
        file_path = askopenfilename(
            filetypes = [("DICOM Files","*.dcm"),("All Files","*.*")]
            )
        global imga
        ds = dicom.read_file(file_path)
        img = ds.pixel_array
        imga = ((img-np.min(img))/(np.max(img)-np.min(img)))*255
        canvas1.image_tk = ImageTk.PhotoImage(image=Image.fromarray(imga))
        canvas1.itemconfigure(canvas1.create_image(256,256), 
                              image=canvas1.image_tk)
        
    def process(self):
        canvas2.image_tk = ImageTk.PhotoImage(image=Image.fromarray(imga))
        canvas2.itemconfigure(canvas2.create_image(256,256),
                              image=canvas2.image_tk)

M = Module()

btn_open = tk.Button(master=frame3,
                     text="Open DICOM File",
                     command=M.open_file)
btn_open.place(x=25,y=50)

btn_process = tk.Button(master=frame3,
                        text="Process",
                        command=M.process)
btn_process.place(x=150,y=50)


window.mainloop()