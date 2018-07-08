from flask import Flask, request, render_template, redirect, url_for
import random
import sys
import os
import math

test = []
list1 = []
app = Flask(__name__)
counter = 0
compare = 0
intercept = -7.248873208
calculatedvalue = 0
counter1 = 0

array2 = []
for i in range(0,224):
    array2.append(0)

dictionary= {'Anti-Mage':0,
'Axe':1,
'Bane':2,
'Bloodseeker':3,
'Crystal Maiden':4,
'Drow Ranger':5,
'Earthshaker':6,
'Juggernaut':7,
'Mirana':8,
'Morphling':9,
'Shadow Fiend':10,
'Phantom Lancer':11,
'Puck':12,
'Pudge':13,
'Razor':14,
'Sand King':15,
'Storm Spirit':16,
'Sven':17,
'Tiny':18,
'Vengeful Spirit':19,
'Windranger':20,
'Zeus':21,
'Kunkka':22,
#'Arc Warden':24,
'Lina':24,
'Lion':25,
'Shadow Shaman':26,
'Slardar':27,
'Tidehunter':28,
'Witch Doctor':29,
'Lich':30,
'Riki':31,
'Enigma':32,
'Tinker':33,
'Sniper':34,
'Necrophos':35,
'Warlock':36,
'Beastmaster':37,
'Queen of Pain':38,
'Venomancer':39,
'Faceless Void':40,
'Wraith King':41,
'Death Prophet':42,
'Phantom Assassin':43,
'Pugna':44,
'Templar Assassin':45,
'Viper':46,
'Luna':47,
'Dragon Knight':48,
'Dazzle':49,
'Clockwerk':50,
'Leshrac':51,
'Natures Prophet':52,
'Lifestealer':53,
'Dark Seer':54,
'Clinkz':55,
'Omniknight':56,
'Enchantress':57,
'Huskar':58,
'Night Stalker':59,
'Broodmother':60,
'Bounty Hunter':61,
'Weaver':62,
'Jakiro':63,
'Batrider':64,
'Chen':65,
'Spectre':66,
'Ancient Apparition':67,
'Doom':68,
'Ursa':69,
'Spirit Breaker':70,
'Gyrocopter':71,
'Alchemist':72,
'Invoker':73,
'Silencer':74,
'Outworld Devourer':75,
'Lycan':76,
'Brewmaster':77,
'Shadow Demon':78,
'Lone Druid':79,
'Chaos Knight':80,
'Meepo':81,
'Treant Protector':82,
'Ogre Magi':83,
'Undying':84,
'Rubick':85,
'Disruptor':86,
'Nyx Assassin':87,
'Naga Siren':88,
'Keeper of the Light':89,
'Io':90,
'Visage':91,
'Slark':92,
'Medusa':93,
'Troll Warlord':94,
'Centaur Warrunner':95,
'Magnus':96,
'Timbersaw':97,
'Bristleback':98,
'Tusk':99,
'Skywrath Mage':100,
'Abaddon':101,
'Elder Titan':102,
'Legion Commander':103,
'Techies':104,
'Ember Spirit':105,
'Earth Spirit':106,
'Underlord':107,
'Terrorblade':108,
'Phoenix':109,
'Oracle':110,
'Winter Wyvern':111}

heroes = ['Anti-Mage',
'Axe',
'Bane',
'Bloodseeker',
'Crystal Maiden',
'Drow Ranger',
'Earthshaker',
'Juggernaut',
'Mirana',
'Morphling',
'Shadow Fiend',
'Phantom Lancer',
'Puck',
'Pudge',
'Razor',
'Sand King',
'Storm Spirit',
'Sven',
'Tiny',
'Vengeful Spirit',
'Windranger',
'Zeus',
'Kunkka',
#'Arc Warden':24,
'Lina',
'Lion',
'Shadow Shaman',
'Slardar',
'Tidehunter',
'Witch Doctor',
'Lich',
'Riki',
'Enigma',
'Tinker',
'Sniper',
'Necrophos',
'Warlock',
'Beastmaster',
'Queen of Pain',
'Venomancer',
'Faceless Void',
'Wraith King',
'Death Prophet',
'Phantom Assassin',
'Pugna',
'Templar Assassin',
'Viper',
'Luna',
'Dragon Knight',
'Dazzle',
'Clockwerk',
'Leshrac',
'Natures Prophet',
'Lifestealer',
'Dark Seer',
'Clinkz',
'Omniknight',
'Enchantress',
'Huskar',
'Night Stalker',
'Broodmother',
'Bounty Hunter',
'Weaver',
'Jakiro',
'Batrider',
'Chen',
'Spectre',
'Ancient Apparition',
'Doom',
'Ursa',
'Spirit Breaker',
'Gyrocopter',
'Alchemist',
'Invoker',
'Silencer',
'Outworld Devourer',
'Lycan',
'Brewmaster',
'Shadow Demon',
'Lone Druid',
'Chaos Knight',
'Meepo',
'Treant Protector',
'Ogre Magi',
'Undying',
'Rubick',
'Disruptor',
'Nyx Assassin',
'Naga Siren',
'Keeper of the Light',
'Io',
'Visage',
'Slark',
'Medusa',
'Troll Warlord',
'Centaur Warrunner',
'Magnus',
'Timbersaw',
'Bristleback',
'Tusk',
'Skywrath Mage',
'Abaddon',
'Elder Titan',
'Legion Commander',
'Techies',
'Ember Spirit',
'Earth Spirit',
'Underlord',
'Terrorblade',
'Phoenix',
'Oracle',
'Winter Wyvern']

