from telethon import TelegramClient, events
from telethon.tl.functions.channels import GetParticipantRequest,GetParticipantRequest
from telethon.tl.types import  ChannelParticipantAdmin,ChannelParticipantCreator
from random import choice, randint
import asyncio
import json
import random
import unicodedata


telethon_api_id = "29783495"
telethon_api_hash = "2d461ad1a30d66d819bce54f58bb262a"

client = TelegramClient("telethon_session", telethon_api_id,telethon_api_hash)



@client.on(events.NewMessage(pattern = r'\/cold'))
async def cold_command(event):
    await event.reply(
    "**Cold Game Aktivdir**\n\n"
    "🎮 **Mövcud oyunlar**\n\n"
    "🔤 **Söz oyunu:**\n"
    "`/startcold` - Oyunu başlat\n"
    "`/stopcold` - Oyunu bitir\n\n"
    "🔄 **Qarışıq hərfli sözlər:**\n"
    "`/startmix` - Qarışıq hərf oyununu başlat\n"
    "`/pas` - Növbəti sözə keçid\n"
    "`/stopmix` - Qarışıq hərf oyununu dayandır\n\n"
    "👥 **Etiketləmə:**\n"
    "`/tagcold <mesaj>` - istifadəçini etiketlə\n"
    "`/stoptag` - Etiketləmə prosesini dayandır\n"
)


