import pygame
from Classes import *

pygame.init()
# Images
main_screen_bg=pygame.image.load("mainscreen.png")
pygame.display.set_caption("lizardshieldthing")
heal_shield_img = pygame.image.load("healshield.png")
mean_shield_img = pygame.image.load("meanshield.png")
money_shield_img = pygame.image.load("moneyshield.png")
shield_shield_img = pygame.image.load("shieldshield.png")
heal_man_img = pygame.image.load("healman.png")
mean_man_img = pygame.image.load("meanman.png")
money_man_img = pygame.image.load("moneyman.png")
shield_man_img = pygame.image.load("shieldman.png")
secret_man_img = pygame.image.load("secret_character.png")
secret_shield_img=pygame.image.load("secret_shield.png")
heal_icon=pygame.image.load("Healicon.png")
shield_icon=pygame.image.load("Shieldicon.png")
money_icon=pygame.image.load("Moneyicon.png")
attack_icon=pygame.image.load("Attackicon.png")
secret_icon=pygame.image.load("secreticon.png")
attack_building=pygame.image.load("attack_building.png")
heal_building=pygame.image.load("heal_building.png")
money_building=pygame.image.load("money_building.png")
untaken=pygame.image.load("untaken.png")
big_bullet=pygame.image.load("big_enemy_bullet.png")
small_bullet=pygame.image.load("small_enemy_bullet.png")
player_bullet=pygame.image.load("player_bullet.png")
mean_player_bullet=pygame.image.load("mean_player_bullet.png")
strong_ship=pygame.image.load("big_ship.png")
fast_ship=pygame.image.load("small_ship.png")
buff_ship_strength=pygame.image.load("attack_buff_ship.png")
buff_ship_firerate=pygame.image.load("fire_rate_buff_ship.png")
buff_ship_speed=pygame.image.load("projectile_speed_buff_ship.png")
money_buff=pygame.image.load("more_money.png")
passive_money=pygame.image.load("passive_money.png")
more_healing=pygame.image.load("healing_amount.png")
healing_range=pygame.image.load("healing_range.png")
more_damage=pygame.image.load("damage.png")
projectile_speed=pygame.image.load("bullet_speed.png")
damage_taken=pygame.image.load("damage_taken.png")
charge_bonus=pygame.image.load("charge.png")
background=pygame.image.load("background.png")
humantown=pygame.image.load("humantown.png")
lizardtown=pygame.image.load("lizardtown.png")
baselizard=pygame.image.load("baselizard.png")
finalboss=pygame.image.load("finalbosspic.png")
mechanicboss=pygame.image.load("mechanicbosspic.png")
teleporterboss=pygame.image.load("tpbosspic.png")
bomberman=pygame.image.load("bombermanpic.png")
meanlizard=pygame.image.load("meanlizard.png")
mechanic_boss=pygame.image.load("Mechanic_Boss.png")
teleport_boss=pygame.image.load("Teleport_Boss.png")
explosion_boss=pygame.image.load("BOOMBOI.png")
explosion_boss_bullet=pygame.image.load("BOOMBOISON.png")
heallizard=pygame.image.load("heallizard.png")
shieldlizard=pygame.image.load("shieldlizard.png")
moneylizard=pygame.image.load("moneylizard.png")
# Resizes
rescaled_mean_lizard=pygame.transform.scale(meanlizard,(200,200))
rescaled_heal_lizard=pygame.transform.scale(heallizard,(200,200))
rescaled_shield_lizard=pygame.transform.scale(shieldlizard,(200,200))
rescaled_money_lizard=pygame.transform.scale(moneylizard,(200,200))
scaled_bomberman=pygame.transform.scale(bomberman,(200,200))
scaled_tpboss=pygame.transform.scale(teleporterboss,(200,200))
scaled_mechanicboss=pygame.transform.scale(mechanicboss,(200,200))
scaled_baselizard=pygame.transform.scale(baselizard,(200,200))
scaled_finalboss=pygame.transform.scale(finalboss,(200,200))
scaled_humantown=pygame.transform.scale(humantown,(1200,400))
scaled_lizardtown=pygame.transform.scale(lizardtown,(1200,400))
scaled_heal_man=pygame.transform.scale(heal_man_img, (350,350))
scaled_shield_man=pygame.transform.scale(shield_man_img, (350,350))
scaled_money_man=pygame.transform.scale(money_man_img, (350,350))
scaled_mean_man=pygame.transform.scale(mean_man_img, (350,350))
scaled_secret_man=pygame.transform.scale(secret_man_img, (350,350))
scaled_shield_shield=pygame.transform.scale(shield_shield_img, (191,64))
shield_shield_shield=pygame.transform.scale(shield_shield_img, (850,64))
scaled_mean_shield=pygame.transform.scale(mean_shield_img, (191,64))
scaled_money_shield=pygame.transform.scale(money_shield_img, (191,64))
scaled_heal_shield=pygame.transform.scale(heal_shield_img, (191,64))
scaled_secret_shield=pygame.transform.scale(secret_shield_img, (191,64))
scaled_shield_icon=pygame.transform.scale(shield_icon,(150,150))
scaled_heal_icon=pygame.transform.scale(heal_icon,(150,150))
scaled_money_icon=pygame.transform.scale(money_icon,(150,150))
scaled_attack_icon=pygame.transform.scale(attack_icon,(150,150))
scaled_secret_icon=pygame.transform.scale(secret_icon,(150,150))
main_scaled_heal_man=pygame.transform.scale(heal_man_img, (270,270))
main_scaled_shield_man=pygame.transform.scale(shield_man_img, (270,270))
main_scaled_money_man=pygame.transform.scale(money_man_img, (270,270))
main_scaled_mean_man=pygame.transform.scale(mean_man_img, (270,270))
scaled_big_bullet=pygame.transform.scale(big_bullet,(40,40))
scaled_small_bullet=pygame.transform.scale(small_bullet,(20,20))
scaled_player_bullet=pygame.transform.scale(player_bullet,(20,20))
scaled_mean_player_bullet=pygame.transform.scale(mean_player_bullet,(100,100))
scaled_fast_ship=pygame.transform.scale(fast_ship,(80,80))
scaled_strong_ship=pygame.transform.scale(strong_ship,(80,80))
scaled_buff_ship_strength=pygame.transform.scale(buff_ship_strength,(80,80))
scaled_buff_ship_firerate=pygame.transform.scale(buff_ship_firerate,(80,80))
scaled_buff_ship_speed=pygame.transform.scale(buff_ship_speed,(80,80))
scaled_money_buff=pygame.transform.scale(money_buff,(100,100))
scaled_passive_money=pygame.transform.scale(passive_money,(100,100))
scaled_more_healing=pygame.transform.scale(more_healing,(100,100))
scaled_healing_range=pygame.transform.scale(healing_range,(100,100))
scaled_more_damage=pygame.transform.scale(more_damage,(100,100))
scaled_projectile_speed=pygame.transform.scale(projectile_speed,(100,100))
scaled_damage_taken=pygame.transform.scale(damage_taken,(100,100))
scaled_charge_bonus=pygame.transform.scale(charge_bonus,(100,100))
scaled_mechanic_boss=pygame.transform.scale(mechanic_boss,(300,120))
scaled_teleport_boss=pygame.transform.scale(teleport_boss,(300,120))
scaled_explosion_boss=pygame.transform.scale(explosion_boss,(300,120))
scaled_explosion_boss_bullet=pygame.transform.scale(explosion_boss_bullet,(60,60))

