#   Version Play in Python2
#from Play import Play 
#   Version Play_typed in Python3
from Play_typed import Play

p = Play()
while p.win != True:
    nb_player = int(input())
    if nb_player:
        p.play_round(nb_player)
        if(p.win == True):
            break
        p.label()
    