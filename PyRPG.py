import random

monlist = []

class Monster:

    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
        monlist.append(self)

# inicio da lista de monstros

lobo = Monster('Lobo Mau',100,20)

# fim da lista de monstros

def battle(difficulty):

    if(difficulty==1):
        mon = monlist[random.randint(0, (len(monlist) - 1)//5)]
    elif(difficulty==2):
        mon = monlist[random.randint((len(monlist) - 1)//5, ((len(monlist) - 1)*2)//5)]
    elif(difficulty==3):
        mon = monlist[random.randint(((len(monlist) - 1)*2)//5, ((len(monlist) - 1)*3)//5)]
    elif(difficulty==4):
        mon = monlist[random.randint(((len(monlist) - 1)*3)//5, ((len(monlist) - 1)*4)//5)]
    elif(difficulty==5):
        mon = monlist[random.randint(((len(monlist) - 1)*4)//5, len(monlist) - 1)]
    else:
        print('ERRO: Dificuldade da batalha inválida')

    print('Um',mon.name,'aparece!')