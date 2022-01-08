# Digital-accurate-clock-using-python
A beautiful half window clock using python

```
import time
from tkinter import *

root = Tk()
root.title("Digital Clock : ---Aryan Raj")
root.resizable()
lbl = Label(root)
lbl.grid(row=0, column=0)


def display():
    time_get = time.strftime("%Y/%m/%d\n%I:%M:%S %p")
    lbl.config(text=time_get, bg='black', fg='blue',
               font=('Butterbelly', 100, 'bold'))
    lbl.after(200, display)


display()
root.mainloop()

```
# By editing source code one can change colour theme of clock

# OUTPUT-
![clock](https://user-images.githubusercontent.com/75358720/148643831-5ad35b41-169e-4aba-a035-6f22b304b294.jpg)

**To use clock**
```
$git clone https://github.com/aryanraj2713/ID-card-generator-using-python.git
```