word_list = [
    "D A V A M L I", "T Ə H L Ü K Ə S İ Z L İ K", "T Ə Ş Ə B B Ü S K A R", "İ D E Y A L A R",
    "Y A R A D I C I", "A R T I Q L I Q", "B İ L İ K L İ L İ K", "A R X A D A Ş L I Q",
    "F Ə A L İ Y Y Ə T L İ", "İ L K İ N L İ K", "A L İ C Ə N A B L I Q", "M Ö V Z U D A Ş",
    "B A Ş L A N G I C", "A Ç I Q S Ö Z L Ü L Ü K", "S A B İ T L İ K", "M Ü N A Q İ Ş Ə S İ Z",
    "S Ə M İ M İ L İ K", "M A S S İ V L İ K", "N Ü M A Y İ Ş E T M Ə", "G İ Z L İ N L İ K",
    "D Ü Ş Ü N C Ə S İ Z", "T A P Ş I R I Q L I", "Y A X Ş I L I Q", "U Ç U Z L A Ş M A",
    "Ə M İ N L İ K", "P R O Q N O Z L U Q", "M Ü Q A V İ M Ə T", "T A N I N M A Z",
    "Q O R X U S U Z L U Q", "İ N A M S I Z L I Q", "S A M İ M İ L İ K", "M Ü H İ T İ N T Ə R K",
    "H E S A B L A Y I C I", "Y E N İ L İ Y Ç İ L İ K", "İ Ş İ G Ö R M Ə K", "H A R A D A N S A",
    "Ə R A Z İ Q U R U L U Ş U", "G Ü L M Ə L İ L İ K", "A C A N L A Ş M A Q", "Ə L İ V Ə R İ L M Ə",
    "Ə H D İ D İ R L İ K", "F Ə S L Ə T S İ Z", "B İ R L İ K Ç İ L İ K", "D İ Z A Y N Ç I L I Q",
    "P R O B L E M L İ L İ K", "S A D Ə L İ Y Y Ə T", "H Ü N Ə R L İ L İ K", "Ə V V Ə L İ N C İ",
    "İ S T E D A D L I", "S A D Ə Ç İ L İ K", "H E Ç K İ M İ K", "A Z A D L I Q S E V Ə R",
    "T Ə Ş Ə K K Ü R L Ü", "D Ə R İ N L İ K L Ə R", "İ S T İ Q A M Ə T", "F Ə R Q L İ L İ K",
    "Y Ü K S Ə K L İ K", "Ç Ə T İ N L İ K", "M Ü Ş A H İ D Ə T Ç İ", "G Ü N Ə Ş İ L İ K",
    "Q Ü D R Ə T L İ", "T Ə C R Ü B Ə L İ", "S A B İ T L İ K", "T Ə D Q İ Q A T Ç I",
    "S İ F A R İ Ş Ç İ", "T Ə Q D İ R L İ", "Ə D Ə B İ L İ Y Y Ə T", "M Ü K A F A T Ç I",
    "T Ə B İ İ L İ K", "F İ K İ R D A Ş L I Q", "G Ə L Ə C Ə Y Ç İ", "S A D Ə L İ Q",
    "A B A D L A Ş D I R M A Q","A Y D I N L A Ş D I R I L M A Q","D A L Ğ A L A N M A Q",
    "Y A X I N L A Ş D I R M A Q","Y Ü K S Ə K L İ K", "M Ü K Ə M M Ə L L İ K", "S O N S U Z L U Q", 
    "H Ə Y A T S E V Ə R L İ K", "U Ğ U R S U Z L U Q", "T Ə D B İ R L İ L İ K", "Ç Ə T İ N L İ K L Ə R", 
    "Ə Z M K A R O L M A Q", "M Ə Q S Ə D Y O N L Ü L Ü K", "Ə M Ə K D A Ş L I Q", "D A V A M L I L I Q", 
    "İ N T E L L E K T U A L", "T Ə C R Ü B Ə Q A Z A N M A Q", "B İ L İ K D Ə Ü S T Ü N L Ü K", 
    "F Ə D A K A R L I Q", "İ N K İ Ş A F E T M Ə", "A Y D I N L I Q", "Ö Z Ü N Ü İ N K İ Ş A F", 
    "İ N T U İ S İ Y A L", "Z Ə K A L I O L M A Q", "K R E A T İ V L İ K", "B Ə R P A E T M Ə", 
    "F Ə A L İ Y Y Ə T L İ L İ K", "Ç A L I Ş Q A N L I Q", "F Ə L S Ə F Ə D Ü Ş Ü N C Ə",
    "Q Ə T İ Y Y Ə T L İ K", "Ə D Ə L Ə T L İ L İ K", "D Ə Y İ Ş İ K L Ə R Ə U Y Q U N L A Ş M A", 
    "S O N S U Z Q A B İ L İ Y Y Ə T", "T Ə Ş Ə B B Ü S K A R O L M A Q", "M Ə Q S Ə D Y O N L Ü", 
    "D Ə R İ N D Ü Ş Ü N C Ə", "T Ə H L İ L Q A B İ L İ Y Y Ə T İ", "Y E N İ L İ K Ç İ L İ K", 
    "İ N N O V A T İ V L İ K", "İ R A D Ə Q Ü V V Ə S İ", "S Ə M İ M İ L İ K", "Ü S T Ü N L Ü K L Ə R İ Ə L D Ə E T M Ə Q", 
    "F İ K İ R D Ə R İ N L İ K", "S Ə B İ R L İ O L M A Q", "G Ü C L Ə N D İ R M Ə Q", "Ö Z Ü N Ə İ N A M", 
    "F Ə A L İ Y Y Ə T P L A N I", "D A V A M L I İ N K İ Ş A F", "M Ü S B Ə T D Ü Ş Ü N C Ə", 
    "S Ə X A V Ə T L İ L İ K", "Z Ə N G İ N L Ə Ş D İ R M Ə Q", "K A R Y E R A İ N K İ Ş A F I", 
    "B Ö Y Ü K D Ü Ş Ü N C Ə", "İ Z Q O Y M A Q"
]
azerbaijani_words = []
with open("azerbaijani_words.txt", "r", encoding="utf-8") as file:
    for line in file:
        azerbaijani_words.append(line.strip().lower())


active_word = None
used_words = set()
scores = {}
current_turn = 1
max_turns = 20
turn_duration = 40
remaining_words = []
game_active = False
current_chat_id = None


