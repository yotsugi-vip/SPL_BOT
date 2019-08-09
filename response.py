import spl_resourse as r
import random
import discord_custom as dc


dic = {}
users = {}

def help():
    m = ("---ウデマエとパワーの設定---\n"
             "X 2100~\n"
             "S 1800~2000\n"
             "A 1500~1700\n"
             "B 1400~1600\n"
             "C 1500~1300\n"
             "\n---コマンド一覧-------------\n"
             "**`random`**\n"
             "武器をランダムで選出\n"
             "**`random vc`** \n"
             "全ボイスチャンネルにいるメンバにランダムで武器を選出\n"
             "**`random all`** \n"
             "サーバーの全メンバにランダムで武器を選出\n"
             "**`試合順`**,**`order`**\n"
             "試合順をランダムで選出\n"
             "**`exit`**\n"
             "ボットログアウト\n"
             "**`reg ウデマエ`**\n"
             "いい感じにチームを分ける機能の選手登録\n"
             "**`show`**\n"
             "登録選手表示\n"
             "**`makeTeam`**,**`チーム`**\n"
             "チーム作成"
             )
             
    return m



def gameOrder():

    random.shuffle(r.gameOrder)
    i = 1
    m = ""

    for item in r.gameOrder:
        m += "第" + str(i) + "試合 : " + item + "\n"
        i += 1
    
    return m


def randomWeapon( message ):

    random.shuffle(r.weapon)
    i = random.randint(0,len(r.weapon))
    m = dc.mention( message.author.id ) + r.weapon[i]

    return m


def randomWeapon_vc( message ):
    server = message.channel.guild
    v_channels = server.voice_channels
    m = ""

    random.shuffle(r.weapon)

    for vc in v_channels:
        for member in vc.members:
            i = random.randint(0,len(r.weapon))
            m += dc.mention( member.id ) + r.weapon[i] + "\n"
    
    if m == "":
        m = "だれもいない?"

    return m


def randomWeapon_all(message):
    server = message.channel.guild
    m = ""
    
    for member in server.members:
        random.shuffle(r.weapon)
        i = random.randint(0,len(r.weapon))
        m += dc.mention( member.id ) + r.weapon[i] + "\n"

    return m


def regPlayer( message ):

    s = message.content + " ?"
    m = ""

    splt = s.split(" ")
    p = splt[1].upper()
    r = judgePower( p )
    
    if r == -1:
        m += "正しくないウデマエが入力されました" + p
    else:
        m += dc.mention( message.author.id ) + "を登録します"
        dic[message.author.name] = r
        users[message.author.name] = message.author.id

    return m


def judgePower( p ):

    ret = -1
    try:
        i = p.upper()
        ret = r.dic_power[ i ]
    
    except KeyError:
        ret = -1

    return ret


def showReg():
    m = "現在登録中\n"
    
    for s in dic:
        m += s + "\n"
    
    return m


def makeTeam():   
    
    l = len(dic)

    play_k = list()
    watch_k = list()
    play = dict()

    play_x = dict()

    if l < 6:
        m = "チーム作成の最低人数は6名です。\n現在" + str(l) + "名"
    else:
        
        teamNum = ( l - l % 2 ) / 2
        keys = list(dic.keys())
        
        # 参加者と観戦者を選択
        # キーを分ける
        for i in range(l):
            if i < (teamNum*2):
                play_k.append(keys[i])
            else:
                watch_k.append(keys[i])

        # 参加プレイヤー取得
        for item in play_k:
            play[item] = dic[item]

        play_k.clear()
        play_k = list(play.keys())

        play_notx = dict()
        # Xとそれ以外で分ける

        for key in play_k:
            if play[key] >= 2000:
                play_x[key] = play[key]
            else:
                play_notx[key] = play[key]
        
        

        team_A = list()
        team_B = list()

        play_k = list(play_x.keys())
        random.shuffle(play_k)
        
        teamA_m ="Alpha\n"
        teamB_m ="Blabo\n"

        i = 0
        for key in play_k:
            if i%2 == 0:
                team_A.append(key)
                teamA_m += dc.mention( str( users[key] ) ) + "\n"
            else:
                team_B.append(key)
                teamB_m +=  dc.mention( str( users[key] ) ) + "\n"
            i += 1

        play_k = list(play_notx.keys())
        random.shuffle(play_k)
            
        for key in play_k:
            if i%2 == 0:
                team_A.append(key)
                teamA_m += dc.mention( str( users[key] ) ) + "\n"
            else:
                team_B.append(key)
                teamB_m +=  dc.mention( str( users[key] ) ) + "\n"
            i += 1

        m = teamA_m + teamB_m
    return m


def makeTeam_t():
    m = "test\n"    
    
    dic = { "A 1600" : 1600, "B 2000" : 2000, "C 1800" : 1800, "D 2600" : 2600,
            "E 1200" : 1200, "F 1500" : 1500, "G 1800" : 1800, "H 2000" : 2000,
            "I 1000" : 1000 }

    l = len(dic)


    play_k = list()
    watch_k = list()
    play = dict()

    play_x = dict()

    if l < 6:
        m = "チーム作成の最低人数は6名です。\n現在" + str(l) + "名"
    else:
        
        teamNum = ( l - l % 2 ) / 2
        keys = list(dic.keys())
        
        # 参加者と観戦者を選択
        # キーを分ける
        for i in range(l):
            if i < (teamNum*2):
                play_k.append(keys[i])
            else:
                watch_k.append(keys[i])

        # 参加プレイヤー取得
        for item in play_k:
            play[item] = dic[item]

        play_k.clear()
        play_k = list(play.keys())

        play_notx = dict()
        # Xとそれ以外で分ける

        for key in play_k:
            if play[key] >= 2000:
                play_x[key] = play[key]
            else:
                play_notx[key] = play[key]
        
        

        team_A = list()
        team_B = list()

        play_k = list(play_x.keys())
        random.shuffle(play_k)
        
        teamA_m ="Alpha\n"
        teamB_m ="Blabo\n"

        i = 0
        for key in play_k:
            if i%2 == 0:
                team_A.append(key)
                teamA_m += str(key) + "\n"
            else:
                team_B.append(key)
                teamB_m += str(key) + "\n"
            i += 1

        play_k = list(play_notx.keys())
        random.shuffle(play_k)
            
        for key in play_k:
            if i%2 == 0:
                team_A.append(key)
                teamA_m += str(key) + "\n"
            else:
                team_B.append(key)
                teamB_m += str(key) + "\n"
            i += 1

        m = teamA_m + teamB_m
    return m


def test( message ):
    server = message.channel.guild
    
    for member in server.members:
        p = random.randint(1200,2300)
        dic[member.name] =  p
        users[member.name] = member.id

    return "test"