from CTkRangeSlider import *
import customtkinter

def show_value(value):
    print(value)
    
root = customtkinter.CTk()

range_slider = CTkRangeSlider(root, command=show_value)
range_slider.pack(padx=30, pady=30, fill="both")

root.mainloop()
