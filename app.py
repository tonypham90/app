import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import svgwrite

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x200')
        self.title('SVG Creator')

        self.shape_var = tk.StringVar()
        self.size_var = tk.StringVar()

        ttk.Label(self, text='Shape:').grid(column=0, row=0)
        ttk.Combobox(self, textvariable=self.shape_var, values=['square', 'circle', 'ellipse']).grid(column=1, row=0)

        ttk.Label(self, text='Size:').grid(column=0, row=1)
        ttk.Entry(self, textvariable=self.size_var).grid(column=1, row=1)

        ttk.Button(self, text='Create SVG', command=self.create_svg).grid(column=0, row=2, columnspan=2)

    def create_svg(self):
        shape = self.shape_var.get()
        size = int(self.size_var.get())
        
        dwg = svgwrite.Drawing('output.svg', profile='tiny')
        
        if shape == 'square':
            dwg.add(dwg.rect((10, 10), (size,size)))
        elif shape == 'circle':
            dwg.add(dwg.circle(center=(size/2,size/2), r=size/2))
        elif shape == 'ellipse':
            dwg.add(dwg.ellipse(center=(size/2,size/2), r=(size/2,size/4)))

        dwg.save()

app = Application()
app.mainloop()
