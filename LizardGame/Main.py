# all the fun loaded stuff
from Load import *
pygame.init()
from Classes import *
from pygame import mixer
import random
import os.path

# base cursor
pygame.mouse.set_cursor(*pygame.cursors.arrow)
# modifiers and whatnot that we couldntput anywhere else
income=1
money_production=0
timer=1
healmod=0
healingrange=1
damage=0
bulletspeed=4
damagetakenmod=0
enemyspawntimer=0
chargemod=1
buildingdied=0
playermods=[income,money_production,damage,bulletspeed,damagetakenmod]
player=player(income,money_production,damage,bulletspeed,damagetakenmod)
playerstuff=[player.income,player.money_production,player.damage,player.bulletspeed,player.damagetakenmod]
screen = pygame.display.set_mode((1200,800))
clock=pygame.time.Clock()
# Sounds
ability_sound=mixer.Sound("sfx_sound_shutdown2.wav")
menu_sound=mixer.Sound("sfx_menu_select2.wav")
destroy_sound=mixer.Sound("sfx_exp_medium7.wav")
hit_sound=mixer.Sound("sfx_sounds_impact1.wav")
explode_sound=mixer.Sound("sfx_sounds_impact11.wav")
enemy_weapon_sound=mixer.Sound("sfx_wpn_laser9.wav")
ally_weapon_sound=mixer.Sound("sfx_wpn_laser6.wav")
shield_weapon_sound=mixer.Sound("sfx_wpn_laser5.wav")
mixer.music.load("BeepBox-Song.wav")
mixer.music.play(-1)
# Base music

# Shop variables
amounts=[5,10,15]# the % of the boost
costs=[100,150,200]
taken=["Untaken","Untaken","Untaken","Untaken"]

sceneline=-1 # cutscene moment


shopbuttons=[None,None,None,None]
buttontypes=[None,None,None,None]
shoppictures=[None,None,None,None]

screenidentity=1
charselectvar=1
Name = ''
# Name input box things
Name_rect = pygame.Rect(215,570,230,35)
color = color_passive
# Building buildings
building_active_attack=False
building_active_heal=False
building_active_money=False
deleting_active=False
action_active=False
# Level
level=1
active = False
# For achievements
game_beaten=0
game_beaten_general=0
game_beaten_perfect=0
# Other variables for the game
movingright=0
movingleft=0
playerx=500
playery=400
playerwidth=191
playerheight=64
current_time=0
shotcooldownbase=0
time=0
shieldabilityactive=0
businessabilityactive=0
healrangeupgrade=False
factorystorage=0
moneyscore=0
blockscore=0
cutscenenumber=0
bossspawned=0
# Load of achievements
Game_Data_Permanent=[]
if os.path.isfile('Persistent_Game_Data.txt'):
    loadpermanent=open("Persistent_Game_Data.txt","r")
    for line in loadpermanent:
        Game_Data_Permanent.append(int(line))
    loadpermanent.close()
    for i in range(len(Game_Data_Permanent)):
        if i == 0:
            game_beaten = Game_Data_Permanent[i]
        if i == 1:
            game_beaten_general = Game_Data_Permanent[i]
        if i == 2:
            game_beaten_perfect = Game_Data_Permanent[i]
# spawns enemies on a timer
def enemyspawn():
    buffpresent=0
    for i in range(3):
        for k in range(len(enemies)):
            if enemies[k].__class__ == buffship:
                buffpresent=1
        if buffpresent == 0 and len(enemies) > 2:
            r=random.randrange(1,4) # Chooses which buff will spawn
            if r == 1:
                b = "Strength"
            if r == 2:
                b = "Firerate"
            if r == 3:
                b = "Projectile_speed"
            a = buffship(b,357+i*80,100,current_time)
            enemies.append(a)
        # spawns other enemies
        if buffpresent == 0 and len(enemies) < 3:
            r = random.randrange(1,3)
            if r == 1:
                a = strongship(357+i*80,100,current_time)
                enemies.append(a)
            if r == 2:
                a = fastship(357+i*80,100,current_time)
                enemies.append(a)
        if buffpresent == 1:
            r = random.randrange(1, 3)
            if r == 1:
                a = strongship(357+i*80, 100, current_time)
                enemies.append(a)
            if r == 2:
                a = fastship(357+i*80, 100, current_time)
                enemies.append(a)
# Healing shield's ability
def healability():
    for i in range(len(player.buildings)):
        if player.buildings[i].__class__ != freespace:
            if player.buildings[i].health<player.buildings[i].maxhealth-30:
                player.buildings[i].health+=30
            else:
                player.buildings[i].health+= player.buildings[i].maxhealth-player.buildings[i].health
    player.charge=0

# First boss generation
junkyard = bossship("Healing", 600, 0, "idfk", 300, 120, 200, 0.745)
teleport = bossship("Teleportation", 600, 0, "stilldfk", 300, 120, 300, 0.33)
Megumin = bossship("EXPLOSION", 600, 0, "stop asking", 300, 120, 300, 0.33)
final = bossship("Shield", 600, 200, "leave me alone", 191, 64, 400, 0.2)
enemies=[]
bullets = []
boss = []
# First Building generation-generates free spaces to build on
for i in range(6):
    x=400
    a=freespace(x+120*i+10*i,700)
    player.buildings.append(a)
