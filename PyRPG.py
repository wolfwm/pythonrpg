import random

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
            self.hp = 410
            self.atk = 45
            self.mp = 150
        else:
            self.hp = 400
            self.atk = 40
            self.mp = 200
        self.money = 20
        self.runCount = 0
        self.deathCount = 0

charCreateTest=False
while(charCreateTest == False):
    sex = input('\nQual o sexo de seu personagem? Digite m para masculino ou f para feminino: ')
    if (sex == 'm' or sex == 'f'):
        player = Player(sex,input('\nEscolha o nome de seu personagem: '))
        confirmTest=False
        while(confirmTest==False):
            print('\nPersonagem:',player.name,'de sexo',sex)
            test=input('Confirmar personagem? s/n: ')
            if(test=='s'):
                confirmTest=True
                charCreateTest=True
            elif(test=='n'):
                confirmTest=True
            else:
                print('Opção inválida (',test,')')
    else:
        print('Sexo do personagem inválido (', sex,')')

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
    elif(level==6):
        mon = bosslist[random.randint(0, len(bosslist) - 1)]

        # dificuldade 6 é uma luta de chefe

    else:
        print('ERRO: Dificuldade de batalha inválida ( nível',level,')')

    run=False
    enemyHP = mon.hp
    while(enemyHP > 0 and player.hp > 0 and run == False):
        print('\n',mon.name,': ',enemyHP,'HP\n',player.name,': ',player.hp,'HP\n')
        choiceTest=False
        while(choiceTest==False):
            plyrinpt=input('Digite a para atacar\nDigite f para fugir\nDecisão: ')
            if(plyrinpt=='a'):
                enemyHP -= player.atk
                print(player.name,'infligiu',player.atk,'de dano em',mon.name)
                choiceTest=True
            elif(plyrinpt=='f'):
                choiceTest=True
                run=True
                player.runCount += 1
                print(player.name,'fugiu de', mon.name,'\n')
                return 3
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
            player.hp=400
            run=True
            print('\nDerrota...')
            return 2

storyIndex = 0
if(battle(1)==1):
    print('Estoria se vitória ( batalha 1 )')
    storyIndex=1
else:
    print('Estória se derrota ou fuga ( batalha 1 )')
    storyIndex=2

if(storyIndex==1):
    storyIndex=battle(2)
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
        storyIndex=int(input('Seleção: '))
        if(storyIndex==1):
            print('Consequência de X')
            test=True
            storyIndex=2
        elif(storyIndex==2):
            print('Consequência de Y')
            test=True
        elif(storyIndex==3):
            print('Consequência de Z')
            test=True

        else:
            print('Escolha inválida (',storyIndex,')')

if(storyIndex==1):
    print('Estoria pacifica')
elif(storyIndex==2):
    storyIndex = battle(6)
    if (storyIndex == 1):
        print('Estoria se vitória ( batalha 6 )')
        storyIndex = 1
    elif (storyIndex == 2):
        print('Estória se derrota ( batalha 6 )')
        storyIndex = 2
    else:
        print('Estória se fuga ( batalha 6 )')
        storyIndex = 3
else:
    print('Estoria com desavenças')