async def is_admin(user_id, chat_id):
    permissions = await client.get_permissions(chat_id, user_id)
    return permissions.is_admin or permissions.is_creator

@client.on(events.NewMessage(pattern=r'\/startcold$', outgoing=True, incoming=True))
async def start_game(event):
    global active_word, used_words, scores, current_turn, remaining_words, game_active, current_chat_id
    await event.delete()
    
    chat = await event.get_chat()
    sender = await event.get_sender()

      
    bot_participant = await client(GetParticipantRequest(chat.id, 'me'))
    if not (isinstance(bot_participant.participant, ChannelParticipantAdmin) or
            isinstance(bot_participant.participant, ChannelParticipantCreator)):
        await event.reply("❗ ᴏʏᴜɴᴜ ʙᴀşʟᴀᴛᴍᴀĞɪᴍ üᴄüɴ ᴍəɴə ᴍᴇꜱᴀᴊ ꜱɪʟᴍə ʏᴇᴛᴋɪꜱɪ ᴠᴇʀᴍəʟɪꜱəɴ ɢᴏᴢəʟɪᴍ")
        return

    if not await is_admin(event.sender_id, event.chat_id):
        await event.reply("⛔ **Bu əmri yalnız adminlər istifadə edə bilər!**")
        return

    if game_active:
        await event.reply("⚠️ **Oyun artıq aktivdir!**")
        return

    used_words.clear()
    scores.clear()
    current_turn = 1
    remaining_words = word_list.copy()
    game_active = True
    current_chat_id = event.chat_id

    active_word = random.choice(remaining_words)
    remaining_words.remove(active_word)
    used_words.clear()
    await event.reply(f"🎮 𝙾𝚢𝚞𝚗 𝚋𝚊ş𝚕𝚊𝚍ı! \n\n Ｔｕｒ 1/{max_turns} \n Əｓａｓ Ｓöｚ:\n👀 {active_word}")
    await asyncio.sleep(turn_duration)

    for _ in range(max_turns - 1):
        if not game_active:
            break
        if not remaining_words:
            await event.reply("⚠️ **Bütün sözlər istifadə olundu!**")
            break

        active_word = random.choice(remaining_words)
        remaining_words.remove(active_word)
        used_words.clear()

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        score_text = "\n".join([f" <b>{i + 1}.</b> {(await client.get_entity(user_id)).first_name}: {score} xal"
                            for i, (user_id, score) in enumerate(sorted_scores)])
        await event.reply(
            f"⏳ Ｔｕｒ {current_turn + 1}/{max_turns} \n\n{score_text} \n\n\n Ｙｅｎｉ Ｓöｚ: \n👀 {active_word}",
            parse_mode="html"
        )
        await asyncio.sleep(turn_duration)
        current_turn += 1

    await end_game(event)

@client.on(events.NewMessage(pattern=r'\/stopcold$', outgoing=True, incoming=True))
async def stop_game(event):
    global game_active
    await event.delete()

    if not await is_admin(event.sender_id, event.chat_id):
        await event.reply("⛔ **Bu əmri yalnız adminlər istifadə edə bilər!**")
        return

    if not game_active:
        await event.reply("🛑 **Oyun hal-hazırda aktiv deyil!**")
        return

    game_active = False
    await end_game(event)

@client.on(events.NewMessage)
async def handle_word(event):
    global active_word, used_words, scores

    if not game_active or active_word is None or event.chat_id != current_chat_id:
        return

    
    user_word = event.raw_text.strip().lower()
    user_id = event.sender_id

    if user_word in used_words or user_word not in azerbaijani_words:
        return

    
    if all(char in active_word.lower() for char in user_word):
        used_words.add(user_word)
        points = len(user_word)
        first_name = (await client.get_entity(user_id)).first_name
        scores[user_id] = scores.get(user_id, 0) + points
        await event.reply(f"{first_name} 𝐜𝐚𝐯𝐚𝐛 𝐝𝐨𝐠𝐫𝐮𝐝𝐮𝐫! 🤙\n 𝚜𝚒𝚣 {points} 𝚡𝚊𝚕 𝚚𝚊𝚣𝚊𝚗𝚍ı𝚗ı𝚣 \n\n {active_word}")

