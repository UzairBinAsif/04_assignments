import tkinter as tk
from typing import Union, List, Tuple

class Canvas:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack()
        
        # Store the last click coordinates
        self.last_click_x = 0
        self.last_click_y = 0
        
        # Store current mouse coordinates
        self.mouse_x = 0
        self.mouse_y = 0
        
        # Bind mouse events
        self.canvas.bind('<Button-1>', self._on_click)
        self.canvas.bind('<Motion>', self._on_mouse_move)
        
        # Dictionary to store object colors
        self.object_colors = {}
        
    def _on_click(self, event):
        self.last_click_x = event.x
        self.last_click_y = event.y
        
    def _on_mouse_move(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y
        
    def get_mouse_x(self) -> int:
        return self.mouse_x
        
    def get_mouse_y(self) -> int:
        return self.mouse_y
    
    def get_last_click(self) -> Tuple[int, int]:
        return self.last_click_x, self.last_click_y
    
    def create_rectangle(self, x1: int, y1: int, x2: int, y2: int, color: str) -> int:
        rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')
        self.object_colors[rect_id] = color
        return rect_id
    
    def set_color(self, object_id: int, color: str):
        self.canvas.itemconfig(object_id, fill=color)
        self.object_colors[object_id] = color
        
    def moveto(self, object_id: int, x: int, y: int):
        # Get current coordinates
        coords = self.canvas.coords(object_id)
        if not coords:
            return
            
        # Calculate width and height
        width = coords[2] - coords[0]
        height = coords[3] - coords[1]
        
        # Set new coordinates
        self.canvas.coords(object_id, x, y, x + width, y + height)
        
    def find_overlapping(self, x1: int, y1: int, x2: int, y2: int) -> List[int]:
        return self.canvas.find_overlapping(x1, y1, x2, y2)
        
    def wait_for_click(self):
        self.root.update()
        while self.last_click_x == 0 and self.last_click_y == 0:
            self.root.update()
            
    def update(self):
        self.root.update() 