# Fonts
header_font=pygame.font.Font('Pixel Digivolve.otf', 70)
achievement_font=pygame.font.Font('Pixel Digivolve.otf',40)
main_font=pygame.font.Font('Pixel Digivolve.otf', 18)
small_header_font=pygame.font.Font('Pixel Digivolve.otf', 24)
typing_font = pygame.font.Font('Pixel Digivolve.otf',32)

# Colours
color_passive = (0,0,0)
color_active = (200,200,200)
color = color_passive
Name_rect = pygame.Rect(182,570,297,35) #not a color but it fits with the stuff above for the name input

# Headers

maintext=header_font.render("Choose your reptile",1,(0,0,0))
abilityheader = small_header_font.render("Ability:", 1, (0, 0, 0))
achievementheader = header_font.render("Achievements",1,(125,255,255))
achievementsubheader = small_header_font.render("Seriously, how much time have you spent on this game?",1,(125,255,255))
etext=small_header_font.render("E",1,(250,250,250))
shopheader=header_font.render("Shop",1,(0,0,0))
# Text
boss1name=small_header_font.render("Crankz the Mechanic", 1, (250,250,250))
boss2name=small_header_font.render("Charles the Strategist", 1, (250,250,250))
boss3name=small_header_font.render("Boom the Explosiont", 1, (250,250,250))
boss4name=small_header_font.render("Baq the Supreme Leader", 1, (250,250,250))