async def end_game(event):
    global active_word, used_words, scores, current_turn, remaining_words, game_active, current_chat_id

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    if sorted_scores:
        top_user_id, top_score = sorted_scores[0]
        top_user_name = (await client.get_entity(top_user_id)).first_name
        winner_text = f"🏆 <b>Qalib:</b>\n {top_user_name} ({top_score} xal)"
    
    scoreboard = "\n".join([f" <b>{i + 1}.</b> {(await client.get_entity(user_id)).first_name}: {score} xal"
                            for i, (user_id, score) in enumerate(sorted_scores)])
    await event.reply(f"🎉 ᴏʏᴜɴ ʙɪᴛᴅɪ!\n\n {winner_text}\n\n ꜱᴋᴏʀ ᴄəᴅᴠəʟɪ: \n\n {scoreboard}", parse_mode="html")

    active_word = None
    used_words.clear()
    scores.clear()
    current_turn = 1
    remaining_words.clear()
    game_active = False
    current_chat_id = None



MESAJ_METNI = """
🎉 **Biri ᴏʏᴜɴ dedi?** 🎉

✨ **ʙᴜʀᴅᴀʏᴀᴍ ᴄᴀɴıᴍ!** Mən @DevCold tərəfindən yaradılan bir **ᴏʏᴜɴ ᴜsᴇʀʙᴏᴛᴜʏᴀᴍ** 🎮

🎮 **Mövcud Oyunlarım:**  
   • **Sᴏ̈ᴢ ᴏʏᴜɴᴜ**
   • **Qarışıq Hərf Oyunu**

📜 **Əmrlər:**  
   🕹️ **/startcold** - Sᴏ̈ᴢ ᴏʏᴜɴᴜɴᴜ ʙᴀşʟᴀᴛ 🎲  
   ⛔ **/stopcold** - Sᴏ̈ᴢ ᴏʏᴜɴᴜɴᴜ ʙɪᴛɪʀ 🛑  
   
   🕹️ **/startmix** - Qarışıq Hərf Oyununu Başlat 🎲  
   ⏭️ **/pas** - Sözdən Söze Keçid ⏩  
   ⛔ **/stopmix** - Qarışıq Hərf Oyununu Dayandır 🛑
"""

@client.on(events.NewMessage)
async def oyun_mesaji(event):
    if event.raw_text.strip().lower() == "oyun" and not event.sender.bot:
        try:
            await client.send_message(event.chat_id, MESAJ_METNI, link_preview=False)
        except Exception as e:
            print(f"Mesaj gönderilemedi: {e}")




scores = {}

