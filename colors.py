from random import randint

colors = [
    (255,0,0),      #RED
    (0,255,0),      #GREEN
    (0,0,255),      #BLUE
    (150,0,150),    #PINK
    (150,150,0),    #YELLOW
    (50,50,255),    #DAKRBLUE
    (0,100,0)       #DAKRGREEN
]

ColoredPieces = {}

def SetUp(pieces):
    global ColoredPieces
    
    localColors = colors
    pieces.remove(pieces[0])

    for piece in pieces:
        choice = randint(0,len(localColors) - 1)
        ColoredPieces[piece] = localColors[choice]
        del localColors[choice]

def GetColor(piece):
    return ColoredPieces[piece]