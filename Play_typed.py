# import to generate random int
from random import randint
class Play:
    #mystery randomn int
    nb_myst: int = randint(0,100)
    #number of try
    nb_try: int = 1
    #upper limit
    limit_sup: int = 100
    #lower limit
    limit_inf: int = 0
    message: str = ''
    #status win or not yet
    win: bool = False

    #first message, display when the player not played yet
    def __init__(self):
        print('Un nombre mystère entre ' + str(self.limit_inf)+ ' et ' + str(self.limit_sup) + ' a été généré, lequel ?')

    # message with the new limit numbers to help the player
    def label(self):
        print('Le nombre mystère se trouve donc entre ' + str(self.limit_inf)+ ' et ' + str(self.limit_sup) + '.')

    # a round function, compare the player number to the mystery number
    # or display a message if the player number is over the limits
    def play_round(self, nb_player: int):
        if nb_player in range(self.limit_inf, self.limit_sup + 1):
            if nb_player == self.nb_myst :
                self.message = 'Gagné ! En '+ str(self.nb_try) + ' essais.'
                self.win = True
            else :
                if nb_player > self.nb_myst :
                    self.message = 'Trop grand !'
                    self.limit_sup = nb_player
                else :
                    self.message = 'Trop petit !'
                    self.limit_inf = nb_player

                self.nb_try += 1
            print(self.message)
        else :
            print('Votre proposition est incorrecte !')
