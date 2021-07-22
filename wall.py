import os
import math

import matplotlib.pyplot as plt
import matplotlib.lines as lines
from matplotlib.patches import Rectangle

class Panel:  
    def __init__(self, x, y, width, length ):  
        self.x = x
        self.y = y
        self.width = width  
        self.length = length  

    def getWidth():  
        return self.width  

class Wall:
    def __init__(self, length, baseboard_top, chair_rail_bottom ):  
        self.length = length
        self.baseboard_top = baseboard_top
        self.chair_rail_bottom = chair_rail_bottom  

wall_len = 175.0
num_panels = 4  
panel_gap = 4.0  
chair_rail_bottom = 33.0
baseboard_top = 3.0  

panel_width = ( wall_len - (panel_gap * (num_panels + 1))) / num_panels  
panel_height = (chair_rail_bottom - baseboard_top) - (2 * panel_gap )  

# windows spec 
#cols = (os.get_terminal_size().columns ) 
#rows = (os.get_terminal_size().rows ) - 10  

# mac  
rows, cols = os.popen('stty size', 'r').read().split()
rows = int(rows ) - 10  
cols = int(cols )  

factor = float( cols ) / wall_len  
print(factor )  

measurements = []  
measurements_scaled = []  
panels = []  

mark = 0  
for i in range (num_panels * 2 + 2 ):
    measurements.append(mark)  
    measurements_scaled.append(math.floor(mark * factor ))
    
    if i % 2 == 0:  
        mark = mark + panel_gap  
        p1 = Panel(mark, 0, panel_width, panel_height )  
        panels.append(p1)
    else:  
        mark = mark + panel_width  

screen = ''  
for i in range(rows):  
    row = ''  
    for j in range(cols):  
        if i == 0 or i == rows - 1:  
            screen = screen + '-'  
        else:  
            if measurements_scaled.count(j) == 1:  
                screen = screen + '|'  
            else:  
                screen = screen + ' '  

print(screen)  

print("Panel width: " + str(panel_width ))
print("Left marks: " )  
info = ''  
for i in measurements:  
    info = info + str(i) + ', '  
print(info )  

for pnl in panels:
    print( str( pnl.x ) + ' - ' + str( pnl.x + panel_width ) )



# use matplotlib to visual the wall layout  
plt.figure()
currentAxis = plt.gca()
plt.xlim(0, wall_len)
plt.ylim(0, 96 )
#draw the chair rail  
currentAxis.add_patch(Rectangle((0 , chair_rail_bottom ), wall_len, 3, fill=None, alpha=1))
#draw the baseboard  
currentAxis.add_patch(Rectangle((0 , 0 ), wall_len, baseboard_top , fill=None, alpha=1))
#draw the outlet  
currentAxis.add_patch(Rectangle((29 , 12 ), 4, 5.5 , fill=None, alpha=1))
#draw the outlet    
currentAxis.add_patch(Rectangle((159 , 12), 4, 5.5 , fill=None, alpha=1))
#draw the panels  
for pnl in panels:  
    currentAxis.add_patch(Rectangle((pnl.x, baseboard_top + panel_gap ), 23, panel_height , fill=None, alpha=1))
plt.show()