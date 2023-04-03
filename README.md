# CTkRangeSlider
**A range slider widget made for [customtkinter](https://github.com/TomSchimansky/CustomTkinter)**

![Screenshot](https://user-images.githubusercontent.com/89206401/229349732-0e078b00-f2b7-46e7-9774-313090253769.jpg)

## Installation
### [<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Akascape/CTkRangeSlider?&color=white&label=Download%20Source%20Code&logo=Python&logoColor=yellow&style=for-the-badge"  width="400">](https://github.com/Akascape/CTkRangeSlider/archive/refs/heads/main.zip)

Download the source code, paste the `CTkRangeSlider` folder in the directory where your program is present.

## Example
```python
from CTkRangeSlider import *
import customtkinter

def show_value(value):
    print(value)
    
root = customtkinter.CTk()

range_slider = CTkRangeSlider(root, command=show_value)
range_slider.pack(padx=30, pady=30, fill="both")

root.mainloop()
```

## Arguments
| Parameters | Details |
|--------|----------|
|master	| root window, can be _tkinter.Frame_ or _CTkFrame_|
|command	| callback function, receives slider value as argument, two separate commands can be given by `command=(cmd1, cmd2)`|
|variables	| tuple: set two tkinter.IntVar or tkinter.DoubleVar objects |
|width	| slider width in px|
|height | slider height in px|
|corner_radius| corner roundness of the slider |
|border_width	| space around the slider rail in px |
|from_	| lower slider value |
|to	| upper slider value |
|number_of_steps |	number of steps in which the sliders can be positioned |
|fg_color	| foreground color, tuple: (light_color, dark_color) or single color |
|progress_color	| tuple: (light_color, dark_color) or single color or "transparent", color of the slider line before the button |
|border_color	| slider border color, tuple: (light_color, dark_color) or single color or "transparent", default is "transparent"|
|button_color |	color of the slider buttons, tuple: (light_color, dark_color) or single color or **((light_color_1, dark_color_1), (light_color_2, light_color_2)) for separate button colors** |
|button_hover_color |	hover color, tuple: (light_color, dark_color) or single color|
|button_width | width of the buttons in px |
|button_length | length of the buttons in px|
|button_corner_radius | corner roundness of the buttons |
|orientation | "horizontal" (standard) or "vertical" |
|state	| "normal" or "disabled" (not clickable) |
|hover | bool, enable/disable hover effect, default is True |

## Methods:
- **.configure(attribute=value, ...)**

    All attributes can be configured and updated.
    ```python
     range_slider.configure(fg_color=..., progress_color=..., button_color=..., ...)
    ```
- **.set([value, value])**

   Set sliders to specific float value.

- **.get()**

   Get current values of slider.
   
- **.cget("attribute_name")**

   Get any attribute value.
   
### More Details
This widget works just like the normal customtkinter slider widget, but it has dual slider-heads instead of one. A special thanks to [EN20M](https://github.com/EN20M) for providing the custom DrawEngine for rangeslider. 
Follow me for more stuff like this: [`Akascape`](https://github.com/Akascape/)
### That's all, hope it will help!
