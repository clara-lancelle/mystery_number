from random import randint
class Play:

    nb_myst: int = randint(0,100)
    nb_try: int = 1
    limit_sup: int = 100
    limit_inf: int = 0
    message: str = ""
    win: bool = False

    def __init__(self):
        print('Un nombre mystère entre ' + str(self.limit_inf)+ ' et ' + str(self.limit_sup) + ' a été généré, lequel ?')

    def label(self):
        print('Le nombre mystère se trouve donc entre ' + str(self.limit_inf)+ ' et ' + str(self.limit_sup) + '.')

    def play_round(self, nb_player: int):
        if nb_player in range(self.limit_inf, self.limit_sup + 1):
            if nb_player == self.nb_myst :
                self.message = "Gagné ! En "+ str(self.nb_try) + " essais."
                self.win = True
            else :
                if nb_player > self.nb_myst :
                    self.message = "Trop grand !"
                    self.limit_sup = nb_player
                else :
                    self.message = "Trop petit !"
                    self.limit_inf = nb_player

                self.nb_try += 1
            print(self.message)
        else :
            print("Votre proposition est incorrecte !")
