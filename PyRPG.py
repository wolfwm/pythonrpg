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

    def __init__(self, name, hp, atk, defe, weakness, dif):
        if(0<dif<=6):
            self.name = name
            self.hp = hp
            self.atk = atk
            self.defe = defe
            self.weakness = weakness
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

lobo = Monster('Lobo',100,20,0,'agua',1)
loboF = Monster('Lobo Faminto',130,23,0,'terra',2)
loboA = Monster('Lobo Alpha',150,26,0,'ar',3)
loboH = Monster('Lobisomem',160,28,0,'fogo',4)
loboM = Monster('Lobo Mau',180,30,0,'eter',5)

# fim da lista de monstros

# inicio da lista de chefes ( dif = 6 )

loboMP = Monster('Lobo Mau Picapau',200,33,0,'fogo',6)

# fim da lista de chefes

#lista de magias

fogo = 70
ar = 60
agua = 50
eter = 80
terra = 55

magiclist = []

#fim da lista de magias

#lista de itens

hp25 = 25
hp50 = 50
mp40 = 40
defesa = 0.20
itemlist = [hp25, hp25, hp50, mp40, defesa]

#fim da lista de magias

class Player:
    def __init__(self,sex,name):
        if(sex=='m' or sex=='f'):
            self.sex = sex
            self.name = name
            if name == 'cheatmode':
                self.sex='m'
                self.name='Wolf'
                self.hpmax=9999
                self.mpmax=9999
                self.atk=9999
                self.defe=9999
                self.money=9999
            else:
                if(sex=='m'):
                    self.hpmax = 380
                    self.mpmax = 150
                    self.atk = 45
                    self.defe = 15
                else:
                    self.hpmax = 410
                    self.mpmax = 200
                    self.atk = 40
                    self.defe = 10
                self.money = 20
            self.hp = self.hpmax
            self.mp = self.mpmax
            self.runCount = 0
            self.deathCount = 0
        else:
            print('ERRO: Sexo de personagem inválido (', sex,')')

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
    enemyAtk=mon.atk
    while(enemyHP > 0 and player.hp > 0 and run == False):
        print('\n',mon.name,': ',enemyHP,'HP\n',player.name,': ',player.hp,'HP,',player.mp,'MP\n')
        choiceTest=False
        while(choiceTest==False):
            defend = 0
            plyrinpt=input('Digite a para atacar\nDigite d para se defender\nDigite m para usar magia\nDigite i para usar item\nDigite f para fugir\nDecisão: ')
            if(plyrinpt=='a'):
                dmg = player.atk + random.randint(-5,3) - mon.defe
                enemyHP -= dmg
                print(player.name,'infligiu',dmg,'de dano a',mon.name)
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
            elif(plyrinpt=='d'):
                choiceTest = True
                defend = player.defe
                print(player.name,'está se defendendo')
            elif(plyrinpt=='m'):
                if (fogo in magiclist or terra in magiclist or agua in magiclist or ar in magiclist or eter in magiclist):
                    mgtest=False
                    while mgtest==False:
                        dmg=0
                        plyrinpt = str(input('Escolha fogo, ar, agua, eter, terra ou 0 para cancelar: '))
                        if plyrinpt == 'fogo':
                            if fogo in magiclist:
                                if mon.weakness == 'fogo':
                                    dmg=fogo*2
                                else:
                                    dmg=fogo
                                enemyHP -= dmg
                                print(player.name,'gastou 25 MP')
                                print (player.name, 'infligiu', dmg, 'de dano a', mon.name)
                                player.mp-=25
                                mgtest=True
                                choiceTest=True
                            else:
                                print(player.name,'não sabe essa magia ( fogo )')
                        elif plyrinpt == 'ar':
                            if ar in magiclist:
                                if mon.weakness == 'ar':
                                    dmg = ar *2
                                else:
                                    dmg = ar
                                enemyHP -= dmg
                                print(player.name, 'gastou 20 MP')
                                print (player.name, 'infligiu', dmg, 'de dano a', mon.name)
                                player.mp-=20
                                mgtest=True
                                choiceTest=True
                            else:
                                print(player.name,'não sabe essa magia ( ar )')
                        elif plyrinpt == 'agua':
                            if agua in magiclist:
                                if mon.weakness == 'agua':
                                    dmg = agua *2
                                else:
                                    dmg = agua
                                enemyHP -= dmg
                                print(player.name, 'gastou 10 MP')
                                print (player.name, 'infligiu', dmg, 'de dano a', mon.name)
                                player.mp-=10
                                mgtest=True
                                choiceTest=True
                            else:
                                print(player.name,'não sabe essa magia ( agua )')
                        elif plyrinpt == 'eter':
                            if eter in magiclist:
                                if mon.weakness == 'eter':
                                    dmg = eter *2
                                else:
                                    dmg = eter
                                enemyHP -= dmg
                                print(player.name, 'gastou 30 MP')
                                print(player.name, 'infligiu', dmg, 'de dano a', mon.name)
                                player.mp -= 30
                                mgtest = True
                                choiceTest = True
                            else:
                                print(player.name,'não sabe essa magia ( eter )')
                        elif plyrinpt == 'terra':
                            if terra in magiclist:
                                if mon.weakness == 'terra':
                                    dmg = terra *2
                                else:
                                    dmg = terra
                                enemyHP -= dmg
                                print(player.name, 'gastou 15 MP')
                                print(player.name, 'infligiu', dmg, 'de dano a', mon.name)
                                player.mp-=15
                                mgtest = True
                                choiceTest = True
                            else:
                                print(player.name,'não sabe essa magia ( terra )')
                        elif plyrinpt=='0':
                            mgtest=True
                        else:
                            print('Escolha inválida (', mgtest, ')')
                else:
                    print(player.name,'não sabe nenhuma magia')

            elif (plyrinpt =='i'):
                if(hp25 in itemlist or hp50 in itemlist or mp40 in itemlist or defesa in itemlist):
                    itemtest=False
                    while itemtest==False:
                        plyrinpt = str(input('Escolha o item hp25, hp50, mp40, defesa, ou 0 para cancelar: '))
                        if plyrinpt == 'hp25':
                            if hp25 in itemlist:
                                player.hp = player.hp + hp25
                                if player.hp > player.hpmax:
                                    player.hp = player.hpmax
                                print ('Novo HP de ', player.name, 'é ', player.hp)
                                itemlist.remove(hp25)
                                itemtest=True
                                choiceTest=True
                            else:
                                print(player.name,'não tem esse item ( hp25 )')
                        elif plyrinpt == 'hp50':
                            if hp50 in itemlist:
                                player.hp = player.hp + hp50
                                if player.hp > player.hpmax:
                                    player.hp = player.hpmax
                                print ('Novo HP de ', player.name, 'é ', player.hp)
                                itemlist.remove(hp50)
                                itemtest=True
                                choiceTest=True
                            else:
                                print(player.name,'não tem esse item ( hp50 )')
                        elif plyrinpt == 'mp40':
                            if mp40 in itemlist:
                                player.mp = player.mp + mp40
                                if player.mp > player.mpmax:
                                    player.mp = player.mpmax
                                print ('Novo MP de ', player.mp, 'é ', player.mp)
                                itemlist.remove(mp40)
                                itemtest=True
                                choiceTest=True
                            else:
                                print(player.name,'não tem esse item ( mp40 )')
                        elif plyrinpt == 'defesa':
                            if defesa in itemlist:
                                enemyAtk = enemyAtk-enemyAtk*defesa
                                print ('Defesa aprimorada em ',defesa)
                                itemlist.remove(defesa)
                                itemtest=True
                                choiceTest=True
                            else:
                                print(player.name,'não tem esse item ( defesa )')
                        elif plyrinpt=='0':
                            itemtest=True
                        else:
                            print ('Escolha inválida (',plyrinpt,')')
                else:
                    print(player.name,'não possúi nenhum item')
            else:
                print('Escolha inválida (',plyrinpt,')')
        if(enemyHP > 0 and player.hp > 0 and run==False):
            dmg = mon.atk + random.randint(-3,3) - defend
            if dmg < 0:
                dmg=0
            player.hp -= dmg
            print(player.name,'sofreu',dmg,'de dano de',mon.name)
            defend = 0
        if(enemyHP<=0):
            player.atk += 1
            dinheiro=random.randint(3,15)
            player.money+= dinheiro
            print('\nVitória!',player.name,'encontrou',dinheiro,'ruby\n',player.name,'se sente mais forte\nRuby total:',player.money,'Ruby\n')
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

    if(plyrinpt=='1' or plyrinpt == ''):

        charCreateTest = False
        while (charCreateTest == False):
            sex = input('\nQual o sexo de seu personagem? Digite m para masculino ou f para feminino: ')
            if (sex == 'm' or sex == 'f'):
                player = Player(sex, input('\nEscolha o nome de seu personagem: '))
                confirmTest = False
                while (confirmTest == False):
                    print('\nPersonagem:', player.name, 'de sexo', player.sex)
                    test = input('Confirmar personagem? s/n: ')
                    if (test == 's' or test == ''):
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
