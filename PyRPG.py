import random

# import time

monlist1 = []
monlist2 = []
monlist3 = []
monlist4 = []
monlist5 = []

bosslist = []

itemlist = []

magiclist = []

class Monster:

    def __init__(self, name, hp, atk, dif):
        if(0<dif<=6):
            self.name = name
            self.hp = hp
            self.atk = atk
            if(dif==1):
                monlist1.append(self)
            elif(dif==2):
                monlist2.append(self)
            elif(dif==3):
                monlist3.append(self)
            elif(dif==4):
                monlist4.append(self)
            elif(dif==5):
                monlist5.append(self)
            else:
                bosslist.append(self)
        else:
            print('ERRO: Dificuldade de monstro inválida (', name,')')

# inicio da lista de monstros

lobo = Monster('Lobo',100,20,1)
loboF = Monster('Lobo Faminto',130,23,2)
loboA = Monster('Lobo Alpha',150,26,3)
loboH = Monster('Lobisomem',160,28,4)
loboM = Monster('Lobo Mau',180,30,5)

# fim da lista de monstros

# inicio da lista de chefes ( dif = 6 )

loboMP = Monster('Lobo Mau Picapau',200,33,6)

# fim da lista de chefes

class Player:
    def __init__(self,sex,name):
        self.sex = sex
        self.name = name
        if(sex=='m'):
            self.hpmax = 410
            self.mpmax = 150
            self.atk = 45
        else:
            self.hpmax = 400
            self.mpmax = 200
            self.atk = 40
        self.hp = self.hpmax
        self.mp = self.mpmax
        self.money = 20
        self.runCount = 0
        self.deathCount = 0

def battle(id, canRun):

        # cada id de 1 a 5 é uma dificuldade crescente

    if(id==1):
        mon = monlist1[random.randint(0, len(monlist1) - 1)]
    elif(id == 2):
        mon = monlist2[random.randint(0, len(monlist2) - 1)]
    elif(id == 3):
        mon = monlist3[random.randint(0, len(monlist3) - 1)]
    elif(id == 4):
        mon = monlist4[random.randint(0, len(monlist4) - 1)]
    elif(id == 5):
        mon = monlist5[random.randint(0, len(monlist5) - 1)]

    elif(id == 6):
        mon = bosslist[random.randint(0, len(bosslist) - 1)]

        # id 6 é uma luta de chefe aleatória

    elif(id in monlist1 or id in monlist2 or id in monlist3 or id in monlist4 or id in monlist5 or id in bosslist):
        mon = id
    else:
        print('ERRO: ID de inimigo inválido (', id, ')')

    run=False
    enemyHP = mon.hp
    while(enemyHP > 0 and player.hp > 0 and run == False):
        print('\n',mon.name,': ',enemyHP,'HP\n',player.name,': ',player.hp,'HP\n')
        choiceTest=False
        while(choiceTest==False):
            plyrinpt=input('Digite a para atacar\nDigite e para esperar\nDigite f para fugir\nDecisão: ')
            if(plyrinpt=='a'):
                enemyHP -= player.atk
                print(player.name,'infligiu',player.atk,'de dano a',mon.name)
                choiceTest=True
            elif(plyrinpt=='f'):
                if(canRun==True):
                    choiceTest = True
                    run=True
                    player.runCount += 1
                    print(player.name,'fugiu de', mon.name,'\n')
                    return 3
                else:
                    print(player.name,'não pode fugir!')
            elif(plyrinpt=='e'):
                choiceTest = True
                print(player.name,'esperou')
            else:
                print('Escolha inválida (',plyrinpt,')')
        if(enemyHP > 0 and player.hp > 0 and run==False):
            player.hp -= mon.atk
            print(player.name,'sofreu',mon.atk,'de dano de',mon.name)
        if(enemyHP<=0):
            player.atk += 1
            print('\nVitória!',player.name,'se sente mais forte\n')
            return 1
        if(player.hp<=0):
            player.deathCount += 1
            player.hp=player.hpmax
            player.mp=player.mpmax
            run=True
            print('\nDerrota...\n')
            return 2

turnOff=False
print('Descrição do jogo\n')
while(turnOff==False):
    plyrinpt=input('Digite 1 para começar o jogo\nDigite 0 para desligar o jogo\nDecisão: ')

    if(plyrinpt=='1'):

        charCreateTest = False
        while (charCreateTest == False):
            sex = input('\nQual o sexo de seu personagem? Digite m para masculino ou f para feminino: ')
            if (sex == 'm' or sex == 'f'):
                player = Player(sex, input('\nEscolha o nome de seu personagem: '))
                confirmTest = False
                while (confirmTest == False):
                    print('\nPersonagem:', player.name, 'de sexo', sex)
                    test = input('Confirmar personagem? s/n: ')
                    if (test == 's'):
                        confirmTest = True
                        charCreateTest = True
                    elif (test == 'n'):
                        confirmTest = True
                    else:
                        print('Opção inválida (', test, ')')
            else:
                print('Sexo do personagem inválido (', sex, ')')

        # começo do exemplo de possível estrutura de estoria

        storyIndex = 0
        if(battle(1,True)==1):
            print('Estoria se vitória ( batalha 1 )')
            storyIndex=1
        else:
            print('Estória se derrota ou fuga ( batalha 1 )')
            storyIndex=2

        if(storyIndex==1):
            storyIndex=battle(2,True)
            if(storyIndex==1):
                print('Estoria se vitória ( batalha 2 )')
                storyIndex=1
            elif(storyIndex==2):
                print('Estória se derrota ( batalha 2 )')
                storyIndex=2
            else:
                print('Estória se fuga ( batalha 2 )')
                storyIndex=3
        else:
            test=False
            while(test==False):
                print('Escolha entre as opções\nX ( 1 )\nY ( 2 )\nZ ( 3 )')
                choiceTest=input('Seleção: ')
                if(choiceTest=='1'):
                    print('Consequência de X')
                    test=True
                    battle(lobo,False)
                    storyIndex=2
                elif(choiceTest=='2'):
                    print('Consequência de Y')
                    test=True
                    storyIndex=2
                elif(choiceTest=='3'):
                    print('Consequência de Z')
                    test=True
                    storyIndex=3
                else:
                    print('Escolha inválida (',choiceTest,')')

        if(storyIndex==1):
            print('Estoria com atritos')
        elif(storyIndex==2):
            storyIndex = battle(loboMP,False)
            if (storyIndex == 1):
                print('Estoria se vitória ( batalha loboMP )')
                storyIndex = 1
            else:
                print('Estória se derrota ( batalha loboMP )')
                storyIndex = 2
        else:
            print('Estoria pacifica')

        # fim do exemplo

    elif(plyrinpt=='0'):
        print('Desligando o jogo')
        turnOff=True
    else:
        print('Seleção inválida (',plyrinpt,')')