secretselectedtext=main_font.render("Please select an available character.",1,(0,0,0))

shieldabilitytext=main_font.render("For x seconds, the shield enlarges,",1,(0,0,0))
shieldabilitytext2 = main_font.render("spanning the entire screen and effectively",1, (0, 0, 0))
shieldabilitytext3=main_font.render("rendering enemy attacks useless.",1, (0, 0, 0))
shieldloretext1=main_font.render("The Shieldbearers, the protectors of the",1,(0,0,0))
shieldloretext2=main_font.render("Khvlik’i. Since the ancient times in which they",1,(0,0,0))
shieldloretext3=main_font.render("were named, their philosophy believes in",1,(0,0,0))
shieldloretext4=main_font.render("preserving peace by stopping conflict and",1,(0,0,0))
shieldloretext5=main_font.render("disaster before it affects anyone.",1,(0,0,0))
shieldloretext6=main_font.render("",1,(0,0,0))
# The Shieldbearers, the protectors of the Khvlik’i. Since the ancient times in which they were named, their philosophy believes in preserving peace by stopping conflict and disaster before it affects anyone.

healabilitytext = main_font.render("Instantly restores a set amount", 1,(0, 0, 0))
healabilitytext2=main_font.render("of health to all friendly buildings.",1,(0,0,0))
healabilitytext3=main_font.render("",1,(0,0,0))
healloretext1=main_font.render("The Menders, a beacon of hope for the ill and",1,(0,0,0))
healloretext2=main_font.render("injured. Rooted in the ritualistic practices of",1,(0,0,0))
healloretext3=main_font.render("their predecessors, their methods often employ",1,(0,0,0))
healloretext4=main_font.render("herbal medication and meditation. They aim to",1,(0,0,0))
healloretext5=main_font.render("keep peace by healing the wounds and dispelling",1,(0,0,0))
healloretext6=main_font.render("the grudges caused by conflict.",1,(0,0,0))
# The Menders, a beacon of hope for the ill and injured. Rooted in the ritualistic practices of their predecessors, their methods often employ herbal medication and meditation. They aim to keep peace by healing the wounds and dispelling the grudges caused by conflict


moneyabilitytext=main_font.render("For x seconds boosts the production,",1, (0, 0, 0))
moneyabilitytext2=main_font.render("heal or attack speed of all generation, heal",1,(0,0,0))
moneyabilitytext3=main_font.render("or damage ally buildings.",1,(0,0,0))
moneyloretext1=main_font.render("The Merchant Association, the driving force",1,(0,0,0))
moneyloretext2=main_font.render("behind the Khvlik’i economy. Unlike their fellow",1,(0,0,0))
moneyloretext3=main_font.render("factions of the council, the Merchant Association ",1,(0,0,0))
moneyloretext4=main_font.render("formed sometime after the industrial era, aiming",1,(0,0,0))
moneyloretext5=main_font.render("to help maintain peace by improving the citizens'",1,(0,0,0))
moneyloretext6=main_font.render("living standards with commerce.",1,(0,0,0))


# The Merchant Association, the driving force behind the Khvlik’i economy. Unlike their fellow factions of the council, the Merchant Association formed sometime after the industrial era, aiming to help maintain peace by improving the citizens' living standards with commerce.

