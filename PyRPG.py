import random

monlist1 = []
monlist2 = []
monlist3 = []
monlist4 = []
monlist5 = []

itemlist = []

magiclist = []

class Monster:

    def __init__(self, name, hp, atk, diff):
        if(0<diff<=5):
            self.name = name
            self.hp = hp
            self.atk = atk
            if(diff<=1):
                monlist1.append(self)
            elif(diff<=2):
                monlist2.append(self)
            elif(diff<=3):
                monlist3.append(self)
            elif(diff<=4):
                monlist4.append(self)
            else:
                monlist5.append(self)
        else:
            print('ERRO: Dificuldade de monstro inválida', name)

# inicio da lista de monstros

lobo = Monster('Lobo',100,20,1)
loboF = Monster('Lobo Faminto',130,23,2)
loboA = Monster('Lobo Alpha',150,26,3)
loboH = Monster('Lobisomem',160,28,4)
loboM = Monster('Lobo Mau',180,30,5)

# fim da lista de monstros

class Player:
    def __init__(self,gen,name):
        self.gen = gen
        self.name = name
        self.hp = 400
        self.atk = 30
        self.mp = 200
        self.money = 20

charCreatTest=False
while(charCreatTest == False):
    sex = input('Qual o sexo de seu personagem? Digite m para masculino ou f para feminino: ')
    if (sex == 'm' or sex == 'f'):
        player = Player(sex,input('Escolha o nome de seu personagem: '))
        charCreatTest=True
    else:
        print('Sexo do personagem inválido', sex)
        charCreatTest=False

def battle(level):

    if(level==1):
        mon = monlist1[random.randint(0, len(monlist1) - 1)]
    elif(level==2):
        mon = monlist2[random.randint(0, len(monlist2) - 1)]
    elif(level==3):
        mon = monlist3[random.randint(0, len(monlist3) - 1)]
    elif(level==4):
        mon = monlist4[random.randint(0, len(monlist4) - 1)]
    elif(level==5):
        mon = monlist5[random.randint(0, len(monlist5) - 1)]
    else:
        print('ERRO: Dificuldade de batalha inválida')

    print('Um',mon.name,'aparece!')

    while(mon.hp > 0 or run == False):
        run=False
        print('Digite A para atacar\nDigite M para usar magia\nDigite I para abrir o inventário\nDigite F para fugir')
