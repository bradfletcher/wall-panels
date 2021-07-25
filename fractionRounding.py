import math

def showFraction( numberToRound ):  
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
    elif fraction > .99 :  
        return str (numberToRound )    
    else :  
        fractionStr = "15/16" 
    return wholePartStr + " " + fractionStr + "\""     