attackabilitytext=main_font.render("Releases 20% of built up charge to",1,(0,0,0))
attackabilitytext2=main_font.render("unleash a devastating attack on the enemies.",1,(0,0,0))
attackabilitytext3=main_font.render("",1,(0,0,0))
attackloretext1=main_font.render("General Mk’vleli II was a member of the",1,(0,0,0))
attackloretext2=main_font.render("shieldbearers before his supposed death.",1,(0,0,0))
attackloretext3=main_font.render("He was always more agressive than his peers,",1,(0,0,0))
attackloretext4=main_font.render("though no one had suspected he was working on ",1,(0,0,0))
attackloretext5=main_font.render("a taboo shield with offensive capabilities.",1,(0,0,0))
attackloretext6=main_font.render("",1,(0,0,0))
# General Mk’vleli II was a member of the shieldbearers before his supposed death. He was always more agressive than his peers, though no one had suspected he was working on a taboo shield with offensive capabilities.

secretabilitytext=small_header_font.render("Secret",1,(0,0,0))
secretloretext= header_font.render("Secret",1,(0,0,0))

achievementtext1false=achievement_font.render("???",1,(125,255,255))
achievementtext1true=achievement_font.render("Wow! You beat the game!",1,(125,255,255))
achievementsubtext1=small_header_font.render("(Beat the game)",1,(125,255,255))
achievementtext2false=achievement_font.render("???",1,(125,255,255))
achievementtext2true=achievement_font.render("Guess you just had to try out the General, huh?",1,(125,255,255))
achievementsubtext2=small_header_font.render("(Beat the game with the General character)",1,(125,255,255))
achievementtext3false=achievement_font.render("???",1,(125,255,255))
achievementtext3true=achievement_font.render("A flawless run, eh? Pretty impressive!",1,(125,255,255))
achievementsubtext3=small_header_font.render("(Beat the game without incurring any losses)",1,(125,255,255))


# heronumbers so anything that has something to do with player character
shield_hero= [shieldabilitytext,shieldabilitytext2,shieldabilitytext3,scaled_shield_man,scaled_shield_shield,scaled_shield_icon,shieldloretext1,shieldloretext2,shieldloretext3,shieldloretext4,shieldloretext5,shieldloretext6]
heal_hero= [healabilitytext,healabilitytext2,healabilitytext3,scaled_heal_man,scaled_heal_shield,scaled_heal_icon,healloretext1,healloretext2,healloretext3,healloretext4,healloretext5,healloretext6]
money_hero= [moneyabilitytext,moneyabilitytext2,moneyabilitytext3,scaled_money_man,scaled_money_shield,scaled_money_icon,moneyloretext1,moneyloretext2,moneyloretext3,moneyloretext4,moneyloretext5,moneyloretext6]
attack_hero= [attackabilitytext,attackabilitytext2,attackabilitytext3,scaled_mean_man,scaled_mean_shield,scaled_attack_icon,attackloretext1,attackloretext2,attackloretext3,attackloretext4,attackloretext5,attackloretext6]
heroes=[shield_hero,heal_hero,money_hero,attack_hero]
charscreencoords=[(600,350),(500,370),(500,390),(150, 220),(500, 253),(670,214),(500,430),(500,450),(500,470),(500,490),(500,510),(500,530)]
characterpictures=[main_scaled_shield_man,main_scaled_heal_man,main_scaled_money_man,main_scaled_mean_man]
abilitypictures=[scaled_shield_icon,scaled_heal_icon,scaled_money_icon,scaled_attack_icon]
charcutscenepics=[rescaled_shield_lizard,rescaled_heal_lizard,rescaled_money_lizard,rescaled_mean_lizard]

# buttons
startbutton = button((125,255,255),520,500,150,30,"New Game")
continuebutton  = button((125,255,255),520,500,150,30,"New Game")
achievementbutton = button((125,255,255),515,600,160,30,"Achievements")
quitbutton = button((125,255,255),520,700,150,30,"Quit")
mainmenubuttons=[startbutton,continuebutton,achievementbutton,quitbutton]


charselectbutton = button((255,255,255),1000,400,100,30,"Next")
backbutton= button((255,255,255),50,720,200,30,"Back to Menu")
finishbutton = button((255,255,255),950,720,200,30,"Finish")

