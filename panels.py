#use python3  
import math
import json
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from fractionRounding import *  

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

#try reading from the json config file  
# with open("long_wall.json") as json_data_file:
#     data = json.load(json_data_file)

#try reading from the json config file  
with open("wall110.json") as json_data_file:
    data = json.load(json_data_file)

wall1 = data["wall"]
wall_len = wall1["width"]  
num_panels = wall1["panels"]  
baseboard_top = wall1["baseboard"]  
panel_gap = wall1["panel_gap"]  
chair_rail_bottom = wall1["chair_rail_bottom"]  

panel_width = ( wall_len - (panel_gap * (num_panels + 1))) / num_panels  
panel_height = (chair_rail_bottom - baseboard_top) - (2 * panel_gap )  

measurements = []  
panels = []  

mark = 0  
for i in range (num_panels * 2 + 2 ):
    measurements.append(mark)  
    
    if i % 2 == 0:  
        mark = mark + panel_gap  
        if i < num_panels * 2 :  
            p1 = Panel(mark, baseboard_top + panel_gap , panel_width, panel_height )  
            panels.append(p1)
    else:  
        mark = mark + panel_width   

print("Wall length: " + str(showFraction(wall_len) ) )  
print("Panels: " + str(num_panels) )  
print("Panel width: " + str(showFraction(panel_width) ))
print("Panel height: " + str(showFraction (panel_height) ) )

for pnl in panels:
    print( str( showFraction(pnl.x) ) + ' - ' + str( showFraction( pnl.x + panel_width ) ) )

# use matplotlib to visual the wall layout  
plt.figure()
currentAxis = plt.gca()
plt.xlim(0, wall_len)
# wall height is 96 in  
plt.ylim(0, 96 )
#draw the chair rail  
currentAxis.add_patch(Rectangle((0 , chair_rail_bottom ), wall_len, 3, fill=None, alpha=1))
#draw the baseboard  
currentAxis.add_patch(Rectangle((0 , 0 ), wall_len, baseboard_top , fill=None, alpha=1))
#draw the outlet  
currentAxis.add_patch(Rectangle((76 , 12 ), 3.5, 5 , fill=None, alpha=1))
#draw the outlet    
# currentAxis.add_patch(Rectangle((159 , 12), 3.5, 5 , fill=None, alpha=1))
#draw the panels  
for pnl in panels:  
    # outer edge  
    currentAxis.add_patch(Rectangle((pnl.x, baseboard_top + panel_gap ) , panel_width , panel_height , fill=None, alpha=1))  
    # inner edge  
    currentAxis.add_patch(Rectangle((pnl.x + 1.25, baseboard_top + panel_gap + 1.25 ) , panel_width - 2.5 , panel_height - 2.5 , fill=None, alpha=1))
#plt.show()  

# make a pdf of the plot instead of showing it.  
plt.savefig("wall.pdf")