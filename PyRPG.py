import random

monlist1 = []
monlist2 = []
monlist3 = []
monlist4 = []
monlist5 = []

itemlist = []

magiclist = []

class Monster:

    def __init__(self, name, hp, atk, dif):
        if(0<dif<=5):
            self.name = name
            self.hp = hp
            self.atk = atk
            if(dif<=1):
                monlist1.append(self)
            elif(dif<=2):
                monlist2.append(self)
            elif(dif<=3):
                monlist3.append(self)
            elif(dif<=4):
                monlist4.append(self)
            else:
                monlist5.append(self)
        else:
            print('ERRO: Dificuldade de monstro inválida (', name,')')

# inicio da lista de monstros

lobo = Monster('Lobo',100,20,1)
loboF = Monster('Lobo Faminto',130,23,2)
loboA = Monster('Lobo Alpha',150,26,3)
loboH = Monster('Lobisomem',160,28,4)
loboM = Monster('Lobo Mau',300,30,5)

# fim da lista de monstros

class Player:
    def __init__(self,sex,name):
        self.sex = sex
        self.name = name
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
    else:
        print('ERRO: Dificuldade de batalha inválida ( nível',level,')')

    print('\nUm',mon.name,'aparece!')

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
            else:
                print('Escolha inválida (',plyrinpt,')')
        if(enemyHP > 0 and player.hp > 0 and run==False):
            player.hp -= mon.atk
            print(player.name,'sofreu',mon.atk,'de dano de',mon.name)
        if(enemyHP<=0):
            player.atk += 1
            print('\nVitória!',player.name,'se sente mais forte\n')
        if(player.hp<=0):
            player.deathCount += 1
            player.hp=400
            run=True
            print('\nDerrota...')
            print(player.name,'acordou horas depois no local da batalha\n')

battle(1)
battle(2)
battle(3)
battle(4)
battle(5)