sozler =  [
    "komputer", "proqram", "robot", "teleqram", "internet", "dil", "məktəb", "elm", "sistem", "təcrübə",
    "hesablama", "şəbəkə", "təhlükəsizlik", "məlumat", "idarəetmə", "ağıllı", "funksiya", "düstur", "təhlil", "məsələ",
    "texnologiya", "kalkulyator", "təsnifat", "emal", "nəticə", "təchizat", "araşdırma", "mühəndislik", "tədris",
    "yaddaş", "rəqəmsal", "informasiya", "layihə", "vasitə", "şifrə", "inkişaf", "idarəçi", "məkan",
    "adam", "advokat", "bahalı", "bakal", "bakteriya", "başqa", "balıqçı", "batmaq", "bildiriş", 
    "birdən", "bacanaq", "buzlaq", "bəraət", "böhtan", "bölünmək", "boşqab", "bükmək", "bədən", "cadu",
    "cadugər", "cahil", "caiz", "calaq", "camış", "can", "canavar", "canlı", "cansız", "cari", 
    "casus", "cavab", "cavab vermək", "cavan", "caynaq", 
    "caz", "cazibə", "cazibədar", "cehiz", "cem", "ciddi", 
    "cihaz", "cild", "cilov", "cin", "cinayət", "cinayətkar", "cins", "cinsi", "cır", "cırcırama", 
    "cırmaq", "cisim", "civə", "cizgi", "corab", 
    "coğrafi", "coğrafiya", "coşmaq", "coşqun", 
    "cökə", "cücü", "dalğalı", "dalğıc", "dalğınlıq", "dam", "damaq", 
    "damar", "damcı", "damcılamaq", "dammaq", "damğa", "dana", 
    "danışdı", "danışıq", "danışmaq", "danlamaq", "danlanmaq", "danlatmaq", "dar", "daraq", "darı", "darıxdırıcı", 
    "darıxmaq", "dartmaq", "darvaza", "darçın", "dava", "davranış", "daxili", "daxma", "dayanacaq", 
    "dayandırmaq", "dayanmaq", "dayaq", "dayaz", "dayı", "daylaq", "dayça", "dayə", "dazlaşmaq", 
    "dağ", "dağılmaq", "dağıntı", "dağıtmaq", "dağlaləsi", "dağlıq", 
    "daş", "daşımaq", "daşıyıcı", 
    "dekabr", "delfin", "demokratiya", "demək", 
    "demək ki", "deməli", "deputat", "desant", "desert", "devirmək","etdirmək", "etibar", "etimad", "etiraf", "etiraz", "etmək", "ev", "Everest", "evli",
    "evlənmək", "ey", "eybəcər", "eyham", "eyhamlı", "eyib", "eyni", "eyvan",
    "eşik", "eşitmək", "eşmək", "eşq", "eşşək", "fabrik", "faciə", "faiz", "fakt",
    "fakültə", "fani", "fantastik", "farsca", "fasad", "faydalı", "faydasız", "fayton",
    "fevral", "fidan", "fikir", "fikir vermək", "fikirli", "fikirləşmək", "fil", 
    "Filippin", "filiz", "film", "filosof", "fincan", "fındıq", "Finlandiya",
    "futbolçu", "fürsət", "Füzuli", "fəal", "fəaliyyət", "fəhlə", "fəlakət", 
    "fəlsəfə", "gavalı", "gec", "gecə", "gediş", "general", "geniş", "geologiya", 
    "geoloq", "gerb", "geriləmək", "getmək", "geydirmək", "geyim", "geyindirmək", 
    "geyinmək", "geymək", "gicgah", "gicitkən", "gigiyena", "gil", "gilas", "giliz", 
    "gilə", "giləmeyvə", "gilənar", "gimnastika", "gips", "girdə", "giriş", "girmək", 
    "girov", "Hacıqabul", "hadisə", "hakim", "hakimiyyət", "halqa", "halva", "hamam", 
    "hamar", "hambal", "hamı", "hamilə", "hamısı", "haqq", "haqqında", "hara", 
    "harada", "haraya", "hasar", "hasarlamaq", "hasil", "hasilat", "heykəl", 
    "heykəltəraş", "heykəltəraşlıq", "heyran", "heyva", "heyvandarlıq", "heyət", 
    "heç", "ibadət", "ibarə", "iblis", "icad", "icarə", "icazə", "icazə vermək", 
    "iclas", "icmal", "icraçı", "ictimai", "idarə", "idarə etmək", "idbar", "iddia", 
    "iddiaçı", "ideya", "idman", "idmançı", "idrak", "ifadə", "ifadə etmək", 
    "ifaçı", "iffətli", "iflic", "ifritə", "iftira", "igid", "iki", "il", "ilahi", 
    "ilanbalığı", "ilbiz", "ildırım", "kabab", "kabel", "kadr", "kafir", "kaftar", 
    "kahı", "kahin", "kainat", "kakao", "kaktus", "kal", "Kaliforniya", "kalium", 
    "kalsium", "kamal", "Kamal", "kaman", "ki", "kifayət", "kifir", "kiflənmək", 
    "kilid", "kilidləmək", "Kilis", "kilometr", "kilsə", "kim", "liman", "limon", 
    "linza", "mahir", "mahnı", "mexanizm", "meyar", "meydan", "meydança", "meyil", 
    "meymun", "meyvə", "meşə", "milyon", "milçək", "min", "mina", "minarə", 
    "minbər", "mineral", "Mingəçevir", "möcüzə", "möhkəm"
]