cancelbutton=button((255,255,255),20,530,30,30,"X")
deletebutton=button((255,255,255),70,530,160,30,"Delete")
attackbutton=button((255,255,255),20,440,300,80,"Attack Building  50G") # For purchasing attack buildings
healbutton=button((255,255,255),20,350,300,80,"Heal Building  50G") # For purchasing healing buildings
genbutton=button((255,255,255),20,260,300,80,"Business Building  40G") # For purchasing generation buildings
buildingbuttons=[cancelbutton,deletebutton,attackbutton,healbutton,genbutton]

shopcontinuebutton=button((255,255,255),1000,400,150,30,"Continue")

#Cutscene Text

c1t11=main_font.render("The year is 3576 on the homeworld of the Khvlik'i,",1,(0,0,0))
c1t12=main_font.render("a peace loving reptilian race which helps maintain",1,(0,0,0))
c1t13=main_font.render("friendly relations between the space-faring empires of their sector.",1,(0,0,0))
c1t2=main_font.render("Today a festival is being held in honor of a hero, Baq.",1,(0,0,0))
c1t31=main_font.render("General Baq was a shield-bearer who valiantly gave his life",1,(0,0,0))
c1t32=main_font.render("to stop a planet-wiping weapon in the final war of their sector,",1,(0,0,0))
c1t33=main_font.render("buying the time needed to secure a peace treaty.",1,(0,0,0))
c1t41=main_font.render("However,",1,(0,0,0))
c1t42=main_font.render("as the faction representatives of the Khvlik'i finish their speech",1,(0,0,0))
c1t43=main_font.render("and head inside to enjoy the festivities,",1,(0,0,0))
c1t44=main_font.render("an unknown danger approaches.",1,(0,0,0))

c1t1=[c1t11,c1t12,c1t13]
c1t3=[c1t31,c1t32,c1t33]
c1t4=[c1t41,c1t42,c1t43,c1t44]

