# -*- coding: utf-8 -*-

import random

import math

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

lobo = Monster('Lobo',100,20,0,'fogo',1)
mandrorinha = Monster('Mandrorinha',80,18,0,'ar',1)
carnoceronte = Monster('Carnoceronte',125,21,3,'terra',1)
tantaruga = Monster('Tantaruga', 125,19,5,'terra',1)
kobold = Monster('Kobold',90,22,1,'agua',1)
loboF = Monster('Lobo Faminto',130,23,0,'fogo',2)
diabrete = Monster('Diabrete',112,22,0,'agua',2)
pMercurio = Monster('Planta Mercúrio',115,21,4,'fogo',2)
pNimbus = Monster('Pássaro Nimbus',112,23,0,'ar',2)
undead = Monster('Andarilho do Vale da Morte',100,115,0,'eter',2)
loboA = Monster('Lobo Alpha',150,26,0,'fogo',3)
languia = Monster('Langüia',145,22,1,'terra',3)
nekochan = Monster('Neko-chan',140,26,0,'fogo',3)
golem = Monster('Golem peltre',155,20,8,'agua',3)
eVisgo = Monster('Elemental de Visgo',130,28,0,'ar',3)
loboH = Monster('Lobisomem',160,28,0,'fogo',4)
bGranito = Monster('Bisão de Granito',140,30,9,'terra',4)
cervoru = Monster('Cervoru',163,29,0,'ar',4)
sCaido = Monster('Soldado Caído',150,29,0,'eter',4)
djinn = Monster('Djinn',170,30,0,'agua',4)
loboM = Monster('Lobo Mau',180,30,0,'fogo',5)
cAmaldicoado = Monster('Cruzado Amaldiçoado',200,30,10,'eter',5)
gTerra = Monster('Golem de Terra',175,38,2,'ar',5)
eVulcanico = Monster('Elemental Vulcânico',170,40,0,'agua',5)
leviathan = Monster('Leviatã',180,37,1,'terra',5)

# fim da lista de monstros

# inicio da lista de chefes ( dif = 6 )

loboMP = Monster('Lobo Mau Picapau',200,33,2,'fogo',6)
dragon = Monster('Dragão',250,45,10,'ar',6)
dragonT = Monster('Dragão Terrestre',270,40,25,'terra',6)
dragonW = Monster('Dragão Aquático',250,45,10,'fogo',6)
dragonF = Monster('Grande Dragão de Fogo',260,50,10,'agua',6)
dragonE = Monster('Dragão Etéreo',380,30,60,'eter',6)
dragonA = Monster('Grande Dragão Ancião',330,50,50,'',6)

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
            if name == 'Cheatmode':
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
            self.alignment = 0
            self.hp = self.hpmax
            self.mp = self.mpmax
            self.runCount = 0
            self.deathCount = 0
            self.bossCount = 0
        else:
            print('ERRO: Sexo de personagem inválido (',sex,')')

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