games = {}

@client.on(events.NewMessage(pattern=r"^/startmix$", outgoing=True, incoming=True))
async def start_game(event):
    global sozler
    
    chat_id = event.chat_id
    
    if chat_id in games and games[chat_id]["current_word"]:
        await event.reply("🔄 Oyun artıq davam edir!")
        return
    
    
    games[chat_id] = {
        "current_word": "",
        "shuffled_word": "",
        "tur_sayi": 0,
        "max_tur": 40,
        "scores": {},
        "used_words": set()  
    }
    
    await start_new_round(event)

async def start_new_round(event):
    """Yeni bir oyun turunu başlatır."""
    chat_id = event.chat_id
    game_data = games[chat_id]
    
    if game_data["tur_sayi"] >= game_data["max_tur"]:
        if game_data["scores"]:
            kazanan_id, en_yuksek_puan = max(game_data["scores"].items(), key=lambda x: x[1])
            kazanan_name = (await client.get_entity(kazanan_id)).first_name
            await event.reply(f"🏆 Oyun bitdi! Qalib: {kazanan_name} ({en_yuksek_puan} xal) 🎉")
        else:
            await event.reply("🛑 Oyun bitdi, heç kim xal qazanmadı.")
        games.pop(chat_id)  
        return
    
    
    available_words = [word for word in sozler if word not in game_data["used_words"]]
    
    if not available_words:
        await event.reply("🛑 Bütün sözlər istifadə edilib, oyun bitdi!")
        games.pop(chat_id)  
        return
    
    current_word = random.choice(available_words)
    shuffled_word = ''.join(random.sample(current_word, len(current_word)))
    first_letter = current_word[0]  
    word_length = len(current_word)  
    points = word_length  
    
    
    game_data["current_word"] = current_word
    game_data["shuffled_word"] = shuffled_word
    game_data["tur_sayi"] += 1  
    game_data["used_words"].add(current_word)  
    
    await event.reply(f"Tur {game_data['tur_sayi']}/{game_data['max_tur']}\n\n"
                      f"🔤 Qarışıq söz : **{shuffled_word}**\n"
                      f"📍 İlk hərf: **{first_letter}**\n"
                      f"🔢 Xal: **{points}**\n"
                      f"🔠 Hərf sayı: **{word_length}**\n\n"
                      f"Düzgün sözü tapmağa çalışın!")
    
    
    if game_data["tur_sayi"] % 10 == 0:
        await show_scores(event)

@client.on(events.NewMessage(pattern=r"^/stopmix$", outgoing=True, incoming=True))
async def stop_game(event):
    chat_id = event.chat_id
    
    if chat_id in games:
        games.pop(chat_id)  
        user_id = event.sender_id
        user = await client.get_entity(user_id)
        first_name = user.first_name or "İstifadəçi"
        first_name_mention = f"[{first_name}](tg://user?id={user_id})"
        await event.reply(f"🛑 Oyun {first_name_mention} tərəfindən dayandırıldı")
    else:
        await event.reply("❗ Hal-hazırda davam edən bir oyun yoxdur.")

async def show_scores(event):
    """Xal cədvəlini göstərir."""
    chat_id = event.chat_id
    game_data = games.get(chat_id, {})
    
    if game_data.get("scores"):
        score_table = "📊 **Xal Cədvəli**\n\n"
        for user_id, score in sorted(game_data["scores"].items(), key=lambda x: x[1], reverse=True):
            user_name = (await client.get_entity(user_id)).first_name
            score_table += f"👤 {user_name}: {score} xal\n"
        await event.reply(score_table)
    else:
        await event.reply("📊 Hələ heç kim xal qazanmadı.")