c2t1=text(scaled_baselizard,"Alert, an emergency meeting of the leaders has been called,","ally","Lizard General")
c2t2=text(scaled_baselizard,"please report to the meeting chamber as soon as possible.","ally","Lizard General")
c2t3=text(None,"We had an emergency just last week! What could it possibly ","ally","")
c2t38=text(None,"be this time? ","ally","")
c2t4=text(scaled_baselizard,"You're late, there's no time to dawdle. ","ally","Lizard General")
c2t37=text(scaled_baselizard,"Our whole empire might be in danger.","ally","Lizard General")
c2t5=text(None,"Is it a natural disaster?","ally","")
c2t6=text(None,"We've been stockpiling emergency rations since the war ended,","ally","")
c2t39=text(None,"shouldn't our people be safe?","ally","")
c2t7=text(scaled_baselizard,"No, our scouts have detected a heavily armed fleet","ally","Lizard General")
c2t40=text(scaled_baselizard,"traveling through our territory.","ally","Lizard General")
c2t8=text(None,"What empire does it belong to?","ally","")
c2t9=text(None,"We finished the last of the peace talks months ago,","ally","")
c2t10=text(None,"there should be no open hostility happening within our borders.","ally","")
c2t11=text(scaled_baselizard,"The flags and insignia on their ships are not known to us,","ally","Lizard General")
c2t12=text(scaled_baselizard,"we believe we are dealing with a new race","ally","Lizard General")
c2t41=text(scaled_baselizard,"who comes from another sector.","ally","Lizard General")
c2t13=text(None,"Very well then, we should attempt first contact.","ally","")
c2t14=text(None,"Perhaps they can be reasoned with.","ally","")
c2t15=text(None,"Comms department!","ally","")
c2t42=text(None,"Establish a link with the leading ship of their fleet!","ally","")
c2t16=text(scaled_baselizard,"On it!","ally","Comms Guy")
c2t43=text(scaled_baselizard,"We are putting you through to the command room of the main ship.","ally","Comms Guy")
c2t17=text(scaled_finalboss,"This is Supreme Leader Adam of the Adamian Empire,","enemy","Supreme Leader")
c2t44=text(scaled_finalboss,"state your name and reason for contact.","enemy","Supreme Leader")
c2t18=text(scaled_baselizard,"Greetings Supreme Leader, this is the High General of the Khvlik'i.","ally","")
c2t19=text(None,"Your fleet is passing through our part of this sector,","ally","")
c2t20=text(None,"we seek to learn your intentions in","ally","")
c2t45=text(None,"traveling through our territory.","ally","")
c2t21=text(scaled_finalboss,"We have come to widen the borders the Great Adamian Empire,","enemy","Adam")
c2t22=text(scaled_finalboss,"i demand a portion of this sector's territory.","enemy","Adam")
c2t23=text(scaled_finalboss,"If it is not given, we shall take it by force.","enemy","Adam")
c2t24=text(None,"Calm yourself Supreme Leader, there is no need for bloodshed.","ally","")
c2t25=text(None,"We cannot give up our land,","ally","")
c2t26=text(None,"but I'm sure our empires could mutually benefit","ally","")
c2t46=text(None,"through trade and cultural exchange.","ally","")
c2t27=text(scaled_finalboss,"Our leaders have no need of your trade vermin.","enemy","Adam")
c2t28=text(scaled_finalboss,"The wealth in the lands we will take","enemy","Adam")
c2t47=text(scaled_finalboss,"is already ours in the first place.","enemy","Adam")
c2t29=text(scaled_finalboss,"Since you do not wish to give up willingly,","enemy","Adam")
c2t48=text(scaled_finalboss,"we will take what we need by force.","enemy","Adam")
c2t30=text(scaled_finalboss,"Cut communications with these worthless lizards!","enemy","Adam")
c2t49=text(scaled_finalboss,"And prepare the men for attack!","enemy","Adam")
c2t31=text(scaled_baselizard,"What a crude race, They must've achieved","ally","Lizard General")
c2t50=text(scaled_baselizard,"space-faring technology very recently.","ally","Lizard General")
c2t32=text(None,"Their history is the least of our concerns right now,","ally","")
c2t33=text(None,"you must start evacuating the people.","ally","")
c2t34=text(None,"I will try to get at least my A.E.G.I.S. in working order","ally","")
c2t35=text(scaled_baselizard,"Very well, you shall lead our armies","ally","Lizard General")
c2t36=text(scaled_baselizard,"The rest of us will hide the civillians","ally","Lizard General")
c2t51=text(scaled_baselizard,"and help provide resources for battle.","ally","Lizard General")
c2t52=text(scaled_baselizard,"","ally","Lizard General")
c2t=[c2t1,c2t2,c2t3,c2t38,c2t4,c2t37,c2t5,c2t6,c2t39,c2t7,c2t40,c2t8,c2t9,c2t10,c2t11,c2t12,c2t41,c2t13,c2t14,c2t15,c2t42,c2t16,c2t43,c2t17,c2t44,c2t18,c2t19,c2t20,c2t45,c2t22,c2t23,c2t24,c2t25,c2t26,c2t46,c2t27,c2t28,c2t47,c2t29,c2t48,c2t30,c2t49,c2t31,c2t50,c2t32,c2t33,c2t34,c2t35,c2t36,c2t51,c2t52]

c3t0=main_font.render("Two days Later",1,(0,0,0))
c3t1=text(None,"My A.E.G.I.S. is up and running.","ally","")
c3t2=text(None,"We are ready to begin defending.","ally","")
c3t3=text(None,"Their fleet should arrive soon.","ally","")
c3t4=text(scaled_baselizard,"We are receiving a transmission from the enemy sir!","ally","Worker")
c3t5=text(scaled_finalboss,"Our fleet is in position, you have one last chance to surrender","enemy","Adam")
c3t6=text(scaled_finalboss,"before we blow you to bits.","enemy","Adam")
c3t7=text(None,"The Khvlik'i have stood worse, we will not fall here","ally","")
c3t8=text(scaled_baselizard,"","ally","Lizard General")

c3t=[c3t1,c3t2,c3t3,c3t4,c3t5,c3t6,c3t7,c3t8]

c4t1=text(None,"Your weapons are no match for our A.E.G.I.S.,","ally","")
c4t2=text(None,"turn back now, so that we may end this foolish conflict.","ally","")
c4t3=text(scaled_finalboss,"You think we will retreat because you beat some grunts?","enemy","Adam")
c4t4=text(scaled_finalboss,"Your city cannot withstand the might of the Empire forever.","enemy","Adam")
c4t5=text(scaled_baselizard,"","ally","Lizard General")
c4t=[c4t1,c4t2,c4t3,c4t4,c4t5]