#    elif(id == 6):
#        mon = bosslist[random.randint(0, len(bosslist) - 1)]

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
            print('Digite a para atacar\nDigite d para se defender\nDigite m para usar magia\nDigite i para usar item\nDigite f para fugir')
            if player.hp <= player.hpmax * 0.15 and player.mp >= 5:
                print('Digite l para atacar com Limit Break ( 5 MP )')
            plyrinpt=input('Decisão: ')
            plyrinpt = plyrinpt.lower()
            if(plyrinpt=='a'):
                dmg = player.atk + random.randint(-5,3) - mon.defe
                if dmg < 3:
                    dmg=3
                enemyHP -= dmg
                print(player.name,'infligiu',dmg,'de dano a',mon.name)
                choiceTest=True
            elif plyrinpt=='l':
                if player.hp <= player.hpmax * 0.15 and player.mp >= 5:
                    dmg = player.atk + 80
                    enemyHP -= dmg
                    player.mp -= 5
                    print('Limit Break!')
                    print(player.name, 'infligiu', dmg, 'de dano a', mon.name)
                    choiceTest = True
                else:
                    print('Limit Break indisponível')
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
                                enemyAtk = math.ceil(enemyAtk-enemyAtk*defesa)
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
print ('''\nWolfgang Walder

Kleber Takashi Yoshida

Jorge Gomes

Turma 01N

Olá guerreiro! Você está preparado para a batalha?
Esperamos que sim, pois as criaturas que assombram a região não terão dó de você.
Preste atenção em suas ações e decida cuidadosamente cada passo. Cada decisão, uma consequência. E isso poderá mudar o percurso da estória.
Você terá poderes de ataque, defesa, magia e itens para utilizar. Por isso seja estratégico, pois a vida das pessoas do vilarejo dependerá da sua vitória!
Para o jogo ficar mais dinâmico, crie o seu personagem, o ambiente e os monstros na sua imaginação.

Bom jogo!''')
while(turnOff==False):
    plyrinpt = input('\nO Conto de 1001 Dias\n\nPressione ENTER para começar o jogo\nDigite 0 para desligar o jogo\nDecisão: ').lower()

    if(plyrinpt == '' or plyrinpt == 'enter'):

        charCreateTest = False
        while (charCreateTest == False):
            sex = input('\nQual o sexo de seu personagem? Digite m para masculino ou f para feminino: ').lower()
            if (sex == 'm' or sex == 'f'):
                name = input('\nEscolha o nome de seu personagem: ').capitalize()
                player = Player(sex, name)
                confirmTest = False
                while (confirmTest == False):
                    print('\nPersonagem:', player.name, 'de sexo', player.sex)
                    test = input('Confirmar personagem? S/n: ').lower()
                    if (test == 's' or test == '' or test == 'sim'):
                        confirmTest = True
                        charCreateTest = True
                    elif (test == 'n' or test == 'nao' or test == 'não'):
                        confirmTest = True
                    else:
                        print('Opção inválida (', test, ')')
            else:
                print('Sexo do personagem inválido (', sex, ')')

        # começo da estória

        print('''\n... O mundo não é mais o mesmo, nossas terras estão devastadas por bestas sedentas de sangue. Estamos cansados, cansados de correr, cansados de perder as pessoas que amamos.
Minha alma estava congelada de medo, seus gritos ecoam dentro de mim…

O vale sofre com a invasão de monstros, os primeiros foram fáceis de derrotar, os aldeões fizeram o trabalho rápido, antes que a praga se alastrasse,
no início não tivemos baixas, até que surgiram outros monstros.

Os abissais, era assim que nós os chamávamos, eles eram rápidos, vorazes, sádicos e por fim, carnívoros. Devoravam tudo que se mexia,
gostavam de brincar de caça enquanto observavam o rosto de suas vítimas, ao final do dia, poucos aldeões sobreviveram e se esconderam.

Como enfrentar tais criaturas que com a força de 100 homens partiam suas vítimas ao meio? Como trazer esperança em meio a tanto sofrimento?

“Libertem-n{1}!!” – Disse o ancião do vilarejo.

Os gritos cessaram imediatamente, e as atenções se voltaram para o ancião.

Logo ao fundo alguém gritou “Qual a diferença entre el{2} e os monstros? ”

“El{3} ainda é um{4} de nós, e já faz 100 anos desde que el{5} foi pres{6}, diante dessa situação, é o melhor que nós temos”.'''.format('','o' if player.sex == 'm' else 'a','e' if player.sex == 'm' else 'a','e' if player.sex == 'm' else 'a','' if player.sex == 'm' else 'a','e' if player.sex == 'm' else 'a','o' if player.sex == 'm' else 'a'))
        print('''\nEntão {1} foi libert{2} e o ancião se aproximou com cautela
        
"Vá e acabe com o mal que consome nosso povo, então sua alma amaldiçoada conhecera paz.
Siga até as ruinas ao norte onde se origina o mal que nos assola. Começe sua jornada pela floresta de Norham, e cuidado com os dragões que guardam o caminho até as ruinas" - disse o ancião em uma voz trêmula

Então {3} começou sua ardua jornada até as Ruínas dracônicas ao norte'''.format('',player.name,'o' if player.sex == 'm' else 'a',player.name))
        print('''\n{1} chega a floresta e se depara com dois caminhos

Digite e para seguir o caminho escuro à esquerda
Digite d para seguir o caminho aprazível à direita'''.format('',player.name))
        test = False
        while test == False:
            plyrinpt = input('Escolha: ')
            if plyrinpt == 'e':
                print('\nO chão é úmido sob seus pés. De repente algo surpreende {1}'.format('',player.name))
                bat = battle(1,True)
                if bat == 1:
                    print('\nAo continuar o caminho {1} encontra algo brilhante preso em uma pédra\n{2} adquiriu magia de ar!'.format('',player.name,player.name))
                    magiclist.append(ar)
                elif bat == 2:
                    print('\nO monstro perde o interesse em {1} que após acordar, continua o cominho com o orgulho e o corpo ferido'.format('',player.name))
                else:
                    print('\n{1} foge em direção ao caminho aprazível à direita'.format('',player.name))
                test = True
            elif plyrinpt == 'd':
                print('\n{1} segue tranquilamente pelo caminho e encontra um item hp50!'.format('',player.name))
                itemlist.append(hp50)
                test=True
            else:
                print('Escolha inválida (',plyrinpt,')')
        print('\n{1} chegou em uma clareira onde dormia um grande dragão aládo que acordou com sua chegada e se aproximou para a batalha'.format('',player.name))
        bat = battle(dragon,False)
        if bat==1:
            player.bossCount += 1
            magiclist.append(agua)
            print('\nO Grande dragão aládo jáz aos seus pés derrotado. {1} encontrou algo brilhante na boca do dragão. Magia de água adquirida!'.format('',player.name))
        else:
            print('\n{1} é derrotad{2} pelo dragão, mas consegue escapar em direção ao norte, assim que escapa do dragão',player.name,'desmaia, ao acordar...'.format('',player.name, 'o' if player.sex == 'm' else 'a'))

        print('''\nAo seguir o caminho {1} chega em uma savana. Após muito caminhar, {2} se aproxima de uma formação rochosa com uma caverna
Digite e para entrar na caverna
Digite a para continuar caminhando pela savana'''.format('',player.name,player.name))
        test=False
        while test == False:
            plyrinpt=input('Decisão: ')
            if plyrinpt == 'e':
                print('''\n{1} entra na caverna, onde encontra várias luzes no teto
Ao se distrair {2} é atacad{3} por um monstro!'''.format('',player.name,player.name,'o' if player.sex =='m' else 'a'))
                bat= battle(2,True)
                if bat==1:
                    print('\n{1} encontrou a magia de fogo!'.format('',player.name))
                    magiclist.append(fogo)
                print('\nApós um tempo...')
                bat = battle(2,True)
                if bat ==1:
                    print('\n{1} encontrou um item mp40!'.format('',player.name))
                    itemlist.append(mp40)
                print('{1} chega ao final da caverna e se encontra de volta na savana'.format('',player.name))
                test=True
            elif plyrinpt=='a':
                print('\n{1} continua caminhando pela savana até que se depara com um inimigo'.format('',player.name))
                bat = battle(3,False)
                if bat ==1:
                    print('Por vencer um inimigo nível hard, {1} ganha mais força'.format('',player.name))
                    player.atk+=math.ceil(player.atk*0.1)
                test=True
            else:
                print('Escolha inválida (',plyrinpt,')')
        print('\nNo limíte da savana um grande dragão vermelho espera por {1}'.format('',player.name))
        bat = battle(dragonF,False)
        if bat ==1:
            player.hpmax+=math.ceil(player.hpmax*0.33)
            player.hp = player.hpmax
            player.mp = player.mpmax
            player.bossCount+=1
            print('''\nApós a vitória, a energia do dragão derrotado é absorvida por {1}, que se sente recuperad{2}.
Em pouco tempo {3} chega à costa'''.format('',player.name,'o' if player.sex == 'm' else 'a', player.name))
        else:
            print('''\nO dragão persegue {1} até a costa. {2} pula no mar e o dragão interrompe a perseguição como se temesse a água.
{3} desmaia na praia, e após algum tempo...'''.format('',player.name,player.name,player.name))

        print('''\nTivemos uma luta difícil, não é mesmo?
Continue até o litoral da região. Esse é o caminho certo para Zauberkreis.
Caminhando pela costa {1} avistou dois grupos de criaturas distintas.
Uma se encontra na água e a outra na areia.
Afinal, o que nos espera? Qual caminho seguir?
Opção m para monstro do mar ou a para monstro da areia''' .format('', player.name))
        test=False
        while test == False:
            plyrinpt=input('Escolha: ')
            if plyrinpt=='m':
                print('\n{1} encontrou um Leviatã!'.format('',player.name))
                bat = battle(leviathan,True)
                if bat == 3:
                    print('\n{1} correu em dreção à praia'.format('',player.name))
                    bat = battle(nekochan,False)
                    print('\nO cheiro de churrasquinho de gato empesteia o ar')
                test=True
            elif plyrinpt=='a':
                print('\n{1} encontrou um Neko-chan!'.format('',player.name))
                bat = battle(nekochan,True)
                if bat == 1:
                    print('\nO cheiro de churasquinho de gato empesteia o ar')
                if bat == 3:
                    print('\n{1} correu em dreção ao mar'.format('',player.name))
                    bat = battle(leviathan,False)

                test=True
            else:
                print('Escolha inválida (',plyrinpt,')')
            if bat==1:
                print('{1} encontrou a magia de terra na praia!'.format('',player.name))
                magiclist.append(terra)
        print('''Dando continuidade à sua jornada, {1} se depara com um grande
dragão aquático saltando para fora da água em sua direção e se prepara para a batalha'''.format('',player.name))
        bat = battle(dragonW,False)
        if bat == 1:
            player.mpmax+=math.ceil(player.mpmax*0.5)
            player.mp=player.mpmax
            player.hp=player.hpmax
            player.bossCount+=1
            print('''\nO cheiro de peixe morto indou o ar vitorioso da batalha, {1} seguiu imediatamente em direção ao deserto árido'''.format('',player.name))
        else:
            print('\n{1} foge em direção ao deserto, onde o ar seco faz com que o dragão não consiga persegui-l{2}'.format('',player.name,'o' if player.sex == 'm' else 'a'))

        print('''\nO caminho continua árduo e glorioso. O calor está intenso.
Seguimos para o deserto Tryvalen, onde monstros enfurecidas nos aguardam para a batalha.

Após caminhar por muito tempo sem saber ao certo se estava seguindo na direção certa,
{1} é atacad{2} por bestas furiosas!''' . format('', player.name,'o' if player.sex == 'm' else 'a'))
        bat = battle(4,True)
        if bat==1:
            print('\n{1} encontrou um item hp50!'.format('',player.name))
            itemlist.append(hp50)
        print('\nApós muitas horas mais de caminhada...')
        bat=battle(5,True)
        if bat==1:
            print('\n{1} encontrou um item mp40'.format('',player.name))
            itemlist.append(mp40)
        print('''\nDe repente, ocorre uma explosão de areia logo em frente, e dela
surge o guardião do deserto enfurecido, ao mesmo tempo um aroma nauseabundo de Neko-chan tostado infesta o ambiênte.
O grande dragão terrestre se lança ao combate!''')
        bat=battle(dragonT,False)
        if bat ==1:
            player.hp=player.hpmax
            player.mp=player.mpmax
            magiclist.append(eter)
            player.bossCount+=1
            print('''\nO cheiro intenso de Neko-chan chamuscado emana das entranhas abertas do dragão
{1} caminha até as ruínas dracônicas, agora bem a sua frente e adentra seu interior escuro...
{2} encontrou a magia de eter nas entranhas do dragão!'''.format('',player.name,player.name))
        else:
            print('''\nPara a sorte de {1} o cheiro de Neko-chan chamuscado espantou o dragão terreste depois de desacordar {2}
As ruínas são logo em frente. Não perca mais tempo. Corra até as ruínas!'''.format('',player.name,player.name))

        print('''\nConseguimos! Mas essas ruínas parecem tortuosas e de uma atmosfera tenebrosa.
Espere! o que é aquela chama ardente no final das ruínas?!

Das chamas surge um grande dragão fantasmagórico,
o temido dragão etéreo que dá vida às criaturas amaldiçoadas, o flagelo de Zauberkreis!

Prepare-se para o combate!''')

        test=False
        while test==False:
            bat=battle(dragonE,False)
            if bat==1:
                test=True
                player.hp=player.hpmax
                player.mp=player.mpmax
                player.bossCount+=1
                print('''\nAgora a paz volta às casas dos aldeões,
a vida parece estar de volta ao normal e chegamos ao fim de nossa aventura...
    
Ou será que não?''')
            else:
                test2=False
                while test2==False:
                    plyrinpt=input('\nContinue? S/n : ').lower()
                    if plyrinpt=='n':
                        test=True
                        test2=True
                        print('\nSeu Neko-chan!')
                    elif plyrinpt=='s' or plyrinpt=='':
                        test2=True
                    else:
                        print('\nNão entendeu Neko-chan? SIM ou NÃO')

        if player.bossCount==5:
            print('''\nApós a morte do dragão etéreo, as ruínas dracônicas começaram a desmoronar
{1} correu para fora das ruínas e observa as malditas ruínas desaparcerem... mas algo parece não estar certo... Neko...-chan?
    
Um gigantesco dragão cinzento irrompe das ruínas... é ele, o lendário grande dragão ancião!
    
Esta é a verdadeira batalha final!'''.format('',player.name))
            test=False
            while test==False:
                bat = battle(dragonA,False)
                if bat == 1:
                    print('''\nFinalmente a paz reina novamente em Zauberkreis.
O círculo mágico contempla a vitória do herói que seguramente enfrentou desafios e decisões difíceis. 
Zauberkreis agora possui um novo herói para controlar a harmonia da região!
Parabéns! As estratégias foram muito bem elaboradas e as batalhas corajosamente enfrentadas.
Espero que tenha gostado do jogo.
Até a próxima!''')
                    test=True
                else:
                    test2=False
                    while test2==False:
                        plyrinpt = input('\nContinue? S/n : ').lower()
                        if plyrinpt == 'n':
                            test = True
                            test2 = True
                            print('\nSeu Neko-chan!')
                        elif plyrinpt == 's' or plyrinpt == '':
                            test2 = True
                        else:
                            print('\nNão entendeu Neko-chan? SIM ou NÃO')

        # fim da estória

        print('\n')
        if player.runCount==0:
            if player.deathCount==0:
                print('Ranking: Matador de Dragões')
            elif player.deathCount<=5:
                print('Ranking: Bravo Guerreiro')
            else:
                print('Ranking: Valente Neko-chan')
        else:
            if player.deathCount==0:
                print('Ranking: Maratonista de Zauberkreis')
            elif player.deathCount<=5:
                print('Ranking: Ágil Morto-vivo')
            else:
                print('Ranking: Alma de Neko-chan')

    elif(plyrinpt=='0'):
        print('Desligando o jogo')
        turnOff=True
    else:
        print('Seleção inválida (',plyrinpt,')')