coefmatrix = (1.23454395303285 ,  1.16182142473777 ,  1.2703225022877 ,   1.14627211229078 ,  1.60140683835123 ,  1.35020949419738 ,  1.42994193650351 
    ,  1.38764351927468 ,  1.48337191929531 ,  1.01975753492294 ,  1.31589145156114 ,  1.23332317458786 ,  0.933560893405223 , 1.35985657204192 
    ,  1.26144851933923 ,  1.30359928443253 ,  0.879909075638846 , 1.44741265472389 ,  1.30621201816178 ,  1.50766206060722 ,  1.24443233757443 
    ,  1.58449227893762 ,  1.2567821842343 ,   0 , 1.0646682980741 ,   1.31707743432279 ,  1.58359795901165 ,  1.62027310041561 ,  1.33431000068961 
    ,  1.46784718909303 ,  1.64025436952536 ,  1.6733468274447 ,   1.33258143728099 ,  1.01322983200102 ,  1.07232524083444 ,  1.69017264727538 
    ,  1.63097336321114 ,  1.38722666453237 ,  1.1150589544279 ,   1.46229362420192 ,  1.12729877551744 ,  1.67982265817497 ,  1.34532170863488 
    ,  1.2121591346664 ,   1.24366455421886 ,  1.34625366422953 ,  1.33519808738595 ,  1.50976890499098 ,  1.36929486828462 ,  1.53582090448921 
    ,  1.33764189363163 ,  1.19342710491093 ,  0.947409034809793 , 1.22270552217879 ,  1.390430431145 ,    1.29875416961237 ,  1.82132292549979 
    ,  1.03193242479797 ,  1.17237778081953 ,  1.48452575567122 ,  0.951318073178483 , 1.43544249642843 ,  1.2371037904689 ,   1.44019078275556 
    ,  1.13811636961102 ,  1.31344069478402 ,  1.72880424040759 ,  1.46978095761508 ,  1.5449710092793 ,   1.6132353874073 ,   1.54486399153952 
    ,  1.30526693971516 ,  1.39906988586347 ,  1.25910274219761 ,  1.54136330508932 ,  1.15712994323718 ,  1.35527547187674 ,  1.32982130030252 
    ,  0.992779983461705 , 0.958090309287318 , 1.38247369733918 ,  1.10548559482569 ,  1.50886456641502 ,  1.53836383210442 ,  1.70119626624154 
    ,  1.24588248063528 ,  1.51508070818495 ,  1.31223821268185 ,  1.13520746973913 ,  1.23327570054309 ,  1.24642371783198 ,  1.4245019900164 
    ,   1.28947950636753 ,  1.40915676828533 ,  1.29364113006649 ,  1.46450595014547 ,  1.15544343537953 ,  1.20275807640301 ,  1.26252947302184 
    ,  1.46721043221923 ,  1.12510668977442 ,  1.75824419882627 ,  1.36102647152053 ,  1.34362366228017 ,  1.2113140377886 ,   1.27019542715577 
    ,  1.44679865642176 ,  0 , 1.42852977323597 ,  1.48301766175982 ,  1.31643013256682 ,  1.45768151969721 ,  0.235397644528861 , 0.331729615057013 
    , 0.162588130108987 , 0.29888470774359 ,  -0.0648128771958832 ,   -0.000767758683272263 , 0.0239122696693534 ,    -0.0222428235268095 
    ,   -0.00545022145009522 ,  0.35049270121034 ,  0.133034739876247 , 0.314007849640513 , 0.452206812920442 , 0.138044658065818 , 0.289646403425705 
    , 0.156819045088344 , 0.48794491364668 ,  0.0529994378099652 ,    0.219458145612298 , -0.0943197412040337 ,   0.234527993405337 , -0.0388343612384171 
    ,   0.322510009966649 , 0 , 0.43836753219312 ,  0.183643551518555 , 0.0216037620688482 ,    -0.19825709736085 , 0.0361456095354126 ,    0.0106391046339932 
    ,    -0.196832471082076 ,    -0.122829696536552 ,    0.0497793350754742 ,    0.36065263722863 ,  0.383759257535162 , -0.150151532069239 ,    -0.0391550107273752 
    ,   -0.135030236091936 ,    0.42096700420119 ,  -0.0590855702309353 ,   0.319970324828321 , -0.238461262296262 ,    0.15792493507902 ,  0.234937528514651 
    , 0.0851743998111874 ,    0.20420431172757 ,  0.102208632610755 , 0.112690245663498 , 0.130856373027173 , -0.074437216822003 ,    0.0552225018813691 
    ,    0.268163626009629 , 0.420130156482559 , 0.260372636167979 , -0.0370425949568814 ,   0.228791276325226 , -0.366451227505184 ,    0.477482409721693 
    , 0.0775322798303618 ,    0.0165732802114812 ,    0.358286426616556 , 0.0538684712900154 ,    0.278986692353062 , 0.00295071207566925 ,   0.323977607627623
    , 0.181650198076148 , -0.207229539429467 ,    0.0571492235226357 ,    -0.0895667628668503 ,   -0.261869982208006 ,    -0.128947567735263 ,    0.0838736140317823 
    ,    0.0387671472860309 ,    0.18150038849395 ,  0.00417225957345187 ,   0.290509486133934 , -0.0530295729053097 ,   0.0974392382651124 ,    0.37815715987679 
    ,  0.215124373280029 , 0.0725059230641893 ,    0.141624179182744 , -0.0584956222475652 ,   0.00824835163194758 ,   -0.193186978061132 ,    0.232155546422942 
    , -0.062797173049113 ,    0.154669048856521 , 0.24559932483257 ,  0.0652780779978316 ,    0.266720475297926 , 0.130608864021112 , 0.109355607056511 , 0.0136239922149848 
    ,    0.191245972549135 , -0.0205700842302285 ,   0.328584756307223 , 0.322927942557564 , 0.151548128946827 , 0.0580838712853496 ,    0.296616494699377 , -0.218168996434478 
    ,    -0.0912329206697045 ,   0.226653747637939 , 0.221771624639237 , 0.283566971374919 , -0.0650148436094005 ,   0 , 0.0317403174958671 ,    -0.0365357517055045 ,   0.164242603682135 , 0)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():

    for i in range(0,224):
        array2[i] = 0
    global counter1
    counter1 = counter1 + 1

    global counter
    global compare
    if counter > compare:
        i = 0
        while i < 10:
            del test[0]
            i += 1

    counter = counter + 1

    test.append(request.form['Player1'])
    test.append(request.form['Player2'])
    test.append(request.form['Player3'])
    test.append(request.form['Player4'])
    test.append(request.form['Player5'])
    test.append(request.form['Player6'])
    test.append(request.form['Player7'])
    test.append(request.form['Player8'])
    test.append(request.form['Player9'])
    test.append(request.form['Player10'])

    #processed_text = text
    #text = 'dog'
    notFound = 0
    i = 0
    while i < 10:
        if test[i] in heroes:
            i = i + 1
        else:
            notFound = 1
            break

    duplicate = 0
    i = 0
    while i < 9:
        c = i + 1
        while c < 9 : 
            if test[i] == test[c]:
                duplicate = 1
            c += 1
        i += 1

    i = 0
    error = 0
    while i < 10:
        if test[i] == '':
            error = 1
        i += 1

    if duplicate == 1:
        return redirect(url_for("Error"))
    elif error == 1:
        return redirect(url_for("Error"))
    elif notFound == 1:
        return redirect(url_for("Error"))        
    else:
        return redirect(url_for("hello"))


@app.route('/Result', methods=['GET'])
def hello():

    global test

    index = dictionary.get(test[0]) 
    array2[index] = 1

    index = dictionary.get(test[1]) 
    array2[index] = 1

    index = dictionary.get(test[2]) 
    array2[index] = 1

    index = dictionary.get(test[3]) 
    array2[index] = 1

    index = dictionary.get(test[4]) 
    array2[index] = 1

    index = dictionary.get(test[5]) 
    array2[index+112] = 1

    index = dictionary.get(test[6]) 
    array2[index+112] = 1

    index = dictionary.get(test[7]) 
    array2[index+112] = 1

    index = dictionary.get(test[8]) 
    array2[index+112] = 1

    index = dictionary.get(test[9]) 
    array2[index+112] = 1

    global calculatedvalue
    calculatedvalue = 0
    global intercept
    for i in range(0,224):
        calculatedvalue = calculatedvalue + coefmatrix[i]*array2[i]

    number = 1/(1+math.exp(-calculatedvalue-intercept))
    number =  number * 100
    number = math.floor(number)

    return render_template('result.html',number = number)

@app.route('/Error')
def Error():
    return render_template('Error.html')

@app.route('/Result')
def back():
    return redirect(url_for("my_form"))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