c5t1=text(scaled_mechanicboss,"You think your little shield is strong?","enemy","Mechanic")
c5t2=text(scaled_mechanicboss,"I could make a better ship out of the spare parts from my oven!","enemy","Mechanic")
c5t3=text(None,"A.E.G.I.S. does not need brute force, it is an impenetrable shield","ally","")
c5t4=text(None,"that will protect the Khvlik'i until our final days.","ally","")
c5t5=text(scaled_mechanicboss,"Too bad those final days have arrived then, isn't it?","enemy","Mechanic")
c5t6=text(scaled_baselizard,"","ally","Lizard General")

c5t=[c5t1,c5t2,c5t3,c5t4,c5t5,c5t6]

c6t1=text(scaled_mechanicboss,"Damn it!","enemy","Mechanic")
c6t2=text(scaled_mechanicboss,"The shields are failing and the cannon won't last much longer!","enemy","Mechanic")
c6t3=text(scaled_mechanicboss,"we need more emergency repairs!","enemy","Mechanic")
c6t4=text(scaled_mechanicboss,"WAIT, WHERE DID THE COOLING SYSTEM GET BLOWN OFF TO?!?!","enemy","Mechanic")
c6t5=text(None,"I pray he may rest in the afterlife.","ally","")
c6t6=text(None,"Please leave our homeworld be","ally","")
c6t10=text(None,"before any of us incur more needless casualties.","ally","")
c6t7=text(scaled_finalboss,"Don't assume that grease monkey was the best my army offers.","enemy","Adam")
c6t8=text(scaled_finalboss,"We will blow through your defenses lizard !","enemy","Adam")
c6t9=text(scaled_baselizard,"","ally","Lizard General")

c6t=[c6t1,c6t2,c6t3,c6t4,c6t5,c6t6,c6t10,c6t7,c6t8,c6t9]


c7t1=text(scaled_tpboss,"Blasted machine!","enemy","Strategist")
c7t2=text(scaled_tpboss,"Our troops should have been","enemy","Strategist")
c7t9=text(scaled_tpboss,"transported behind enemy lines hours ago!","enemy","Strategist")
c7t3=text(scaled_tpboss,"Why is the transporter not working?!","enemy","Strategist")
c7t4=text(None,"A.E.G.I.S. is not the only form of defensive technology we have","ally","")
c7t5=text(None,"no one would be foolish enough to wage war","ally","")
c7t10=text(None,"without a transport disruptor.","ally","")
c7t6=text(scaled_tpboss,"This changes nothing!","enemy","Strategist")
c7t7=text(scaled_tpboss,"If you think that's the only trick up my sleeve","enemy","Strategist")
c7t11=text(scaled_tpboss,"you're up for a rude awakening!","enemy","Strategist")
c7t8=text(scaled_baselizard,"","ally","Lizard General")

c7t=[c7t1,c7t2,c7t9,c7t3,c7t4,c7t5,c7t10,c7t6,c7t7,c7t11,c7t8]

c8t1=text(scaled_tpboss,"The transporter is malfunctioning!","enemy","Strategist")
c8t2=text(scaled_tpboss,"If we don't retreat now we will be sent to a void with no return!","enemy","Strategist")
c8t3=text(scaled_finalboss,"Then drag your enemy in there with you!","enemy","Adam")
c8t4=text(scaled_finalboss,"A soldier of the Adamian Empire never retreats!","enemy","Adam")
c8t5=text(scaled_tpboss,"That's not how this works sir!","enemy","Strategist")
c8t6=text(scaled_tpboss,"Please, we don't have much ti-","enemy","Strategist")
c8t7=text(scaled_finalboss,"Hmph, what a waste, they did not take a single lizard with them.","enemy","Adam")
c8t8=text(None,"Have you no shame?!","ally","")
c8t9=text(None,"How could you just leave them to their fates?!","ally","")
c8t10=text(scaled_finalboss,"Do not speak to me of shame, lizard!","enemy","Adam")
c8t11=text(scaled_finalboss,"I know you would sacrifice lives of your own accord too.","enemy","Adam")
c8t12=text(scaled_baselizard,"","ally","Lizard General")