@client.on(events.NewMessage)
async def check_answer(event):
    chat_id = event.chat_id
    game_data = games.get(chat_id)
    
    if not game_data or not game_data["current_word"]:
        return
    
    user_id = event.sender_id
    user_name = (await event.get_sender()).first_name
    
    
    if event.text.lower() == game_data["current_word"].lower():
        word_length = len(game_data["current_word"])
        game_data["scores"][user_id] = game_data["scores"].get(user_id, 0) + word_length
        
        await event.reply(f"🎉 Təbriklər, {user_name}!\n Düzgün cavabı tapdınız: **{game_data['current_word']}**\n"
                          f"🔢 Xalınız: {game_data['scores'][user_id]} (+{word_length} xal)")
        
        
        game_data["current_word"] = ""
        game_data["shuffled_word"] = ""
        
        if game_data["tur_sayi"] < game_data["max_tur"]:
            await start_new_round(event)
        else:
            kazanan_id, en_yuksek_puan = max(game_data["scores"].items(), key=lambda x: x[1])
            kazanan_name = (await client.get_entity(kazanan_id)).first_name
            await event.reply(f"🏆 Oyun bitdi! Qalib: {kazanan_name} ({en_yuksek_puan} xal) 🎉")
            games.pop(chat_id)  

@client.on(events.NewMessage(pattern=r"^/pas$", outgoing=True, incoming=True))
async def skip_turn(event):
    chat_id = event.chat_id
    game_data = games.get(chat_id)
    
    if not game_data or not game_data["current_word"]:
        await event.reply("❗ Hal-hazırda davam edən bir oyun yoxdur")
        return
    
    user_id = event.sender_id
    user_name = (await event.get_sender()).first_name
    
    
    current_score = game_data["scores"].get(user_id, 0)
    
    
    if current_score < 5:
        await event.reply(f"❌ {user_name}, **sözü pas keçmək üçün yetəri qədər xalınız yoxdur**")
        return
    
    
    game_data["scores"][user_id] = current_score - 5
    
    await event.reply(f"⏭️ {user_name} **Sözü pas keçdi və 5 xal ondan çıxıldı**\nDüzgün cavab: **{game_data['current_word']}** idi")

    await start_new_round(event)


is_tagging = False


@client.on(events.NewMessage(pattern='/tagcold (.+)'))
async def tagcold(event):

    sender = await event.get_sender()
    if sender.username:
        initiator = f"@{sender.username}"  
    else:
        initiator = f"{sender.first_name}"  

    await event.reply(f"**𝙴𝚝𝚒𝚔𝚎𝚝𝚕ə𝚖ə𝚢ə 𝚋𝚊𝚜𝚕𝚊𝚢𝚒𝚛𝚊𝚖 ə𝚣𝚒𝚣** {initiator}")
    await asyncio.sleep(2)

    global is_tagging
    is_tagging = True  

    
    tag_message = event.pattern_match.group(1)

    
    chat = await event.get_input_chat()
    participants = await client.get_participants(chat)

    
    for participant in participants[:250]:
        if not is_tagging:  
            return

        if participant.username:
            
            tag = f"{tag_message} @{participant.username}"
        else:
            
            tag = f"{tag_message} [{participant.first_name}](tg://user?id={participant.id})"
        
        
        await event.respond(tag)
        await asyncio.sleep(2)  

    
    is_tagging = False
    await event.reply("✅ Etiketleme prosesi tamamlandı.")


@client.on(events.NewMessage(pattern='/stoptag'))
async def stoptag(event):
    global is_tagging
    is_tagging = False  
    await event.reply("❌ Etiketleme prosesi dayandırıldı.")


print("bot aktivdir")
client.start()
client.run_until_disconnected()