# Draws a specified window
def windowdraw(number):
    number=number
    # Home screen, only really has buttons
    if number==1:
        screen.fill((0, 0, 0))
        screen.blit(main_screen_bg, [0, 0])
        for i in range(len(mainmenubuttons)):
            mainmenubuttons[i].draw(screen)
    # Here you choose a character
    if number==2:
        screen.fill((125,255,255))
        screen.blit(abilityheader, (500, 340))
        screen.blit(maintext,(180,100))
        finishbutton.draw(screen)
        charselectbutton.draw(screen)
        backbutton.draw(screen)
        # We cyclse through characters so charselectvar is the one were on currently
        for i in range(4):
            if charselectvar == i+1:
                if i+1 != 4 or game_beaten == 1:
                    for j in range(12):
                        screen.blit(heroes[i][j],charscreencoords[j])
            # Secret character
            if charselectvar == 4 and game_beaten == 0:
                screen.blit(secretabilitytext, (600, 340))
                screen.blit(scaled_secret_man, (150, 220))
                screen.blit(scaled_secret_shield, (500, 253))
                screen.blit(scaled_secret_icon, (670, 214))
                screen.blit(secretloretext,(500,400))
            if charselectvar==5:
                screen.blit(secretabilitytext, (600, 340))
                screen.blit(scaled_secret_man, (150, 220))
                screen.blit(scaled_secret_shield, (500, 253))
                screen.blit(scaled_secret_icon, (670, 214))
                screen.blit(secretloretext, (500, 400))
                screen.blit(secretselectedtext, (400, 720))

    # Achievement screen , if you beat the game in the way intended it shows up
    if number==3:
        screen.fill((0,0,0))
        screen.blit(achievementheader,(310,50))
        screen.blit(achievementsubheader,(210,120))
        if game_beaten == 0:
            screen.blit(achievementtext1false, (520,300))
            if game_beaten_general == 0:
                screen.blit(achievementtext2false, (520,400))
            if game_beaten_perfect == 0:
                screen.blit(achievementtext3false, (520,500))
        if game_beaten == 1:
            screen.blit(achievementtext1true,(300,220))
            screen.blit(achievementsubtext1,(470,270))
            if game_beaten_general == 1:
                screen.blit(achievementtext2true,(25,370))
                screen.blit(achievementsubtext2, (280,420))
            else:
                screen.blit(achievementtext2false, (520, 400))
            if game_beaten_perfect == 1:
                screen.blit(achievementtext3true,(130,520))
                screen.blit(achievementsubtext3, (275,570))
            else:
                screen.blit(achievementtext3false, (520, 500))
        backbutton.draw(screen)
    # The main game screen
    if number==4:
        scoretext=main_font.render("Score: "+str(player.score),1,(250,250,250))
        moneytext=main_font.render("Money: "+str(player.currency),1,(250,250,250))
        screen.fill((250,250,250))
        pygame.draw.rect(screen,(0,0,0),(0,0,350,800),0)
        # Draws Character portrait
        screen.blit(characterpictures[player.character-1],(-20,550))
        screen.blit(abilitypictures[player.character-1],(200,660))
        # Text next to ability button
        screen.blit(etext,(310,670))
        # Other textx
        screen.blit(scoretext,(20,230))
        screen.blit(moneytext,(230,230))
        screen.blit(nametext,(25,760))
        # Checks which character was picked, assigns player a playable shield based on that
        if player.character==1:
            player.shield = strongshield(playerx, playery,chargemod)
            screen.blit(scaled_shield_shield, (playerx, playery))
        if shieldabilityactive ==1:
            screen.blit(shield_shield_shield,(350,playery)) # Bigger shield if the ability is active, specific to strong shield
        if player.character == 2:
            player.shield = healShield(playerx, playery,chargemod)
            screen.blit(scaled_heal_shield, (playerx, playery))
        if player.character==3:
            player.shield = businessshield(playerx, playery,chargemod)
            screen.blit(scaled_money_shield, (playerx, playery))
        if player.character==4:
            player.shield = attackshield(playerx, playery,chargemod)
            screen.blit(scaled_mean_shield, (playerx, playery))
        pygame.draw.rect(screen, (255, 255, 255), (266 - 2, 570 - 2, 30 + 4, 100 + 4), 0) # Draws out charge bar
        pygame.draw.rect(screen, player.shield.colour, (266, 570, 30, player.charge), 0)
        for i in range(len(enemies)):
            # Draws out enemies
            if enemies[i].__class__ == fastship:
                screen.blit(scaled_fast_ship, (enemies[i].x, enemies[i].y))
            if enemies[i].__class__ == strongship:
                screen.blit(scaled_strong_ship, (enemies[i].x, enemies[i].y))
            if enemies[i].__class__ == buffship:
                if enemies[i].buff == "Firerate":
                    screen.blit(scaled_buff_ship_firerate, (enemies[i].x, enemies[i].y))
                    # Check whether the buff hasn't been applied , if not it applies it
                    for j in range(len(enemies)):
                        if enemies[j].__class__==fastship and enemies[j].attackspeed<3 or enemies[j].__class__==strongship and enemies[j].attackspeed<2:
                            enemies[j].attackspeed+=1
                if enemies[i].buff == "Projectile_speed":
                    screen.blit(scaled_buff_ship_speed, (enemies[i].x, enemies[i].y))
                    for j in range(len(enemies)):
                        if enemies[j].__class__==fastship and enemies[j].shotspeed<2 or enemies[j].__class__==strongship and enemies[j].shotspeed<2:
                            enemies[j].shotspeed+=1
                if enemies[i].buff == "Strength":
                    for j in range(len(bullets)):
                        if bullets[j].type=="strongship" and bullets[j].damage<45:
                            bullets[j].damage+=10
                        if bullets[j].type=="fastship" and bullets[j].damage<30:
                            bullets[j].damage+=10
                    screen.blit(scaled_buff_ship_strength, (enemies[i].x, enemies[i].y))
            # Draws out hp bars for enemy ships
            pygame.draw.rect(screen, (0, 0, 0), (enemies[i].x+13 - 2, enemies[i].y+enemies[i].height+5 - 2, 54, 14), 0)
            pygame.draw.rect(screen, (252, 3, 19), (enemies[i].x+13, enemies[i].y+enemies[i].height+5,enemies[i].maxhealth / 100 * enemies[i].health *0.225, 10), 0)
        # Draws out buttons for building buildings
        for i in range(len(buildingbuttons)):
            buildingbuttons[i-1].draw(screen)
        # Draws out buildings
        for i in range(len(player.buildings)):
            screen.blit(player.buildings[i].picture,(player.buildings[i].x,player.buildings[i].y))
            if player.buildings[i].__class__!=freespace:
                # Draws out healthbars for existing buildings
                pygame.draw.rect(screen,(0,0,0), (player.buildings[i].x-2, 720-2, 104, 14), 0)
                pygame.draw.rect(screen, (252, 3, 19), (player.buildings[i].x, 720, player.buildings[i].maxhealth/100*player.buildings[i].health*player.buildings[i].hpbarmod, 10), 0)
        for i in range(len(bullets)):
            # Draws out bullets based on their type
            if bullets[i].type == "player":
                screen.blit(scaled_player_bullet,(bullets[i].x,bullets[i].y))
            if bullets[i].type == "strongship":
                screen.blit(scaled_big_bullet, (bullets[i].x, bullets[i].y))
            if bullets[i].type == "fastship":
                screen.blit(scaled_small_bullet, (bullets[i].x, bullets[i].y))
            if bullets[i].type == "meanplayer":
                screen.blit(scaled_mean_player_bullet,(bullets[i].x,bullets[i].y))
            if bullets[i].type == "BOOM":
                screen.blit(scaled_explosion_boss_bullet, (bullets[i].x, bullets[i].y))
        for i in range(len(boss)):
            # Draws out bosses based on their ability
            if boss[i].ability == "Healing":
                # Name at the top of the screen
                screen.blit(boss1name,(20,40))
                screen.blit(scaled_mechanic_boss, (boss[i].x, boss[i].y))
            if boss[i].ability == "Teleportation":
                screen.blit(boss2name, (20, 40))
                screen.blit(scaled_teleport_boss, (boss[i].x, boss[i].y))
            if boss[i].ability == "EXPLOSION":
                screen.blit(boss3name, (20, 40))
                screen.blit(scaled_explosion_boss, (boss[i].x, boss[i].y))
            if boss[i].ability == "Shield":
                screen.blit(boss4name, (20, 40))
                screen.blit((scaled_mean_shield), (boss[i].x, boss[i].y))
            # Boss health bar on the top of the screen
            pygame.draw.rect(screen, (250, 250, 250), (20 - 2, 70 - 2, 300 + 2, 50 + 4), 0)
            pygame.draw.rect(screen, (252, 3, 19), (
                20, 70, boss[i].maxhealth / 100 * boss[i].health * boss[i].hpbarmod, 50), 0)
    # Shop
    if number==5:
        # Draws out the amount of money, continue button and the header
        moneytext = small_header_font.render("Money: " + str(player.currency), 1, (0, 0, 0))
        screen.fill((224, 45, 90))
        shopcontinuebutton.draw(screen)
        screen.blit(shopheader,(500,80))
        screen.blit(moneytext,(900,200))
        # Draws out the actual power ups you can buy
        if shopbuttons[0] == None or shopbuttons[1] == None or shopbuttons[2] == None or shopbuttons[3] == None:
            for i in range (2):
                # Randomly generates two percentage power up types and their percentage
                a=random.randrange(1,4)
                b=random.choice(amounts)
                if a==1:
                    shoppictures[i]="money_buff"# Sets the power up picture
                    text=" Production + "+str(b)+"%" # Power up name on the button
                    buttontypes[i]="money"+str(b) # Sets the button type for actual increasing
                if a==2:
                    shoppictures[i] = "more_healing"
                    text = "Healing + " + str(b) + "%"
                    buttontypes[i] = "healing" + str(b)
                if a==3:
                    shoppictures[i] = "more_damage"
                    text = "Damage + " + str(b) + "%"
                    buttontypes[i] = "damage" + str(b)
                if a==4:
                    shoppictures[i] = "damage_taken"
                    text = "Damage Taken - " + str(b) + "%"
                    buttontypes[i] = "resist" + str(b)
                if b==5:
                    # Creates the button and adds cost to it based on whether b was 5 ,10 or 15
                    shopbuttons[i] = button((250,250,250),300,200+i*110,500,100,str(text)+"        Cost: 100")
                if b==10:
                    shopbuttons[i] = button((250, 250, 250), 300, 200 + i * 110, 500, 100,str(text)+"        Cost: 150")
                if b==15:
                    shopbuttons[i] = button((250, 250, 250), 300, 200 + i * 110, 500, 100,str(text)+"        Cost: 200")
            for i in range(2):
                # Generates two random power ups from the other pool, pretty much the same principle as the other generation
                d = random.randrange(1, 4)
                if d==1:
                    shoppictures[i+2] = "passive_money"
                    text= "Passive Income + 1        Cost: 200"
                    buttontypes[i+2]="passivemon"
                    shopbuttons[i+2] = button((250,250,250),300,200+(i+2)*110,500, 100,text)
                if d==2:
                    shoppictures[i + 2] = "healing_range"
                    text= "Healing Range + 1        Cost: 200"
                    buttontypes[i+2]="hrange"
                    shopbuttons[i+2] = button((250,250,250),300,200+(i+2)*110,500, 100,text)
                if d==3:
                    shoppictures[i + 2] = "projectile_speed"
                    text= "Shot Speed + 1        Cost: 200"
                    buttontypes[i+2]="shotspd"
                    shopbuttons[i+2] = button((250,250,250),300,200+(i+2)*110,500, 100,text)
                if d==4:
                    shoppictures[i + 2] = "charge_bonus"
                    text= "Charge Modifier + 1        Cost: 300"
                    buttontypes[i+2]="chargespd"
                    shopbuttons[i+2] = button((250,250,250),300,200+(i+2)*110,500, 100,text)
        for i in range(len(shopbuttons)):
            # Draws the buttons and the picture corresponding to the power up
            shopbuttons[i].draw(screen)
            if shoppictures[i]=="money_buff":
                screen.blit(scaled_money_buff, (220, 200 + i * 110))
            if shoppictures[i]=="more_healing":
                screen.blit(scaled_more_healing, (220, 200 + i * 110))
            if shoppictures[i]=="more_damage":
                screen.blit(scaled_more_damage, (220, 200 + i * 110))
            if shoppictures[i]=="damage_taken":
                screen.blit(scaled_damage_taken, (220, 200 + i * 110))
            if shoppictures[i]=="passive_money":
                screen.blit(scaled_passive_money, (220, 200 + i * 110))
            if shoppictures[i]=="healing_range":
                screen.blit(scaled_healing_range, (220, 200 + i * 110))
            if shoppictures[i]=="projectile_speed":
                screen.blit(scaled_projectile_speed, (220, 200 + i * 110))
            if shoppictures[i]=="charge_bonus":
                screen.blit(scaled_charge_bonus, (220, 200 + i * 110))
    # Cutscenes
    if number==6:
        screen.fill((0,0,0))
        # Background
        screen.blit(scaled_humantown,(0,0))
        screen.blit(scaled_lizardtown,(0,400))
        # There is two types of cutcenes, white background and text and visual novel style (alternating)
        # Cutscene 0 is the first cutscene which is the first type
        if cutscenenumber==0:
            pygame.draw.rect(screen, (250, 250, 250), (200, 175, 800, 450), 0)
            if sceneline==0:
                # sceneline means which scene we are on all of the lines themselves are in load
                for i in range(3):
                    screen.blit(c1t1[i],(600-c1t1[i].get_width()/2,350+i*c1t1[i].get_height()+i*10))
            if sceneline==1:
                screen.blit(c1t2,(600-c1t2.get_width()/2,380))

            if sceneline==2:
                for i in range(3):
                    screen.blit(c1t3[i],(600-c1t3[i].get_width()/2,350+i*c1t3[i].get_height()+i*10))
            if sceneline==3:
                for i in range(4):
                    screen.blit(c1t4[i],(600-c1t4[i].get_width()/2,350+i*c1t4[i].get_height()+i*10))
        # Cutscene 1 is type 2 , and so are all the other cutcenes other than 0 and 12 so those are the exact same
        if cutscenenumber==1:
            # Checks for whether the line was said by an ally or an enemy and puts them on the coresponding side
            if c2t[sceneline].side=="ally":
                y=500
            else:
                y=100
            # If it is said by the player, it sets the picture and name to the player picture and name
            if c2t[sceneline].picture==None:
                c2t[sceneline].picture=charcutscenepics[player.character - 1]
            if c2t[sceneline].name=="" and player.getname()!="":
                c2t[sceneline].name=player.getname()
            c2t[sceneline].draw(screen,y)
        # Cutscene 2 is a combination so first it draws out type 1 and then as it progresses it changes to type 2
        if cutscenenumber==2:
            if sceneline==0:
                pygame.draw.rect(screen, (250, 250, 250), (200, 175, 800, 450), 0)
                screen.blit(c3t0,(600-c3t0.get_width()/2,350+c3t0.get_height()+10))
            else:
                if c3t[sceneline-1].side == "ally":
                    y = 500
                else:
                    y = 100
                if c3t[sceneline-1].picture == None:
                    c3t[sceneline-1].picture = charcutscenepics[player.character - 1]
                if c3t[sceneline-1].name == "" and player.getname() != "":
                    c3t[sceneline-1].name = player.getname()
                c3t[sceneline-1].draw(screen,y)
        if cutscenenumber==3:
            if c4t[sceneline].side == "ally":
                y = 500
            else:
                y = 100
            if c4t[sceneline].picture==None:
                c4t[sceneline].picture=charcutscenepics[player.character - 1]
            if c4t[sceneline].name=="" and player.getname()!="":
                c4t[sceneline].name=player.getname()
            c4t[sceneline].draw(screen,y)
        if cutscenenumber==4:
            if c5t[sceneline].side == "ally":
                y = 500
            else:
                y = 100
            if c5t[sceneline].picture==None:
                c5t[sceneline].picture=charcutscenepics[player.character - 1]
            if c5t[sceneline].name=="" and player.getname()!="":
                c5t[sceneline].name=player.getname()
            c5t[sceneline].draw(screen,y)
        if cutscenenumber==5:
            if c6t[sceneline].side == "ally":
                y = 500
            else:
                y = 100
            if c6t[sceneline].picture==None:
                c6t[sceneline].picture=charcutscenepics[player.character - 1]
            if c6t[sceneline].name=="" and player.getname()!="":
                c6t[sceneline].name=player.getname()
            c6t[sceneline].draw(screen,y)
        if cutscenenumber==6:
            if c7t[sceneline].side == "ally":
                y = 500
            else:
                y = 100
            if c7t[sceneline].picture==None:
                c7t[sceneline].picture=charcutscenepics[player.character - 1]
            if c7t[sceneline].name=="" and player.getname()!="":
                c7t[sceneline].name=player.getname()
            c7t[sceneline].draw(screen,y)
        if cutscenenumber==7:
            if c8t[sceneline].side == "ally":
                y = 500
            else:
                y = 100
            if c8t[sceneline].picture==None:
                c8t[sceneline].picture=charcutscenepics[player.character - 1]
            if c8t[sceneline].name=="" and player.getname()!="":
                c8t[sceneline].name=player.getname()
            c8t[sceneline].draw(screen,y)
        if cutscenenumber==8:
            if c9t[sceneline].side == "ally":
                y = 500
            else:
                y = 100
            if c9t[sceneline].picture==None:
                c9t[sceneline].picture=charcutscenepics[player.character - 1]
            if c9t[sceneline].name=="" and player.getname()!="":
                c9t[sceneline].name=player.getname()
            c9t[sceneline].draw(screen,y)
        if cutscenenumber==9:
            if c10t[sceneline].side == "ally":
                y = 500
            else:
                y = 100
            if c10t[sceneline].picture==None:
                c10t[sceneline].picture=charcutscenepics[player.character - 1]
            if c10t[sceneline].name=="" and player.getname()!="":
                c10t[sceneline].name=player.getname()
            c10t[sceneline].draw(screen,y)
        if cutscenenumber==10:
            if c11t[sceneline].side == "ally":
                y = 500
            else:
                y = 100
            if c11t[sceneline].picture==None:
                c11t[sceneline].picture=charcutscenepics[player.character - 1]
            if c11t[sceneline].name=="" and player.getname()!="":
                c11t[sceneline].name=player.getname()
            c11t[sceneline].draw(screen,y)
        if cutscenenumber==11:
            if c12t[sceneline].side == "ally":
                y = 500
            else:
                y = 100
            if c12t[sceneline].picture==None:
                c12t[sceneline].picture=charcutscenepics[player.character - 1]
            if c12t[sceneline].name=="" and player.getname()!="":
                c12t[sceneline].name=player.getname()
            c12t[sceneline].draw(screen,y)
        # Type 1
        if cutscenenumber==12:
            pygame.draw.rect(screen, (250, 250, 250), (200, 175, 800, 450), 0)
            for i in range(3):
                screen.blit(c13t[i], (600 - c13t[i].get_width() / 2, 350 + i * c13t[i].get_height() + i * 10))