c8t=[c8t1,c8t2,c8t3,c8t4,c8t5,c8t6,c8t7,c8t8,c8t9,c8t10,c8t11,c8t12]

c9t1=text(scaled_bomberman,"So you think your fancy shield can save you?","enemy","Explosives Expert")
c9t2=text(scaled_bomberman,"Let's see how well it handles-","enemy","Explosives Expert")
c9t3=text(None,"Watch yourself, fool!","ally","")
c9t4=text(None,"One wrong step and you'll blow yourself to bits!","ally","")
c9t5=text(scaled_bomberman,"That's exactly what makes this job so damn fun!","enemy","Explosives Expert")
c9t6=text(scaled_baselizard,"","ally","Lizard General")

c9t=[c9t1,c9t2,c9t3,c9t4,c9t5,c9t6]

c10t1=text(scaled_bomberman,"The main ammo storage caught fire!","enemy","Explosives Expert")
c10t2=text(scaled_bomberman,"This will be a good one! HAHAHAH!","enemy","Explosives Expert")
c10t3=text(scaled_finalboss,"Is every person in this fleet a damn idiot?!","enemy","Adam")
c10t4=text(scaled_finalboss,"FINE! I will do this myself.","enemy","Adam")
c10t5=text(None,"Finally, the end of the war approaches.","ally","")
c10t6=text(scaled_baselizard,"","ally","Lizard General")

c10t=[c10t1,c10t2,c10t3,c10t4,c10t5,c10t6]

c11t1=text(None,"WAIT, is that... an A.E.G.I.S.?!","ally","")
c11t2=text(scaled_finalboss,"Correction, it's BETTER than an A.E.G.I.S.!","enemy","Adam")
c11t3=text(scaled_finalboss,"I have waited too long to use this for my revenge!","enemy","Adam")
c11t4=text(rescaled_mean_lizard,"I have waited too long to use this for my revenge!","enemy","'Adam'")
c11t5=text(None,"BAQ?!? We thought you were dead!","ally","")
c11t6=text(rescaled_mean_lizard,"How could you think anything else?","enemy","Baq")
c11t7=text(rescaled_mean_lizard,"after you left me to face death all on my own?!","enemy","Baq")
c11t8=text(None,"Baq wait! I'm sure we can resolve this peacefully!","ally","")
c11t9=text(rescaled_mean_lizard,"All you ever talk about is peace!","enemy","Baq")
c11t10=text(rescaled_mean_lizard,"It is for your petty peace that I almost died that day!","enemy","Baq")
c11t11=text(rescaled_mean_lizard,"Now shut your mouth and fight me, puny General!","enemy","Baq")
c11t12=text(scaled_baselizard,"","ally","Lizard General")

c11t=[c11t1,c11t2,c11t3,c11t4,c11t5,c11t6,c11t7,c11t8,c11t9,c11t10,c11t11,c11t12]

c12t1=text(rescaled_mean_lizard,"It can't be!","enemy","Baq")
c12t2=text(rescaled_mean_lizard,"My A.E.G.I.S. was perfect! How could I lose?!","enemy","Baq")
c12t3=text(None,"In your futile pursuit of physical power,","ally","")
c12t4=text(None,"you forgot true power comes from those you protect.","ally","")
c12t5=text(None,"Now, I pray you may finally rest,","ally","")
c12t6=text(None,"so we may put this conflict behind us.","ally","")
c12t7=text(rescaled_mean_lizard,"NOOO!! I REFUSE TO ACCEPT THIS!!","enemy","Baq")
c12t8=text(scaled_baselizard,"","ally","Lizard General")

c12t=[c12t1,c12t2,c12t3,c12t4,c12t5,c12t6,c12t7,c12t8]

c13t1=main_font.render("With Supreme Leader Adam gone,",1,(0,0,0))
c13t2=main_font.render("the Khvlik'i managed to form an alliance with humanity.",1,(0,0,0))
c13t3=main_font.render("Peace has returned to the world",1,(0,0,0))

c13t=[c13t1,c13t2,c13t3]
