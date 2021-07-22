import math

import matplotlib.pyplot as plt
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

#far wall  
# wall_len = 175.0
# num_panels = 5            
# panel_gap = 4     
# chair_rail_bottom = 33.75
# baseboard_top = 3.0  

#
wall_len = 110.0    
num_panels = 3             
panel_gap = 4.0   
chair_rail_bottom = 33.75
baseboard_top = 3.0  

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

print("Wall length: " + str(wall_len ) )  
print("Panels: " + str(num_panels) )  
print("Panel width: " + str(panel_width ))
print("Panel height: " + str(panel_height) )

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
currentAxis.add_patch(Rectangle((29 , 12 ), 3.5, 5 , fill=None, alpha=1))
#draw the outlet    
currentAxis.add_patch(Rectangle((159 , 12), 3.5, 5 , fill=None, alpha=1))
#draw the panels  
for pnl in panels:  
    currentAxis.add_patch(Rectangle((pnl.x, baseboard_top + panel_gap ) , panel_width , panel_height , fill=None, alpha=1))
    currentAxis.add_patch(Rectangle((pnl.x + 1.25, baseboard_top + panel_gap + 1.25 ) , panel_width - 2.5 , panel_height - 2.5 , fill=None, alpha=1))
plt.show()  

def printFractions( numberToRound ):  
    wholePart = math.floor( numberToRound )  
    fraction = numberToRound - wholePart  
    wholePartStr = str(wholePart) 
    if fraction < 1.0 / 16.0 :
        fractionStr =  ""  
    elif fraction < 2.0 / 16.0 :  
        fractionStr = "1/16"  
    elif fraction < 3.0 / 16.0 :  
        fractionStr = "1/8"  
    elif fraction < 4.0 / 16.0 :  
        fractionStr = "3/16"  
    elif fraction < 5.0 / 16.0 :  
        fractionStr = "1/4"  
    elif fraction < 6.0 / 16.0 :  
        fractionStr = "5/16"
    elif fraction < 7.0 / 16.0 :  
        fractionStr = "3/8"  
    elif fraction < 8.0 / 16.0 :  
        fractionStr = "7/16"
    elif fraction < 9.0 / 16.0 :  
        fractionStr = "1/2"  
    elif fraction < 10.0 / 16.0 :  
        fractionStr = "9/16"  
    elif fraction < 11.0 / 16.0 :   
        fractionStr = "5/8"  
    elif fraction < 12.0 / 16.0 :  
        fractionStr = "11/16"  
    elif fraction < 13.0 / 16.0 :  
        fractionStr = "3/4"  
    elif fraction < 14.0 / 16.0 :    
        fractionStr = "13/16"  
    elif fraction < 15.0 / 16.0 :    
        fractionStr = "7/8"  
    else :  
        fractionStr = "15/16" 
    return wholePartStr + " " + fractionStr + "\""       

num1 = 1.34 
num2 = 0.54 
num3 = 5.67  

print( printFractions (num3 ) )  