running = True
# Spawns the very first wave of enemies
enemyspawn()
# The main loop
while running:
    # checks how many times the loop happened
    current_time = pygame.time.get_ticks()
    # This is the levels, level 1 has no boss so it spawns two waves at the start, the others set the boss for the level
    if level == 1 and bossspawned == 0 and screenidentity == 4:
        if current_time > 1000:
            enemyspawn()
            bossspawned = 1
    if level == 2 and bossspawned == 0 and screenidentity == 4:
        boss = [junkyard]
        bossspawned = 1
    if level == 3 and bossspawned == 0 and screenidentity == 4:
        boss = [teleport]
        bossspawned = 1
    if level == 4 and bossspawned == 0 and screenidentity == 4:
        boss = [Megumin]
        bossspawned = 1
    if level == 5 and bossspawned == 0 and screenidentity == 4:
        boss = [final]
        bossspawned = 1
    # This is the healing the healing building provides
    for i in range(len(player.buildings)):
        if player.buildings[i].__class__ == healbuilding:
            # Business ability makes it heal faster
            if businessabilityactive == 1:
                # Here it heals itself
                if player.buildings[i].health + (player.buildings[i].healing+player.buildings[i].healing/100*player.buildings[i].healm) * player.shield.abilitymult <= player.buildings[i].maxhealth:
                    player.buildings[i].health += (player.buildings[i].healing+player.buildings[i].healing/100*player.buildings[i].healm) * player.shield.abilitymult
                for k in range(player.buildings[i].range):
                    # here it heals the other buildings based on its range
                    if i + k + 1 < 6:
                        if player.buildings[i + k + 1].__class__ != freespace:
                            if player.buildings[i + k + 1].health + (player.buildings[i].healing+player.buildings[i].healing/100*player.buildings[i].healm) * player.shield.abilitymult <= player.buildings[i + k + 1].maxhealth:
                                player.buildings[i + k + 1].health += (player.buildings[i].healing+player.buildings[i].healing/100*player.buildings[i].healm) * player.shield.abilitymult
                    if i - k - 1 >= 0:
                        if player.buildings[i - k - 1].__class__ != freespace:
                            if player.buildings[i - k - 1].health + (player.buildings[i].healing+player.buildings[i].healing/100*player.buildings[i].healm) * player.shield.abilitymult <= player.buildings[i - k - 1].maxhealth:
                                player.buildings[i - k - 1].health += (player.buildings[i].healing+player.buildings[i].healing/100*player.buildings[i].healm) * player.shield.abilitymult
            else:
                # This is the same, just without the healing speed buff the business shield provides
                if player.buildings[i].health + (player.buildings[i].healing+player.buildings[i].healing/100*player.buildings[i].healm) <= player.buildings[i].maxhealth:
                    player.buildings[i].health += player.buildings[i].healing+player.buildings[i].healing/100*player.buildings[i].healm
                for k in range(player.buildings[i].range):
                    if i + k + 1 < 6:
                        if player.buildings[i + k + 1].__class__ != freespace:
                            if player.buildings[i + k + 1].health + (player.buildings[i].healing+player.buildings[i].healing/100*player.buildings[i].healm) <= player.buildings[i + k + 1].maxhealth:
                                player.buildings[i + k + 1].health += player.buildings[i].healing+player.buildings[i].healing/100*player.buildings[i].healm
                    if i - k - 1 >= 0:
                        if player.buildings[i - k - 1].__class__ != freespace:
                            if player.buildings[i - k - 1].health + (player.buildings[i].healing+player.buildings[i].healing/100*player.buildings[i].healm) <= player.buildings[i - k - 1].maxhealth:
                                player.buildings[i - k - 1].health += player.buildings[i].healing+player.buildings[i].healing/100*player.buildings[i].healm
        if player.buildings[i].__class__ == factory:
            # Here the generation building generates money on a cooldown, money producton speeds it up
            if factorystorage < 40:
                if businessabilityactive ==1:
                    factorystorage += (0.1+0.1/100*player.money_production) * player.shield.abilitymult
                else:
                    factorystorage+=0.1+0.1/100*player.money_production
            if factorystorage >= 40:
                # Here it gives player the money and adds a point to their score
                player.currency+=40
                factorystorage=0
                moneyscore+=1

    # Checks for events that can happen such as mouse clicks
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        # If you quit by clicking the x
        if event.type == pygame.QUIT:
            running = False
        # If you press down a key
        if event.type == pygame.KEYDOWN:
            # Checks if a name field is currently activated and ready for typing
            if active == True:
                # deletes the last character written in the field
                if event.key == pygame.K_BACKSPACE:
                    Name = Name[:-1]
                # If you press enter it deactivates
                elif event.key== pygame.K_RETURN:
                    active=False
                # Sets the maximum amountof characters
                elif len(Name) < 10:
                    Name += event.unicode
            # The E key uses an ability if you are currently playing a level
            if event.key==pygame.K_e and screenidentity== 4 and player.charge>=100:
                ability_sound.play()
                if player.shield.__class__==healShield:
                    # Heals all buildings
                    healability()
                if player.shield.__class__==strongshield:
                    # Expands the shield
                    shieldabilityactive=1
                    shieldtimer = current_time
                    player.charge = 0
                if player.shield.__class__==businessshield:
                    # Makes production of buildings faster
                    businessabilityactive=1
                    shieldtimer = current_time
                    player.charge = 0
            if event.key == pygame.K_e and screenidentity == 4 and player.charge >= 20:
                # Fires a projectile
                if player.shield.__class__==attackshield:
                    shield_weapon_sound.play()
                    player.charge -=20
                    # Creates the bullet
                    a = bullet(player.shield.x+player.shield.width/2-50,player.shield.y-100,player.shield.x+player.shield.width/2-50,player.shield.y-101,4,"meanplayer",100,100,0)
                    bullets.append(a)
            if screenidentity == 4:
                # Move the shield with A or D
                if event.key == pygame.K_d:
                    movingright = 1
                if event.key == pygame.K_a:
                    movingleft = 1
        if event.type == pygame.KEYUP:
            # If you let the movement keys go
            if event.key == pygame.K_d:
                movingright = 0
            if event.key == pygame.K_a:
                movingleft = 0

        if active == False:
        # Here it changes the field colour based on whether you are typng in it or not
            color = color_passive
        else:
            color = color_active
        # Grabs the name from the name input field
        Namebox = typing_font.render(Name,True,color)
        # If you click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If your cursor is on the name input field it activates and if you click somewhere else it deactivates
            if Name_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
            # If you click on the New Game button it takes you to character creation
            if startbutton.isOver(pos) and screenidentity == 1:
                menu_sound.play()
                buildingdied = 0
                screenidentity=2
            # If you click the continue button it loads the game on the level you should undergo
            if continuebutton.isOver(pos) and screenidentity == 1 and os.path.isfile('Non-Persistent_Data.txt') and os.path.isfile('Name.txt'):
                Game_Data = [income, money_production, healmod, healingrange, bulletspeed, damagetakenmod, chargemod,
                             level, cutscenenumber, player.score, player.currency, player.character,buildingdied]
                Game_Data_WHY = []
                load = open("Non-Persistent_Data.txt", "r")
                for line in load:
                    Game_Data_WHY.append(int(line))
                load.close()
                for i in range(len(Game_Data)):
                    # Changes all the modifiers to the ones saved
                    Game_Data[i] = Game_Data_WHY[i]
                    if i == 0:
                        income = Game_Data[i]
                    if i == 1:
                        money_production = Game_Data[i]
                    if i == 2:
                        healmod = Game_Data[i]
                    if i == 3:
                        healingrange = Game_Data[i]
                    if i == 4:
                        bulletspeed = Game_Data[i]
                    if i == 5:
                        damagetakenmod = Game_Data[i]
                    if i == 6:
                        chargemod = Game_Data[i]
                    if i == 7:
                        level = Game_Data[i]
                    if i == 8:
                        cutscenenumber = Game_Data[i]
                    if i == 9:
                        player.score = Game_Data[i]
                    if i == 10:
                        player.currency = Game_Data[i]
                    if i == 11:
                        player.character = Game_Data[i]
                    if i == 12:
                        buildingdied = Game_Data[i]
                    # Loads player name
                    loadname = open("Name.txt","r")
                    player.setname(loadname.read())
                    loadname.close()
                    nametext = small_header_font.render(player.getname, 1, (0, 0, 0))
                bossspawned = 0
                # prints the values for testing
                print([income, money_production, healmod, healingrange, bulletspeed, damagetakenmod, chargemod,
                 level, cutscenenumber, player.score, player.currency, player.character])
                screenidentity = 4
                print([income, money_production, healmod, healingrange, bulletspeed, damagetakenmod, chargemod,
                             level, cutscenenumber, player.score, player.currency, player.character])
            # If you press Quit it uh quits
            if quitbutton.isOver(pos) and screenidentity == 1:
                menu_sound.play()
                running = False
            if achievementbutton.isOver(pos) and screenidentity == 1:
                menu_sound.play()
                screenidentity=3
            # Button to cycle through the characters in the creation screen
            if charselectbutton.isOver(pos) and screenidentity == 2 :
                menu_sound.play()
                # Checks whether we reached the last character, takes us back to the first one
                if charselectvar == 4:
                    charselectvar = 0
                if charselectvar==5:
                    charselectvar=0
                charselectvar += 1
            # Goes back to main menu from the creation
            if backbutton.isOver(pos) and screenidentity == 2:
                menu_sound.play()
                screenidentity= 1
            # Goes back from achievements
            if backbutton.isOver(pos) and screenidentity == 3:
                menu_sound.play()
                screenidentity= 1
            # Finishes player creation and remembers the name and character, goes into cutscenes
            if finishbutton.isOver(pos) and screenidentity==2 and game_beaten==1:
                menu_sound.play()
                if Name == "":
                    Name = "Name"
                player.setname(Name)
                nametext = small_header_font.render(player.getname(), 1, (0, 0, 0))
                player.character=charselectvar
                screenidentity= 6
                cutscenenumber=0

            # If game wasn't beaten and you didn't try to get in the game with the locked character it does the same as above
            if finishbutton.isOver(pos) and screenidentity == 2 and game_beaten==0:
                menu_sound.play()
                if charselectvar<4:
                    if Name == "":
                        Name = "Name"
                    player.setname(Name)
                    nametext = small_header_font.render(player.getname(), 1, (0, 0, 0))
                    player.character = charselectvar
                    screenidentity = 6
                    cutscenenumber=0
                # If you tried to go in game with secret character it writes out that you can't do that
                else:
                    charselectvar=5
            # Cancels building and deleting, sets cursor back to arrow
            if cancelbutton.isOver(pos) and screenidentity==4:
                menu_sound.play()
                building_active_attack = False
                building_active_heal = False
                building_active_money = False
                deleting_active=False
                action_active=False
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
            # Starts deleting mode, changes cursor to a different arrow
            if deletebutton.isOver(pos) and screenidentity==4:
                menu_sound.play()
                deleting_active=True
                action_active=True
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
            # 3 Building buttons, one for each building type, starts the building mode for that building, changes cursor to diamond
            if attackbutton.isOver(pos) and screenidentity==4:
                menu_sound.play()
                building_active_attack=True
                action_active=True
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            if healbutton.isOver(pos) and screenidentity==4:
                menu_sound.play()
                building_active_heal=True
                action_active=True
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            if genbutton.isOver(pos) and screenidentity==4:
                menu_sound.play()
                action_active=True
                building_active_money=True
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            # Checks the building list for free spaces, if you click on one it builds and creates a building
            if building_active_attack==True and screenidentity==4:
                for i in range(len(player.buildings)):
                    if pos[0]>player.buildings[i].x and pos[0]<player.buildings[i].x+120 and pos[1]>player.buildings[i].y and pos[1]<player.buildings[i].y+20 and player.buildings[i].__class__==freespace and player.currency>=50:
                        x=player.buildings[i].x
                        y=player.buildings[i].y
                        player.buildings[i]=attackbuilding(x,y)
                        building_active_attack=False
                        action_active=False
                        # Takes away the cost of the building and turns off building mode
                        player.currency-=50
                        pygame.mouse.set_cursor(*pygame.cursors.arrow)
            # Same as above
            if building_active_heal == True and screenidentity == 4:
                for i in range(len(player.buildings)):
                    if pos[0] > player.buildings[i].x and pos[0] < player.buildings[i].x + 120 and pos[1] > player.buildings[i].y and pos[1] < player.buildings[i].y + 20 and player.buildings[i].__class__ == freespace and player.currency>=50:
                        x = player.buildings[i].x
                        y = player.buildings[i].y
                        player.buildings[i] = healbuilding(x, y,healmod,healingrange)
                        building_active_heal = False
                        action_active=False
                        player.currency-=50
                        pygame.mouse.set_cursor(*pygame.cursors.arrow)
            # Same as above
            if building_active_money == True and screenidentity == 4:
                for i in range(len(player.buildings)):
                    if pos[0] > player.buildings[i].x and pos[0] < player.buildings[i].x + 120 and pos[1] > player.buildings[i].y and pos[1] < player.buildings[i].y + 20 and player.buildings[i].__class__ == freespace and player.currency>=40:
                        x = player.buildings[i].x
                        y = player.buildings[i].y
                        player.buildings[i] = factory(x, y)
                        building_active_money = False
                        action_active=False
                        player.currency-=40
                        pygame.mouse.set_cursor(*pygame.cursors.arrow)
            # Deletes the building you click on
            if deleting_active==True and screenidentity==4:
                for i in range(len(player.buildings)):
                    if player.buildings[i].__class__ != freespace and pos[0]>player.buildings[i].x and pos[0]<player.buildings[i].x+player.buildings[i].width and pos[1]>player.buildings[i].y and pos[1]<player.buildings[i].y+player.buildings[i].height:
                        if player.buildings[i].__class__==attackbuilding:
                            x=player.buildings[i].x
                            y=player.buildings[i].y+player.buildings[i].height-10 # We had some problems with picture cropping so it needs to be split
                            player.buildings[i]=freespace(x,y) # Replacesthe building with a free spot
                        if player.buildings[i].__class__ == healbuilding:
                            x = player.buildings[i].x
                            y = player.buildings[i].y + player.buildings[i].height - 20
                            player.buildings[i] = freespace(x, y)
                        if player.buildings[i].__class__==factory:
                            x=player.buildings[i].x
                            y=player.buildings[i].y+player.buildings[i].height
                            player.buildings[i] = freespace(x, y)
                        deleting_active=False
                        action_active=False
                        pygame.mouse.set_cursor(*pygame.cursors.arrow)
            # Shoots a bullet from every attack building towards the cursor position
            if screenidentity == 4 and pos[0]>350:
                if businessabilityactive == 1:
                    # Checkc whether we are on cooldown
                    if current_time - shotcooldownbase > 400/player.shield.abilitymult:
                        shotcooldownbase = current_time # Cooldown until one can shoot again
                        for i in range(len(player.buildings)):
                            if player.buildings[i].__class__ == attackbuilding:
                                ally_weapon_sound.play()
                                # Creates bullet
                                a = bullet(player.buildings[i].x, player.buildings[i].y, pos[0], pos[1], player.bulletspeed, "player",20, 20,20)
                                bullets.append(a)
                # Same as above
                else:
                    if current_time - shotcooldownbase > 400:
                        shotcooldownbase = current_time
                        for i in range(len(player.buildings)):
                            if player.buildings[i].__class__ == attackbuilding:
                                ally_weapon_sound.play()
                                a = bullet(player.buildings[i].x,player.buildings[i].y,pos[0],pos[1],player.bulletspeed,"player",20,20,20)
                                bullets.append(a)
            # Shop
            if screenidentity==5 :
                if shopbuttons[0]!=None and shopbuttons[1]!=None and shopbuttons[2]!=None and shopbuttons[3]!=None:
                    for i in range(len(shopbuttons)):
                        # Checks the type of the button and what it is supposed to give
                        if shopbuttons[i] != None and shopbuttons[i].isOver(pos):
                            for j in range(len(amounts)):
                                # Checks whether the power up has this % and whether it was already bought
                                if buttontypes[i]=="money"+str(amounts[j]) and player.currency>=costs[j] and taken[i]=="Untaken":
                                    # adds to the buffed variable
                                    money_production+=amounts[j]
                                    # Takes away the cost
                                    player.currency-=costs[j]
                                    menu_sound.play()
                                if buttontypes[i]=="healing"+str(amounts[j]) and player.currency>=costs[j] and taken[i]=="Untaken":
                                    healmod+=amounts[j]
                                    player.currency-=costs[j]
                                    menu_sound.play()
                                if buttontypes[i]=="damage"+str(amounts[j]) and player.currency>=costs[j] and taken[i]=="Untaken":
                                    damage+=amounts[j]
                                    player.currency-=costs[j]
                                    menu_sound.play()
                                if buttontypes[i]=="resist"+str(amounts[j]) and player.currency>=costs[j] and taken[i]=="Untaken":
                                    damagetakenmod+=amounts[j]
                                    player.currency-=costs[j]
                                    menu_sound.play()
                            # Same, but the % is always the same
                            if buttontypes[i]=="passivemon" and player.currency>=200 and taken[i]=="Untaken":
                                income+=1
                                player.currency-=200
                                menu_sound.play()
                            if buttontypes[i]=="hrange" and player.currency>=200 and taken[i]=="Untaken":
                                healingrange+=1
                                player.currency-=200
                                menu_sound.play()
                            if buttontypes[i]=="shotspd" and player.currency>=200 and taken[i]=="Untaken":
                                bulletspeed+=1
                                player.currency-=200
                                menu_sound.play()
                            if buttontypes[i]=="chargespd" and player.currency>=300 and taken[i]=="Untaken":
                                chargemod+=1
                                player.currency-=300
                                menu_sound.play()
                if shopcontinuebutton.isOver(pos):
                    menu_sound.play()
                    enemyspawn()
                    if level==1:
                        # Continues onto next cutscene
                        screenidentity=6
                        cutscenenumber=4
                        mixer.music.load("BeepBox-Song.wav")
                        mixer.music.play(-1)
                        # Adds a level
                        level = 2
                        # Saves the data
                        Game_Data = [income, money_production, healmod, healingrange, bulletspeed, damagetakenmod, chargemod,
                             level, cutscenenumber, player.score, player.currency, player.character,buildingdied]
                        save = open("Non-Persistent_Data.txt", "w")
                        for i in range(len(Game_Data)):
                            save.write(str(Game_Data[i]))
                            save.write("\n")
                        save.close()
                        # Saves the player name
                        savename = open("Name.txt","w")
                        savename.write(player.getname())
                        savename.close()
                    elif level==2:
                        screenidentity = 6
                        cutscenenumber = 6
                        mixer.music.load("BeepBox-Song.wav")
                        mixer.music.play(-1)
                        level = 3
                        Game_Data = [income, money_production, healmod, healingrange, bulletspeed, damagetakenmod, chargemod,
                             level, cutscenenumber, player.score, player.currency, player.character,buildingdied]
                        save = open("Non-Persistent_Data.txt", "w")
                        for i in range(len(Game_Data)):
                            save.write(str(Game_Data[i]))
                            save.write("\n")
                        save.close()
                    elif level==3:
                        screenidentity=6
                        cutscenenumber=8
                        mixer.music.load("BeepBox-Song.wav")
                        mixer.music.play(-1)
                        level = 4
                        Game_Data = [income, money_production, healmod, healingrange, bulletspeed, damagetakenmod,
                                     chargemod,
                                     level, cutscenenumber, player.score, player.currency, player.character,buildingdied]
                        save = open("Non-Persistent_Data.txt", "w")
                        for i in range(len(Game_Data)):
                            save.write(str(Game_Data[i]))
                            save.write("\n")
                        save.close()
                    else:
                        screenidentity = 6
                        cutscenenumber = 10
                        mixer.music.load("BeepBox-Song.wav")
                        mixer.music.play(-1)
                        level = 5
                        Game_Data = [income, money_production, healmod, healingrange, bulletspeed, damagetakenmod,chargemod,level, cutscenenumber, player.score, player.currency, player.character,buildingdied]
                        save = open("Non-Persistent_Data.txt", "w")
                        for i in range(len(Game_Data)):
                            save.write(str(Game_Data[i]))
                            save.write("\n")
                        save.close()

            # if it has sceneline+=1 it moves the cutscene along when you click
            if screenidentity==6 and cutscenenumber==0 and sceneline<=3:
                sceneline+=1
            if screenidentity==6 and cutscenenumber==0 and sceneline==4:
                # Moves to the next cutscene and resets which line we are on
                cutscenenumber=1
                sceneline=-1
            if screenidentity==6 and cutscenenumber==1 and sceneline<=49:
                sceneline+=1
            if screenidentity==6 and cutscenenumber==1 and sceneline==50:
                # Once more moves to the next cutscene
                cutscenenumber=2
                sceneline=-1
            if screenidentity == 6 and cutscenenumber == 2 and sceneline <=7:
                sceneline+=1
            if screenidentity == 6 and cutscenenumber == 2 and sceneline ==7:
                # Starts a battle
                screenidentity=4
                level=1
                mixer.music.load("xDeviruchi - Prepare for Battle! .wav")
                mixer.music.play(-1)
                sceneline=0
            if screenidentity == 6 and cutscenenumber == 3 and sceneline <=4:
                sceneline+=1
            if screenidentity == 6 and cutscenenumber == 3 and sceneline ==4:
                # Goes into shop
                screenidentity=5
                mixer.music.load("Little Cactus - 8 Bit Song.wav")
                mixer.music.play(-1)
                sceneline=-1
            if screenidentity == 6 and cutscenenumber == 4 and sceneline <=5:
                sceneline+=1
            if screenidentity == 6 and cutscenenumber == 4 and sceneline ==5:
                screenidentity=4
                mixer.music.load("xDeviruchi - Prepare for Battle! .wav")
                mixer.music.play(-1)
                sceneline=0
            if screenidentity == 6 and cutscenenumber == 5 and sceneline <=9:
                sceneline+=1
            if screenidentity == 6 and cutscenenumber == 5 and sceneline ==9:
                screenidentity = 5
                mixer.music.load("Little Cactus - 8 Bit Song.wav")
                mixer.music.play(-1)
                sceneline = -1
            if screenidentity == 6 and cutscenenumber == 6 and sceneline <=10:
                sceneline+=1
            if screenidentity == 6 and cutscenenumber == 6 and sceneline ==10:
                screenidentity = 4
                mixer.music.load("xDeviruchi - Prepare for Battle! .wav")
                mixer.music.play(-1)
                sceneline=0
            if screenidentity == 6 and cutscenenumber == 7 and sceneline <=11:
                sceneline+=1
            if screenidentity == 6 and cutscenenumber == 7 and sceneline ==11:
                screenidentity = 5
                mixer.music.load("Little Cactus - 8 Bit Song.wav")
                mixer.music.play(-1)
                sceneline = -1
            if screenidentity == 6 and cutscenenumber == 8 and sceneline <=5:
                sceneline+=1
            if screenidentity == 6 and cutscenenumber == 8 and sceneline ==5:
                screenidentity = 4
                mixer.music.load("xDeviruchi - Prepare for Battle! .wav")
                mixer.music.play(-1)
                sceneline = 0
            if screenidentity == 6 and cutscenenumber == 9 and sceneline <=5:
                sceneline+=1
            if screenidentity == 6 and cutscenenumber == 9 and sceneline ==5:
                screenidentity = 5
                mixer.music.load("Little Cactus - 8 Bit Song.wav")
                mixer.music.play(-1)
                sceneline = -1
            if screenidentity == 6 and cutscenenumber == 10 and sceneline <=11:
                sceneline+=1
            if screenidentity == 6 and cutscenenumber == 10 and sceneline ==11:
                screenidentity = 4
                mixer.music.load("xDeviruchi - Prepare for Battle! .wav")
                mixer.music.play(-1)
                sceneline = 0
            if screenidentity == 6 and cutscenenumber == 11 and sceneline <=7:
                sceneline+=1
            if screenidentity == 6 and cutscenenumber == 11 and sceneline ==7:
                cutscenenumber=12
                sceneline=-1
            if screenidentity == 6 and cutscenenumber == 12 and sceneline < 0:
                sceneline+=1
            if screenidentity == 6 and cutscenenumber == 12 and sceneline==0:
                # Ends the game and goes into menu
                level=6
                screenidentity = 4
                sceneline=-1


        # If you move the mouse
        if event.type == pygame.MOUSEMOTION:
        # These change the button colour when they are moused over
            for i in range(len(mainmenubuttons)):
                if mainmenubuttons[i].isOver(pos):
                    mainmenubuttons[i].color = (255,226,68)
                else:
                    mainmenubuttons[i].color = (125,255,255)

            if charselectbutton.isOver(pos):
                charselectbutton.color = (200,200,200)
            else:
                charselectbutton.color = (255,255,255)
            if backbutton.isOver(pos):
                backbutton.color = (200,200,200)
            else:
                backbutton.color = (255,255,255)
            if finishbutton.isOver(pos):
                finishbutton.color = (200,200,200)
            else:
                finishbutton.color = (255, 255, 255)
            if deletebutton.isOver(pos):
                deletebutton.color=(200,200,200)
            else:
                deletebutton.color = (255, 255, 255)
            if cancelbutton.isOver(pos):
                cancelbutton.color=(200,200,200)
            else:
                cancelbutton.color = (255, 255, 255)
            if attackbutton.isOver(pos):
                attackbutton.color=(200,200,200)
            else:
                attackbutton.color = (255, 255, 255)
            if healbutton.isOver(pos):
                healbutton.color=(200,200,200)
            else:
                healbutton.color = (255, 255, 255)
            if genbutton.isOver(pos):
                genbutton.color=(200,200,200)
            else:
                genbutton.color = (255, 255, 255)
            if screenidentity==5:
                for i in range(len(shopbuttons)):
                    if shopbuttons[i] != None:
                        if shopbuttons[i].isOver(pos):
                            shopbuttons[i].color = (200, 200, 200)
                        else:
                            shopbuttons[i].color = (250, 250, 250)
                if shopcontinuebutton.isOver(pos):
                    shopcontinuebutton.color = (200, 200, 200)
                else:
                    shopcontinuebutton.color = (255, 255, 255)

    # Moves the player shield
    if movingright == 1 and (playerx + (playerwidth)) < 1200:
        playerx += 5
    if movingleft == 1 and playerx > 350:
        playerx -= 5
    # Changes cursor to crosshair when in gameplay screen
    if screenidentity == 4:
        if pos[0] > 350 and action_active==False:
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        if pos[0] < 350 and action_active==False:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        # uses the teleportation boss ability
        for i in range(len(enemies)):
            if boss != []:
                if boss[0].ability == "Teleportation":
                    # percentage chance
                    r = random.randrange(0, 50)
                else:
                    r = 2
            else:
                r = 2
            if enemies[i].x + enemies[i].width < 1200 and enemies[i].direction == "r":
                if r == 1:
                    # Blinks enemies around
                    if enemies[i].x + enemies[i].width + 200 > 1200:
                        enemies[i].x = 1200 - enemies[i].width
                    else:
                        enemies[i].x += 200
                else:
                    # enemies move
                    enemies[i].x += enemies[i].speed
            # changes direction if they hit the side of the screen
            if enemies[i].x + enemies[i].width >= 1200 and enemies[i].direction == "r":
                enemies[i].direction = "l"
            if enemies[i].x > 350 and enemies[i].direction == "l":
                if r == 1:
                    # Blink once more
                    if enemies[i].x - 200 < 350:
                        enemies[i].x = 350
                    else:
                        enemies[i].x -= 200
                else:
                    enemies[i].x -= enemies[i].speed
            if enemies[i].x <= 350 and enemies[i].direction == "l":
                enemies[i].direction = "r"
            # Enemy ships shoot on a timer
            if enemies[i].__class__ == fastship:
                if current_time - enemies[i].timer > 2000 / enemies[i].attackspeed:
                    enemy_weapon_sound.play()
                    a = bullet(enemies[i].x, enemies[i].y, enemies[i].x, enemies[i].y + 1, 4, "fastship", 20, 20,20)
                    bullets.append(a)
                    # Resets the timer
                    enemies[i].timer=current_time
            if enemies[i].__class__ == strongship:
                if current_time - enemies[i].timer > 2000 / enemies[i].attackspeed:
                    enemy_weapon_sound.play()
                    a = bullet(enemies[i].x, enemies[i].y, enemies[i].x, enemies[i].y + 1, 4, "strongship", 40, 40,35)
                    bullets.append(a)
                    enemies[i].timer = current_time
        # Bosses shoot
        for i in range(len(boss)):
            if boss[i].ability == "EXPLOSION":
                # Explosion boss shoots special projectiles
                if current_time - boss[i].timer > 4000:
                    a = bullet(boss[i].x, boss[i].y, boss[i].x, boss[i].y + 1, 4, "BOOM", 60, 60,50)
                    bullets.append(a)
                    boss[i].timer = current_time
                    enemy_weapon_sound.play()
            if boss[i].ability == "Healing" or boss[i].ability == "Teleportation" or boss[i].ability == "Shield":
                if current_time - boss[i].timer > 2000:
                    a = bullet(boss[i].x, boss[i].y, boss[i].x, boss[i].y + 1, 4, "strongship", 40, 40,35)
                    bullets.append(a)
                    boss[i].timer = current_time
                    enemy_weapon_sound.play()

        bulletstobedeleted = []
        # Bullet collision detection
        if bullets != [] and player.shield != None:
            for i in range(len(bullets)):
                for k in range(len(enemies)):
                    # checks if a player bullet hit an enemy
                    if bullets[i].x >= enemies[k].x and bullets[i].x <= enemies[k].x + enemies[k].width and bullets[i].type == "player" or bullets[i].x + bullets[i].width >= enemies[k].x and bullets[i].x + bullets[i].width <= enemies[k].x + enemies[k].width and bullets[i].type == "player":
                        if bullets[i].y >= enemies[k].y and bullets[i].y <= enemies[k].y + enemies[k].height and bullets[i].type == "player" or bullets[i].y + bullets[i].height >= enemies[k].y and bullets[i].y + bullets[i].height <= enemies[k].y + enemies[k].height and bullets[i].type == "player":
                            hit_sound.play()
                            # checks whether this bullet is already supposed to be deleted so it doesn't crash
                            for j in range(len(bulletstobedeleted)):
                                if i==bulletstobedeleted[j]:
                                    bulletstobedeleted.pop(j)
                            bulletstobedeleted.append(i)
                            # Enemies loose health
                            enemies[k].health-=10+10/100*player.damage
                    # Same, just for special shield bullets
                    if bullets[i].x >= enemies[k].x and bullets[i].x <= enemies[k].x + enemies[k].width and bullets[i].type == "meanplayer" or bullets[i].x + bullets[i].width >= enemies[k].x and bullets[i].x + bullets[i].width <= enemies[k].x + enemies[k].width and bullets[i].type == "meanplayer":
                        if bullets[i].y >= enemies[k].y and bullets[i].y <= enemies[k].y + enemies[k].height and bullets[i].type == "meanplayer" or bullets[i].y + bullets[i].height >= enemies[k].y and bullets[i].y + bullets[i].height <= enemies[k].y + enemies[k].height and bullets[i].type == "meanplayer":
                            hit_sound.play()
                            for j in range(len(bulletstobedeleted)):
                                if i==bulletstobedeleted[j]:
                                    bulletstobedeleted.pop(j)
                            bulletstobedeleted.append(i)
                            enemies[k].health -= 50
                for k in range(len(boss)):
                    # If player bullets hit the boss
                    if bullets[i].x >= boss[k].x and bullets[i].x <= boss[k].x + boss[k].width and bullets[i].type == "player" or bullets[i].x + bullets[i].width >= boss[k].x and bullets[i].x + bullets[i].width <= boss[k].x + boss[k].width and bullets[i].type == "player":
                        if bullets[i].y >= boss[k].y and bullets[i].y <= boss[k].y + boss[k].height and bullets[i].type == "player" or bullets[i].y + bullets[i].height >= boss[k].y and bullets[i].y + bullets[i].height <= boss[k].y + boss[k].height and bullets[i].type == "player":
                            hit_sound.play()
                            for j in range(len(bulletstobedeleted)):
                                if i == bulletstobedeleted[j]:
                                    bulletstobedeleted.pop(j)
                            bulletstobedeleted.append(i)
                            boss[k].health -= 10+10/100*player.damage
                    # If special player bullets hit the boss
                    if bullets[i].x >= boss[k].x and bullets[i].x <= boss[k].x + boss[k].width and bullets[i].type == "meanplayer" or bullets[i].x + bullets[i].width >= boss[k].x and bullets[i].x + bullets[i].width <= boss[k].x + boss[k].width and bullets[i].type == "meanplayer":
                        if bullets[i].y >= boss[k].y and bullets[i].y <= boss[k].y + boss[k].height and bullets[i].type == "meanplayer" or bullets[i].y + bullets[i].height >= boss[k].y and bullets[i].y + bullets[i].height <= boss[k].y + boss[k].height and bullets[i].type == "meanplayer":
                            hit_sound.play()
                            for j in range(len(bulletstobedeleted)):
                                if i == bulletstobedeleted[j]:
                                    bulletstobedeleted.pop(j)
                            bulletstobedeleted.append(i)
                            boss[k].health -= 50
                for k in range(len(player.buildings)):
                    # If player building is hit by a small enemy
                    if player.buildings[k].__class__ != freespace:
                        if bullets[i].x >= player.buildings[k].x and bullets[i].x <= player.buildings[k].x + player.buildings[k].width and bullets[i].type == "fastship" or bullets[i].x + bullets[i].width >= player.buildings[k].x and bullets[i].x + bullets[i].width <= player.buildings[k].x + player.buildings[k].width and bullets[i].type == "fastship":
                            if bullets[i].y >= player.buildings[k].y and bullets[i].y <= player.buildings[k].y + player.buildings[k].height and bullets[i].type == "fastship" or bullets[i].y + bullets[i].height >= player.buildings[k].y and bullets[i].y + bullets[i].height <= player.buildings[k].y + player.buildings[k].height and bullets[i].type == "fastship":
                                hit_sound.play()
                                for j in range(len(bulletstobedeleted)):
                                    if i == bulletstobedeleted[j]:
                                        bulletstobedeleted.pop(j)
                                bulletstobedeleted.append(i)
                                player.buildings[k].health-=bullets[i].damage-10/100*player.damagetakenmod

                for k in range(len(player.buildings)):
                    # If player building was hit by a big enemy
                    if player.buildings[k].__class__ != freespace:
                        if bullets[i].x >= player.buildings[k].x and bullets[i].x <= player.buildings[k].x + player.buildings[k].width and bullets[i].type == "strongship" or bullets[i].x + bullets[i].width >= player.buildings[k].x and bullets[i].x + bullets[i].width <= player.buildings[k].x + player.buildings[k].width and bullets[i].type == "strongship":
                            if bullets[i].y >= player.buildings[k].y and bullets[i].y <= player.buildings[k].y + player.buildings[k].height and bullets[i].type == "strongship" or bullets[i].y + bullets[i].height >= player.buildings[k].y and bullets[i].y + bullets[i].height <= player.buildings[k].y + player.buildings[k].height and bullets[i].type == "strongship":
                                hit_sound.play()
                                for j in range(len(bulletstobedeleted)):
                                    if i == bulletstobedeleted[j]:
                                        bulletstobedeleted.pop(j)
                                bulletstobedeleted.append(i)
                                player.buildings[k].health-=bullets[i].damage-20/100*player.damagetakenmod
                for k in range(len(player.buildings)):
                    # If player building was hit by the special boss bullet
                    if player.buildings[k].__class__ != freespace:
                        if bullets[i].x >= player.buildings[k].x and bullets[i].x <= player.buildings[k].x + player.buildings[k].width and bullets[i].type == "BOOM" or bullets[i].x + bullets[i].width >= player.buildings[k].x and bullets[i].x + bullets[i].width <= player.buildings[k].x + player.buildings[k].width and bullets[i].type == "BOOM":
                            if bullets[i].y >= player.buildings[k].y and bullets[i].y <= player.buildings[k].y + player.buildings[k].height and bullets[i].type == "BOOM" or bullets[i].y + bullets[i].height >= player.buildings[k].y and bullets[i].y + bullets[i].height <= player.buildings[k].y + player.buildings[k].height and bullets[i].type == "BOOM":
                                hit_sound.play()
                                for j in range(len(bulletstobedeleted)):
                                    if i == bulletstobedeleted[j]:
                                        bulletstobedeleted.pop(j)
                                bulletstobedeleted.append(i)
                                for j in range(len(player.buildings)):
                                    # Special boss bullet hits all buildings
                                    if player.buildings[j].__class__ != freespace:
                                        player.buildings[j].health -= bullets[i].damage-50/100*player.damagetakenmod

                # Blocking bullets with the player shield
                if bullets[i].x >= player.shield.x and bullets[i].x <= player.shield.x + player.shield.width and bullets[i].type == "fastship" or bullets[i].x + bullets[i].width >= player.shield.x and bullets[i].x + bullets[i].width <= player.shield.x + player.shield.width and bullets[i].type == "fastship":
                    if bullets[i].y >= player.shield.y and bullets[i].y <= player.shield.y + player.shield.height and bullets[i].type == "fastship" or bullets[i].y + bullets[i].height >= player.shield.y and bullets[i].y + bullets[i].height <= player.shield.y + player.shield.height and bullets[i].type == "fastship":
                        # If we block a small enemy bullet
                        for j in range(len(bulletstobedeleted)):
                            if i == bulletstobedeleted[j]:
                                bulletstobedeleted.pop(j)
                        bulletstobedeleted.append(i)
                        # Adds ability charge when no ability is in use
                        if shieldabilityactive != 1 and businessabilityactive != 1:
                            if player.charge + 2 * player.shield.chargespeed > 100:
                                player.charge = 100
                                print(player.charge)
                            else:
                                player.charge += 2 * player.shield.chargespeed
                                print(player.charge)
                # Blocking strong enemy bullets
                if bullets[i].x >= player.shield.x and bullets[i].x <= player.shield.x + player.shield.width and bullets[i].type == "strongship" or bullets[i].x + bullets[i].width >= player.shield.x and bullets[i].x + bullets[i].width <= player.shield.x + player.shield.width and bullets[i].type == "strongship":
                    if bullets[i].y >= player.shield.y and bullets[i].y <= player.shield.y + player.shield.height and bullets[i].type == "strongship" or bullets[i].y + bullets[i].height >= player.shield.y and bullets[i].y + bullets[i].height <= player.shield.y + player.shield.height and bullets[i].type == "strongship":
                        for j in range(len(bulletstobedeleted)):
                            if i == bulletstobedeleted[j]:
                                bulletstobedeleted.pop(j)
                        bulletstobedeleted.append(i)
                        if shieldabilityactive != 1 and businessabilityactive != 1:
                            if player.charge + 2 * player.shield.chargespeed > 100:
                                player.charge = 100
                                print(player.charge)
                            else:
                                player.charge += 2 * player.shield.chargespeed
                                print(player.charge)
                # Blocking special boss bullets
                if bullets[i].x >= player.shield.x and bullets[i].x <= player.shield.x + player.shield.width and bullets[i].type == "BOOM" or bullets[i].x + bullets[i].width >= player.shield.x and bullets[i].x + bullets[i].width <= player.shield.x + player.shield.width and bullets[i].type == "BOOM":
                    if bullets[i].y >= player.shield.y and bullets[i].y <= player.shield.y + player.shield.height and bullets[i].type == "BOOM" or bullets[i].y + bullets[i].height >= player.shield.y and bullets[i].y + bullets[i].height <= player.shield.y + player.shield.height and bullets[i].type == "BOOM":
                        for j in range(len(bulletstobedeleted)):
                            if i == bulletstobedeleted[j]:
                                bulletstobedeleted.pop(j)
                        bulletstobedeleted.append(i)
                        if shieldabilityactive != 1 and businessabilityactive != 1:
                            if player.charge + 2 * player.shield.chargespeed > 100:
                                player.charge = 100
                                print(player.charge)
                            else:
                                player.charge += 2 * player.shield.chargespeed
                                print(player.charge)
                            for j in range(len(player.buildings)):
                                # Special boss bullet doesn't get completely blocked, just deals half the damage
                                if player.buildings[j].__class__ != freespace:
                                    player.buildings[j].health -= 25-25/100*player.damagetakenmod

                            blockscore += 1
                # Edge of the screen deletion
                if bullets[i].x + bullets[i].dx + bullets[i].width > 1200 or bullets[i].x + bullets[i].dx < 350 or bullets[i].y + bullets[i].dy +bullets[i].height > 800 or bullets[i].y + bullets[i].dy < 0:
                    for j in range(len(bulletstobedeleted)):
                        if i == bulletstobedeleted[j]:
                            bulletstobedeleted.pop(j)
                    bulletstobedeleted.append(i)
               # Bullets hurt a tiny bit when they hit the floor
                if bullets[i].y+bullets[i].dy+bullets[i].height >=720 and bullets[i].type=="fastship" or bullets[i].y+bullets[i].dy+bullets[i].height >=720 and bullets[i].type=="strongship":
                    explode_sound.play()
                    for j in range(len(bulletstobedeleted)):
                        if i == bulletstobedeleted[j]:
                            bulletstobedeleted.pop(j)
                    bulletstobedeleted.append(i)
                    for j in range (len(player.buildings)):
                        # Deals the small floor damage
                        if player.buildings[j].__class__!=freespace:
                            player.buildings[j].health-=5-5/100*player.damagetakenmod
                # Special boss bullets deal their full damage when they hit the floor
                if bullets[i].y + bullets[i].dy + bullets[i].height >= 720 and bullets[i].type == "BOOM":
                    explode_sound.play()
                    for j in range(len(bulletstobedeleted)):
                        if i == bulletstobedeleted[j]:
                            bulletstobedeleted.pop(j)
                    bulletstobedeleted.append(i)
                    for j in range(len(player.buildings)):
                        if player.buildings[j].__class__ != freespace:
                            player.buildings[j].health -= 50-50/100*player.damagetakenmod
                # Same thing, only the shield spans the entire screen
                if shieldabilityactive ==1:
                    if bullets[i].y >= player.shield.y and bullets[i].y <= player.shield.y + player.shield.height and bullets[i].type == "fastship" or bullets[i].y + bullets[i].height >= player.shield.y and bullets[i].y + bullets[i].height <= player.shield.y + player.shield.height and bullets[i].type == "fastship":
                        for j in range(len(bulletstobedeleted)):
                            if i == bulletstobedeleted[j]:
                                bulletstobedeleted.pop(j)
                        bulletstobedeleted.append(i)
                    if bullets[i].y >= player.shield.y and bullets[i].y <= player.shield.y + player.shield.height and bullets[i].type == "strongship" or bullets[i].y + bullets[i].height >= player.shield.y and bullets[i].y + bullets[i].height <= player.shield.y + player.shield.height and bullets[i].type == "strongship":
                        for j in range(len(bulletstobedeleted)):
                            if i == bulletstobedeleted[j]:
                                bulletstobedeleted.pop(j)
                        bulletstobedeleted.append(i)
                    if bullets[i].y >= player.shield.y and bullets[i].y <= player.shield.y + player.shield.height and bullets[i].type == "BOOM" or bullets[i].y + bullets[i].height >= player.shield.y and bullets[i].y + bullets[i].height <= player.shield.y + player.shield.height and bullets[i].type == "BOOM":
                        for j in range(len(bulletstobedeleted)):
                            if i == bulletstobedeleted[j]:
                                bulletstobedeleted.pop(j)
                        bulletstobedeleted.append(i)
                        for j in range(len(player.buildings)):
                            if player.buildings[j].__class__ != freespace:
                                player.buildings[j].health -= 25-25/100*player.damagetakenmod
                # If they don't hit they move
                bullets[i].x += bullets[i].dx
                bullets[i].y += bullets[i].dy
            # Here it deletes the bullets that hit
            for i in range(len(bulletstobedeleted)):
                del bullets[bulletstobedeleted[len(bulletstobedeleted)-i-1]]
            for i in range(len(player.buildings)):
                # Checks whether the building hit 0 hp and destroys the ones that did
                if player.buildings[i].__class__!=freespace and player.buildings[i].health <= 0:
                    buildingdied = 1 # Modifier for an achievement
                    if player.buildings[i].__class__ == attackbuilding:
                        destroy_sound.play()
                        x = player.buildings[i].x
                        y = player.buildings[i].y + player.buildings[i].height - 10
                        player.buildings[i] = freespace(x, y)
                    if player.buildings[i].__class__ == healbuilding:
                        destroy_sound.play()
                        x = player.buildings[i].x
                        y = player.buildings[i].y + player.buildings[i].height - 20
                        player.buildings[i] = freespace(x, y)
                    if player.buildings[i].__class__ == factory:
                        destroy_sound.play()
                        x = player.buildings[i].x
                        y = player.buildings[i].y + player.buildings[i].height
                        player.buildings[i] = freespace(x, y)
        enemiestobedeleted=[]
        bosstobedeleted=[]
        # Checks whether enemies hit 0 hp, if it's a buffship it gets rid of the buff
        for i in range(len(enemies)):
            if enemies[i].health <= 0:
                enemiestobedeleted.append(i)
                if enemies[i].__class__==buffship:
                    if enemies[i].bufftype=="Strenght":
                        for j in range(len(bullets)):
                            bullets[j].damage-=10
                    if enemies[i].bufftype=="Firerate":
                        for j in range(len(enemies)):
                            if enemies[j].__class__==fastship or enemies[j].__class__==strongship:
                                enemies[j].attackspeed-=0.1
                    if enemies[i].bufftype == "Projectile_speed":
                        for j in range(len(enemies)):
                            if enemies[j].__class__ == fastship or enemies[j].__class__ == strongship:
                                enemies[j].shotspeed-= 1
        # Deletes dead enemies
        for i in range(len(enemiestobedeleted)):
            destroy_sound.play()
            del enemies[enemiestobedeleted[len(enemiestobedeleted)-i-1]]
            # First boss heals when enemies die so this is how that works
            if boss != []:
                if boss[0].ability == "Healing":
                    if boss[0].health + 20 > boss[0].maxhealth:
                        boss[0].health = boss[0].maxhealth
                    else:
                        boss[0].health += 20
        # Checks if a boss hit 0 hp
        for i in range(len(boss)):
            if boss[i].health <= 0:
                bosstobedeleted.append(i)
        # Deletes dead boss, adds score for beating it
        for i in range(len(bosstobedeleted)):
            destroy_sound.play()
            del boss[bosstobedeleted[len(bosstobedeleted) - i - 1]]
            player.score += 10
        # Special boss ability of final boss, moves to where the player shoots to block bullets
        for i in range(len(boss)):
            if boss[i].ability == "Shield":
                for k in range(len(bullets)):
                    if bullets[k].type == "player" and bullets[k].y > boss[i].y or bullets[k].type == "meanplayer" and bullets[k].y > boss[i].y:
                        if bullets[k].x + bullets[k].width / 2 > boss[i].x + boss[i].width / 2:
                            boss[i].x += 5
                        if bullets[k].x + bullets[k].width / 2 < boss[i].x + boss[i].width / 2:
                            boss[i].x -= 5
                        break
        # Timer for enemy spawning
        if current_time - enemyspawntimer > 20000 and boss != []:
            enemyspawn()
            enemyspawntimer = current_time

        # If a level is beaten, plays cutscene
        if boss == [] and enemies == []:
            if level ==1:
                screenidentity = 6
                cutscenenumber=3
                bossspawned = 0
                mixer.music.load("BeepBox-Song.wav")
                mixer.music.play(-1)
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
            if level==2:
                screenidentity = 6
                cutscenenumber = 5
                bossspawned = 0
                mixer.music.load("BeepBox-Song.wav")
                mixer.music.play(-1)
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
            if level==3:
                screenidentity=6
                cutscenenumber=7
                bossspawned=0
                mixer.music.load("BeepBox-Song.wav")
                mixer.music.play(-1)
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
            if level==4:
                screenidentity=6
                cutscenenumber=9
                bossspawned = 0
                mixer.music.load("BeepBox-Song.wav")
                mixer.music.play(-1)
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
            if level==5:
                screenidentity = 6
                cutscenenumber =11
                bossspawned = 0
                mixer.music.load("BeepBox-Song.wav")
                mixer.music.play(-1)
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
            # If the game is completely beaten ir saves achievements and returns to menu
            if level>5:
                game_beaten = 1
                if player.character == 4:
                    game_beaten_general = 1
                if buildingdied == 0:
                    game_beaten_perfect = 1
                Persistent_Game_Data = [game_beaten, game_beaten_general, game_beaten_perfect]
                save = open("Persistent_Game_Data.txt", "w")
                for i in range(len(Persistent_Game_Data)):
                    save.write(str(Persistent_Game_Data[i]))
                    save.write("\n")
                save.close
                bossspawned = 0
                level = 1
                screenidentity = 1
                # Boss reset
                junkyard = bossship("Healing", 600, 0, "idfk", 300, 120, 200, 0.745)
                teleport = bossship("Teleportation", 600, 0, "stilldfk", 300, 120, 300, 0.33)
                Megumin = bossship("EXPLOSION", 600, 0, "stop asking", 300, 120, 300, 0.33)
                final = bossship("Shield", 600, 200, "leave me alone", 191, 64, 400, 0.2)
                enemyspawn()
    # Adds money based on passive income
    if screenidentity==4 and timer==40:
        player.currency+=player.income
        timer=0
    # Moves timer
    if screenidentity==4:
        timer+=1
    windowdraw(screenidentity)
    if screenidentity == 2:
        Name_rect.w = max(230,Namebox.get_width()+10)
        screen.blit(Namebox, (Name_rect.x+5,Name_rect.y))
        pygame.draw.rect(screen,color,Name_rect,2)
    # all the timers
    if shieldabilityactive ==1:
        if current_time - shieldtimer > 5000:
            shieldabilityactive = 0
    if businessabilityactive == 1:
        if current_time - shieldtimer > 5000:
            businessabilityactive = 0
    # Adds shop buffs
    for i in range(len(playerstuff)):
        if playerstuff[i]!=playermods[i]:
            playerstuff[i]=playermods[i]

    pygame.display.update()
    clock.tick(60)