# Work with Python 3.6
import discord, random, sys, os
from AnTeangaBheo import chapters, headings
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

general_help = '```\
Ceiltíoch (Irish for "Celticist") is a bot for converting a modified Celticist phonemic transcription (one simplified to be typeable in ASCII) to phonemic IPA transcriptions in the 3 main dialects of Irish.\n\
\n\
Commands:\n\
____________________\n\
c!haigh\t\t\t\t\t   Pings bot.\n\
c!help\t\t\t\t\t\tShows this help.\n\
c!help u|c|m\t\t\t\t  Shows transcription scheme for\n\
\t\t\t\t\t\t\t  Ulster/Connacht/Munster Irish respectively.\n\
c!help g\t\t\t\t\t  Shows help for the Gaelic script converter.\n\
\n\
u/<transcription>/\t\t\tConverts Celticist to IPA for Ulster Irish.\n\
c/<transcription>/\t\t\tConverts Celticist to IPA for Connacht Irish.\n\
m/<transcription>/\t\t\tConverts Celticist to IPA for Munster Irish.\n\
\n\
g/<latin script>/\t\t\t Converts Latin script to pseudo-Gaelic script.\n\
\n\
c!mts\t\t\t\t\t     Responds with a random Máirtín Tom Sheáinín\n\
\t\t\t\t\t\t\t  phrase.\n\
```'

ulster_help = "```\
Usage: u/<transcription>/\n\
\n\
Ulster Irish Celticist → IPA key\n\
____________________\n\
Vowels:\n\
Celticist: a e i o u @ a: e: i: o: u: ai au i@ u@\n\
IPA:       a ɛ ɪ ʌ ɤ ə æː eː iː ɔː ʉː ai oː ia ua\n\
\n\
Broad consonants:\n\
Celticist: b  d  f  g  G  k  K  l  L  m  n  N  p  r  R  s  t  v  x\n\
IPA:       bˠ d̪ˠ fˠ ɡ  ɣ  k  ŋ  lˠ l̪ˠ mˠ nˠ n̪ˠ pˠ ɾˠ ɾˠ sˠ t̪ˠ w  x\n\
\n\
Slender consonants:\n\
Celticist: b' d' dZ D f' g' j  k' K' l' L' m' n' N' p' r' R' s' t' tS  T v' x'\n\
IPA:       bʲ ʥ  dʒ d fʲ ɟ  j  c  ɲ  l l̠ʲ mʲ n  n̠ʲ pʲ ɾʲ ɾˠ ɕ  ʨ  tʃ  t  vʲ ç\n\
\n\
Other consonants:\n\
Celticist: h\n\
IPA:       h\n\
\n\
Suprasegmental symbols:\n\
Celticist: \"  %\n\
IPA:       ˈ  ˌ\n\
```"

connacht_help = "```\
Usage: c/<transcription>/\n\
\n\
Connacht Irish Celticist → IPA key\n\
____________________\n\
Vowels:\n\
Celticist: a e i o u @ a: e: i: o: u: ai au i@ u@ ei\n\
IPA:       a ɛ ɪ ʌ ʊ ə ɑː eː iː oː uː ai au iə uə ei\n\
\n\
Broad consonants:\n\
Celticist: b  d  f  g  G  k  K  l  L  m  n  N  p  r  R  s  t  v  x\n\
IPA:       bˠ d̪ˠ fˠ ɡ  ɣ  k  ŋ  lˠ l̪ˠ mˠ nˠ n̪ˠ pˠ ɾˠ ɾˠ sˠ t̪ˠ w  x\n\
\n\
Slender consonants:\n\
Celticist: b' d' dZ D f' g' j  k' K' l' L' m' n' N' p' r' R' s' t' tS  T v' x'\n\
IPA:       bʲ d̠ʲ dʒ d fʲ ɟ  ʝ  c  ɲ  l l̠ʲ mʲ n  n̠ʲ pʲ ɾʲ ɾˠ ɕ  t̠ʲ tʃ  t  vʲ ç\n\
\n\
Other consonants:\n\
Celticist: h\n\
IPA:       h\n\
\n\
Suprasegmental symbols:\n\
Celticist: \"  %\n\
IPA:       ˈ  ˌ\n\
```"

munster_help = "```\
Usage: m/<transcription>/\n\
\n\
Munster Irish Celticist → IPA key\n\
____________________\n\
Vowels:\n\
Celticist: a e i o u @ a: e: i: o: u: ai au i@ u@\n\
IPA:       a ɛ ɪ ʌ ʊ ə ɑː eː iː oː uː ai ɔu iə uə\n\
\n\
Broad consonants:\n\
Celticist: b  d  f  g  G  k  K  l  L  m  n  N  p  r  R  s  t  v  x\n\
IPA:       bˠ d̪ˠ fˠ ɡ  ɣ  k  ŋ  lˠ l̪ˠ mˠ nˠ n̪ˠ pˠ ɾˠ ɾˠ sˠ t̪ˠ vˠ x\n\
\n\
Slender consonants:\n\
Celticist: b' d' dZ D f' g' j  k' K' l' L' m' n' N' p' r' R' s' t' tS  T v' x'\n\
IPA:       bʲ dʲ dʒ d fʲ ɟ  ʝ  c  ɲ  lʲ l̠ʲ mʲ nʲ n̠ʲ pʲ ɾʲ ɾˠ ʃ  tʲ tʃ  t  vʲ ç\n\
\n\
Other consonants:\n\
Celticist: h\n\
IPA:       h\n\
\n\
Suprasegmental symbols:\n\
Celticist: \"  %\n\
IPA:       ˈ  ˌ\n\
```"

gaelic_help = '```\
Usage: g/<latin script>/\n\
\n\
Latin→Pseudo-Gaelic script converter\n\
____________________\n\
This converter turns regular latin script Irish ("Gaeilge") into\n\
pseudo-Gaelic script approximated by Unicode characters ("Ᵹⲁeıᒐᵹe").\n\
____________________\n\
Regular usage:\n\
\n\
Regular consonants, vowels and punctuation are typed as normal.\n\
e.g. g/t/ → ꞇ\n\
\n\
Dotted consonants are produced with consonant+h.\n\
e.g. g/bh/ → б\n\
\n\
Acute accents are produced using either your regular keyboard (á)\n\
or by typing a tilde "~" after the vowel.\n\
e.g. g/a~/ → ⲁ\u0301\n\
\n\
Grave accents are produced using either your regular keyboard (à)\n\
or by typing a vertical bar "|" after the vowel.\n\
e.g. g/a|/ → ⲁ\u0300\n\
\n\
Tironian et (⁊) is produced by typing an ampersand (&).\n\
____________________\n\
Scribal abbreviations:\n\
\n\
Overdot: g/a#./ → ⲁ\u0307\n\
Suspension stroke: g/a#-/ → ⲁ\u0305\n\
M stroke: g/a#-/ → ⲁ\u0303\n\
\n\
"con" abbreviation g/#c/ → ↄ\n\
```'

ulsterPhonology = ["a","ɛ","ɪ","ʌ","ɤ","ə","æː","eː","iː","ɔː","ʉː","ai","oː","ia","ua",\
     "bˠ","d̪ˠ","fˠ","ɡ","ɣ","k","lˠ","l̪ˠ","mˠ","nˠ","n̪ˠ","ŋ","pˠ","ɾˠ","ɾˠ","sˠ","t̪ˠ","w","x",\
     "bʲ","ʥ","dʒ","d","fʲ","ɟ","j","c","l","l̠ʲ","mʲ","n","n̠ʲ","ɲ","pʲ","ɾʲ","ɾˠ","ɕ","ʨ","tʃ","t","vʲ","ç",\
     "h","ˈ","ˌ"]
connachtPhonology = ["a","ɛ","ɪ","ʌ","ʊ","ə","ɑː","eː","iː","oː","uː","ai","au","iə","uə",\
     "bˠ","d̪ˠ","fˠ","ɡ","ɣ","k","lˠ","l̪ˠ","mˠ","nˠ","n̪ˠ","ŋ","pˠ","ɾˠ","ɾˠ","sˠ","t̪ˠ","w","x",\
     "bʲ","d̠ʲ","dʒ","d","fʲ","ɟ","ʝ","c","l","l̠ʲ","mʲ","n","n̠ʲ","ɲ","pʲ","ɾʲ","ɾˠ","ɕ","t̠ʲ","tʃ","t","vʲ","ç",\
     "h","ˈ","ˌ","ei"]
munsterPhonology = ["a","ɛ","ɪ","ʌ","ʊ","ə","ɑː","eː","iː","oː","uː","ai","ɔu","iə","uə",\
     "bˠ","d̪ˠ","fˠ","ɡ","ɣ","k","lˠ","l̪ˠ","mˠ","nˠ","n̪ˠ","ŋ","pˠ","ɾˠ","ɾˠ","sˠ","t̪ˠ","vˠ","x",\
     "bʲ","dʲ","dʒ","d","fʲ","ɟ","ʝ","c","lʲ","l̠ʲ","mʲ","nʲ","n̠ʲ","ɲ","pʲ","ɾʲ","ɾˠ","ʃ","tʲ","tʃ","t","vʲ","ç",\
     "h","ˈ","ˌ"]

oneToOnePhonology = ["a","e","i","o","u","@","A","E","I","O","U","{","}","1","2",\
     "b","d","f","g","w","k","l","l","m","n","n","y","p","r","r","s","t","v","x",\
     "B","D","J","Q","F","G","W","K","L","4","M","N","Z","Y","P","R","r","S","T","C","H","V","X",\
     "h","\"","%", "3"]

def phrase():
    choice = random.randint(1,16)
    if choice==1:
        chosenphrase = "sea"
    elif choice==2:
        chosenphrase = "by dad"
    elif choice==3:
        chosenphrase = "ab ea"
    elif choice==4:
        chosenphrase = "muis ab ea"
    elif choice==5:
        chosenphrase = "hahhh"
    elif choice==6:
        chosenphrase = "tá's am"
    elif choice==7:
        chosenphrase = "bail ó dhia ort"
    elif choice==8:
        chosenphrase = "mar sin é"
    elif choice==9:
        chosenphrase = "mmm"
    elif choice==10:
        chosenphrase = "bhoil má tá"
    elif choice==11:
        chosenphrase = "muis má tá"
    elif choice==12:
        chosenphrase = "ab in é an chaoi"
    elif choice==13:
        chosenphrase = "sin é anois é a mh'anam"
    elif choice==14:
        chosenphrase = "sin é an chaoi"
    elif choice==15:
        chosenphrase = "*ag ionanálú* sea"
    elif choice==16:
        chosenphrase = "*ag ionanálú* tá's am"
        
    return chosenphrase

client = discord.Client()

@client.event


async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    start = message.content.find("c!haigh")>-1

    #if message.content.find("tástáil")>-1:
    #    msg = 'tástáil tástáil'.format(message)
    #    await message.channel.send("tástáil") #client.send_message(message.channel, msg) 
    #ping
    if message.content.find("c!haigh")>-1:
        msg = 'Haigh a {0.author.mention}'.format(message)
        await message.channel.send(msg)
    
    elif message.content.find("c!help")>-1: 
        #ulster transcription guide
        if message.content.find("c!help u")>-1:
            msg = ulster_help.format(message)
            await message.channel.send(msg)
        #connacht transcription guide
        elif message.content.find("c!help c")>-1:
            msg = connacht_help.format(message)
            await message.channel.send(msg)
        #munster transcription guide
        elif message.content.find("c!help m")>-1:
            msg = munster_help.format(message)
            await message.channel.send(msg)
        #pseudo-gaelic script guide
        elif message.content.find("c!help g")>-1:
            msg = gaelic_help.format(message)
            await message.channel.send(msg)
        #main help
        else:
            msg = general_help.format(message)
            await message.channel.send(msg)
            
    #conamara 100
    elif message.content.lower().find("by dad muis anois má tá")>-1:
        firstphrase = phrase()
        extraphrases = " "+firstphrase[0].upper()+firstphrase[1:]
        for i in range(random.randint(1,3)):
            newphrase = phrase()
            while (firstphrase.find(newphrase)>-1 or extraphrases.find(newphrase)>-1):
                newphrase = phrase()
                
            extraphrases+=" "+newphrase
            
        msg = ":fire: :ok_hand: :flag_ie: ***Conⲁmⲁꞃⲁ*** :100: :flag_ie: :ok_hand: :fire: \n"+extraphrases+".".format(message)
        await message.channel.send(msg)
 
    #mts
    elif message.content.find("c!mts")>-1 or message.content.lower().find("máirtín")>-1\
    or message.content.lower().find("mháirtín")>-1 or message.content.lower().find("by dad")>-1 or message.content.lower().find("by deaid")>-1\
    or message.content.lower().find("baidh dad")>-1 or message.content.lower().find("baidh deaid")>-1:

        #emoji = client.get_emoji(693937741381238886)
        #await message.add_reaction(emoji)
        msg = phrase().format(message) 
        await message.channel.send(msg)

    #more mts
    elif message.content.lower().find("c!seafóid")>-1 or message.content.lower().find("c!seafoid")>-1:
        numberofsentences = random.randint(10,20)
        paragraph = ""
        for j in range(numberofsentences):
            phrases = phrase()
            phrases = phrases[0].upper()+phrases[1:]
                        
            for i in range(random.randint(0,10)):
                newphrase = phrase()
                while (phrases.find(newphrase)>-1):
                    newphrase = phrase()
                    
                phrases+=" "+newphrase
            phrases+="."
            if (j<numberofsentences):
                phrases+=" "
                
            paragraph+=phrases
            
        msg = paragraph.format(message)
        await message.channel.send(msg)
    
    #an teanga bheo chonamara
    elif message.content.find("c!atb")>-1:
        msg = " "
        command = message.content[message.content.find("c!atb")+6:]
        command.strip()
        
        if command[0].isdigit():
            command = command.split(".")
            chapter = int(command[0])
            paragraph = int(command[1])

        else:
            try:    
                chapter = headings[command][0]
                paragraph = headings[command][1]
            except KeyError:
                pass
            
        if chapter > 0 and chapter <= 17 and paragraph > 0:
            try:
                msg = (chapters[chapter-1][paragraph-1]).format(message)
                await message.channel.send(msg)
            except IndexError:
                pass

    #howlin
    elif message.content.lower().find("howlin")>-1:
        imageNumber= random.randint(1,2)
        await message.channel.send(file=discord.File("pics/howlin"+str(imageNumber)+".png"))

    #csl
    elif message.content.lower()=="csl":
        await message.channel.send(file=discord.File("pics/csl.png"))
        
    class Dialect:
        def __init__(self,prefixLetter, openBracketType, closeBracketType, phonemes):
            self.prefix = prefixLetter
            self.openBracket = openBracketType
            self.closeBracket = closeBracketType
            
            #vowels
            self.a = phonemes[0]
            self.e = phonemes[1]
            self.i = phonemes[2]
            self.o = phonemes[3]
            self.u = phonemes[4]
            self.schwa = phonemes[5]
            
            self.aLong = phonemes[6]
            self.eLong = phonemes[7]
            self.iLong = phonemes[8]
            self.oLong = phonemes[9]
            self.uLong = phonemes[10]

            self.ai = phonemes[11]
            self.au = phonemes[12]
            self.ia = phonemes[13]
            self.ua = phonemes[14]

            #consonants
            self.bBroad = phonemes[15]
            self.dBroad = phonemes[16]
            self.fBroad = phonemes[17]
            self.gBroad = phonemes[18]
            self.ghBroad = phonemes[19]
            self.kBroad = phonemes[20]
            self.lBroad = phonemes[21]
            self.llBroad = phonemes[22]
            self.mBroad = phonemes[23]
            self.nBroad = phonemes[24]
            self.nnBroad = phonemes[25]
            self.ngBroad = phonemes[26]
            self.pBroad = phonemes[27]
            self.rBroad = phonemes[28]
            self.rrBroad = phonemes[29]
            self.sBroad = phonemes[30]
            self.tBroad = phonemes[31]
            self.vBroad = phonemes[32]
            self.chBroad = phonemes[33]

            self.bSlender = phonemes[34]
            self.dSlender = phonemes[35]
            self.dZ = phonemes[36]
            self.dLoan = phonemes[37]
            self.fSlender = phonemes[38]
            self.gSlender = phonemes[39]
            self.ghSlender = phonemes[40]
            self.kSlender = phonemes[41]
            self.lSlender = phonemes[42]
            self.llSlender = phonemes[43]
            self.mSlender = phonemes[44]
            self.nSlender = phonemes[45]
            self.nnSlender = phonemes[46]
            self.ngSlender = phonemes[47]
            self.pSlender = phonemes[48]
            self.rSlender = phonemes[49]
            self.rrSlender = phonemes[50]
            self.sSlender = phonemes[51]
            self.tSlender = phonemes[52]
            self.tS = phonemes[53]
            self.tLoan = phonemes [54]
            self.vSlender = phonemes[55]
            self.chSlender = phonemes[56]

            self.h = phonemes[57]

            self.primaryStress = phonemes[58]
            self.secondaryStress = phonemes[59]
            
            if (len(phonemes)>60):
                self.ei = phonemes[60]
                
    def transcribe (dialect):
        remainingMessage = message.content
        ipaList  = []
        ipa = ""

        while(remainingMessage.find(dialect.prefix + dialect.openBracket)>-1):
            #has opening and closing brackets and space before opening bracket
            if not(remainingMessage.find(dialect.prefix + dialect.openBracket)>0 and remainingMessage[remainingMessage.find(dialect.prefix + dialect.closeBracket)-1]!=" ")\
            and remainingMessage[remainingMessage.find(dialect.prefix + dialect.openBracket)+2:].find(dialect.closeBracket)>0:
                
                remainingMessage = remainingMessage[remainingMessage.find(dialect.prefix + dialect.openBracket)+2:]
                celticist = remainingMessage
                
                remainingMessage = celticist[celticist.find(dialect.openBracket):]
                celticist = celticist[:celticist.find(dialect.closeBracket)+1]
                
                #make sure there's no spaces before the opening bracket and after the closing bracket (this stops people accidentally triggering the bot)
                if celticist[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ%\"" and celticist[-1] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ%\"":
                    ipa = ""

                    #add "-" after stress marks so sequences of vowels are preserved
                    print("celticist before:"+str(celticist))
                    celticist = list(celticist)

                    i=0
                    while(i<len(celticist)):
                        if celticist[i] in "\"%":
                            celticist[i:i]="-"
                            i+=1
                            print("current celticist:"+str(celticist))
                        i+=1
                    print("celticist after:"+str(celticist))         
                    for i in range(0, len(celticist)-1):
                        if celticist[i]==" ":ipa+=" ";continue
                        if celticist[i]=="-":ipa+="";continue
                        if i<len(celticist)-1: 
                            if celticist[i] in "bcdDfgGhjJkKlLʟmnNɴŋprRʀstTvwx":
                                #if celticist[i+1] in "aeoiu@"
                                if celticist[i+1] not in "'SZ":
                                    if celticist[i]=="b":   ipa += dialect.bBroad
                                    elif celticist[i]=="d": ipa += dialect.dBroad
                                    elif celticist[i]=="D": ipa += dialect.dLoan
                                    elif celticist[i]=="f": ipa += dialect.fBroad
                                    elif celticist[i]=="g": ipa += dialect.gBroad
                                    elif celticist[i]=="G": ipa += dialect.ghBroad
                                    elif celticist[i]=="j": ipa += dialect.ghSlender
                                    elif celticist[i]=="J": ipa += dialect.dZ
                                    elif celticist[i] in "kc": ipa += dialect.kBroad
                                    elif celticist[i] in "Kŋ": ipa += dialect.ngBroad
                                    elif celticist[i]=="l": ipa += dialect.lBroad
                                    elif celticist[i] in "Lʟ": ipa += dialect.llBroad
                                    elif celticist[i]=="m": ipa += dialect.mBroad
                                    elif celticist[i]=="n": ipa += dialect.nBroad
                                    elif celticist[i] in "Nɴ": ipa += dialect.nnBroad
                                    elif celticist[i]=="p": ipa += dialect.pBroad
                                    elif celticist[i]=="r": ipa += dialect.rBroad
                                    elif celticist[i] in "Rʀ": ipa += dialect.rrBroad
                                    elif celticist[i]=="s": ipa += dialect.sBroad
                                    elif celticist[i]=="t": ipa += dialect.tBroad
                                    elif celticist[i]=="T": ipa += dialect.tLoan
                                    elif celticist[i] in "vw": ipa += dialect.vBroad
                                    elif celticist[i]=="x": ipa += dialect.chBroad
                                    else: ipa+= celticist[i]
                                    continue
                                else:
                                    if celticist[i+1]=="\'":
                                        if celticist[i]=="b":   ipa += dialect.bSlender
                                        elif celticist[i]=="d": ipa += dialect.dSlender
                                        elif celticist[i]=="f": ipa += dialect.fSlender
                                        elif celticist[i]=="g": ipa += dialect.gSlender
                                        elif celticist[i]=="G": ipa += dialect.ghSlender
                                        elif celticist[i] in "kc": ipa += dialect.kSlender
                                        elif celticist[i] in "Kŋ": ipa += dialect.ngSlender
                                        elif celticist[i]=="l": ipa += dialect.lSlender
                                        elif celticist[i] in "Lʟ": ipa += dialect.llSlender
                                        elif celticist[i]=="m": ipa += dialect.mSlender
                                        elif celticist[i]=="n": ipa += dialect.nSlender
                                        elif celticist[i] in "Nɴ": ipa += dialect.nnSlender
                                        elif celticist[i]=="p": ipa += dialect.pSlender
                                        elif celticist[i]=="r": ipa += dialect.rSlender
                                        elif celticist[i] in "Rʀ": ipa += dialect.rrSlender
                                        elif celticist[i]=="s": ipa += dialect.sSlender
                                        elif celticist[i]=="t": ipa += dialect.tSlender
                                        elif celticist[i] in "vw": ipa += dialect.vSlender
                                        elif celticist[i]=="x": ipa += dialect.chSlender
                                        continue
                                    else:
                                        if celticist[i]=="d" and celticist[i+1]=="Z": ipa += dialect.dZ;i+=1
                                        if celticist[i]=="t" and celticist[i+1]=="S":   ipa += dialect.tS;i+=1

                        if celticist[i] in "\'SZ": i+=1;continue
                        #vowels    
                        if i<=len(celticist)+1:
                            
                            if i<len(celticist)-1 and celticist[i+1]==":":
                                if i>0 and celticist[i-1] in "aiu":
                                    continue
                                elif celticist[i]=="a": ipa += dialect.aLong;i+=1;continue
                                elif celticist[i]=="e": ipa += dialect.eLong;i+=1;continue
                                elif celticist[i]=="i": ipa += dialect.iLong;i+=1;continue
                                elif celticist[i]=="o": ipa += dialect.oLong;i+=1;continue
                                elif celticist[i]=="u": ipa += dialect.uLong;i+=1;continue
                                continue
                            elif i<len(celticist)-1:
                                if i>0 and celticist[i-1] in "aeiu":
                                    continue
                                else:
                                    if celticist[i]=="a" and celticist[i+1]=="i": ipa += dialect.ai;i+=1;continue
                                    if celticist[i]=="a" and celticist[i+1]=="u": ipa += dialect.au;i+=1;continue
                                    if celticist[i]=="i" and celticist[i+1]=="@": ipa += dialect.ia;i+=1;continue
                                    if celticist[i]=="u" and celticist[i+1]=="@": ipa += dialect.ua;i+=1;continue
                                    if celticist[i]=="e" and celticist[i+1]=="i": ipa += dialect.ei;i+=1;continue
                            if celticist[i]=="a": ipa += dialect.a
                            elif celticist[i]=="e": ipa += dialect.e
                            elif celticist[i]=="i": ipa += dialect.i
                            elif celticist[i]=="o": ipa += dialect.o
                            elif celticist[i]=="u": ipa += dialect.u
                            elif celticist[i]=="@": ipa += dialect.schwa

                            elif celticist[i]==":" or celticist[i]==";": ipa+=""

                            #primary/secondary stress
                            elif celticist[i]=="\"": ipa+= dialect.primaryStress
                            elif celticist[i]=="%": ipa+= dialect.secondaryStress
                            
                            else: ipa+=celticist[i]
                    ipaList.append(ipa)
                    continue
                else: break
            else: break
        return ipaList
        
    """Internal 1 to 1 Cois Fharraige Irish phonemic notation
    ____________________
    Vowels:
    Celticist: a e i o u @ A  E  I  O  U  {  }  1  2  3
    IPA:       a ɛ ɪ ʌ ʊ ə ɑː eː iː oː uː ai au iə uə ei

    Broad consonants:
    Celticist: b  d  f  g  w  k  y  l  m  n  p  r  s  t  v  x
    IPA:       bˠ d̪ˠ fˠ ɡ  ɣ  k  ŋ  l̪ˠ mˠ n̪ˠ pˠ ɾˠ sˠ t̪ˠ w  x

    Slender consonants:
    Celticist: B  D  J  Q F  G  W  K  Y  L  4  M  N  Z  P  R  S  T  C   H  V  X
    IPA:       bʲ d̠ʲ dʒ d fʲ ɟ  ʝ  c  ɲ  l  l̠ʲ mʲ nʲ n̠ʲ pʲ ɾʲ ɕ  t̠ʲ tʃ  t  vʲ ç

    Other consonants:
    Celticist: h
    IPA:       h

    Suprasegmental symbols:
    Celticist: "  %
    IPA:       ˈ  ˌ
    """

    def stressMap(transcription):
        stresses = []
        overallCounter = 0

        while(overallCounter<len(transcription)):
            #get current word
            currentWord = "";
            currentWordLength = 0
            currentWordStressMap = ""
            currentPosition = overallCounter
            #add letters to word
            while (currentPosition<len(transcription) and transcription[currentPosition]!=" "):
                currentWord += transcription[currentPosition]
                print("current word: "+currentWord)
                currentPosition+=1
                currentWordLength+=1
                
            #syllabify word 
            syllables = []
            currentSyllable = ""
            for i in range(0,len(currentWord)):

                #print("number of syllables so far: "+str(len(syllables)) + ", current syllable: "+currentSyllable+ " currentLetter: "+str(currentWord[i])+" i: "+str(i))
                #print("First condition (previous symbol is vowel): "+str(isVowel(currentWord[i-1])))
                #print("Second condition: (previous symbol is stress mark)"+str(currentWord[i] in "\"%"))

                #while (last symbol is a vowel and this symbol is a consonant) = false
                #new syllable
                if i>0 and (isVowel(currentWord[i-1]) or currentWord[i] in "\"%"):
                    #print("new syllable")
                    if (len(currentSyllable)>0):
                        syllables += {currentSyllable}
                    currentSyllable = currentWord[i]
                    #print("syllables:" + str(syllables)+" current syllable: " + currentSyllable)
                    
                #same syllable
                else:
                    currentSyllable += currentWord[i];print("same syllable")
            syllables += {currentSyllable}        
            #decide whether a syllable is stressed or unstressed          
            if (currentWord.find("\"")>-1 or currentWord.find("%")>-1):
                print("yes")
                for i in range(len(syllables)):
                    if (syllables[i][0] in "\"%"):
                        for j in range(len(syllables[i])):
                            print("this letter is: "+syllables[i][j])
                            stresses.append(True)
                    else:
                        for j in range(len(syllables[i])):
                            stresses.append(False)
            else:
                for i in range(len(syllables)):
                    print("syllable count: " + str(len(syllables)))
                    if (i==0):
                        for j in range(len(syllables[i])):
                            stresses.append(True)
                    else:
                        for j in range(len(syllables[i])):
                            stresses.append(False)
            overallCounter += currentWordLength+1

            if overallCounter<len(transcription): stresses.append(False)
        print("stresses length is "+str(len(stresses))+" syllables: "+str(len(syllables)))
        print("stresses: "+str(stresses))
        print("syllables: "+str(syllables))

        #remove stress marks from stresses[]
        print("transcription: "+transcription)
        print("stresses[] length"+ str(len(stresses)) + "transcription length "+str(len(transcription)))

        i=0
        """while i<len(stresses):
            if transcription[i] in "\"%":
                print("transcription["+str(i)+"] = "+transcription[i]+", stresses["+str(i)+"] = "+str(stresses[i]))
                print("i:::"+str(i)+"stresses[] length= "+str(len(stresses)));stresses.pop(i)
            i+=1"""
        print("new stresses: "+str(stresses))
        return stresses

    #----------SYMBOL TYPES ----------
    
    def isVowel(symbol):
        if symbol in "aeiou@AEOIU{}123":
            return True
        else:
            return False

    def isConsonant(symbol):
        if symbol in "aeiou@AEOIU{}123 ":
            return False
        else:
            return True

    #nasal consonants
    def isNasal(transcription,position):
        return transcription[position] in "ymnYMNZ"

    def isStop(transcription,position):
        return transcription[position] in "ptkbdgPTKBDGQH"
    
    def isBroad(transcription,position):
        if transcription[position] in "bdfgwkylmnprstvx":
            return True
        elif transcription[position] == "h":
            if position<len(transcription)-1:
                if transcription[position+1] in "ouAOU{}":
                    return True
                elif transcription[position+1] in "eiEI123":
                    if position<len(transcription)-2:
                        return isBroad(transcription,position+2)
        else:
            return False

    def isSlender(transcription,position):
        if transcription[position] in "bdfgwkylmnprstvx":
            return False
        elif transcription[position] == "h":
            if position<len(transcription)-1:
                if transcription[position+1] in "ouAOU{}":
                    return False
                elif transcription[position+1] in "eiEI123":
                    if position<len(transcription)-2:
                        return not (isBroad(transcription,position+2))
        else:
            if transcription[position] == " ": return False
            else: return True

    #----------DIACRITIC FUNCTIONS----------

    #nasalised vowels
    def isNasalised(transcription,position):
        if (position>0 and isNasal(transcription,position-1)) and (position==len(transcription)-1 or transcription[position+1]==" ") and \
           (transcription[position] in "eoiu"):
            print("NASAL VOWEL AT END OF WORD")
            return True
        elif (position>0 and transcription[position-1]=="m") and (position==len(transcription)-1 or transcription[position+1]==" ") and \
           (transcription[position]=="a"):
            return True
        
        elif (position>0 and isNasal(transcription,position-1)) and (position<len(transcription)-1 and isNasal(transcription,position+1)):
            return True
        else:
            return False
        
    def isVelarised(transcription,position):
        if transcription[position] in "dt":
            if (position>0 and transcription[position-1] in "aeiEI3") and (position==len(transcription)-1 or transcription[position+1]==" "):
                return False
            else:
                return True
        elif transcription[position]=="r":
            if (position==0 or transcription[position-1]==" ") and ((position<len(transcription)-1) and transcription[position+1] in "aeiEI3"):
                return False
            else:
                return True
                
        elif transcription[position]=="s":
            if position>0 and (transcription[position-1] in "uUn"):
                return True
            else:
                return False
            
        elif transcription[position] in "bflmnpr":
            return True
        else :
            return False

    def isPalatalised(transcription,position):
        if transcription[position] in "BDF4MNZPRTV":
            return True
        elif (transcription[position] in "s"):
            if (position>0 and transcription[position-1] in "aeEiI1N") and (position==len(transcription)-1 or transcription[position+1]==" "):
                return True
            else:
                return False
        else:
            return False
        
    def isAspirated(transcription,position,stresses):
        if transcription[position] in "ptkPTKCH" and (not isLaterallyReleased(transcription,position)) and (not isUnreleased(transcription,position)) and \
           (not isNasallyReleased(transcription,position,stresses)):
            if position>0:
                if isConsonant(transcription[position-1]) and ((position<len(transcription)-1) and (isVowel(transcription[position+1]) and not stresses[position+1])):
                    return False
                elif (transcription[position-1]=="x") and (transcription[position] in "tT") and \
                     ((position<len(transcription)-1) and transcription[position+1]==" "):
                    return False
                elif (transcription[position-1]=="S") and (transcription[position]=="T" and \
                     ((position<len(transcription)-1) and transcription[position+1]==" ")):
                    return False
                elif (transcription[position-1]=="S") and (transcription[position]=="K" and \
                     ((position<len(transcription)-1) and transcription[position+1]==" ")):
                    return False
                else:
                    return transcription[position-1]!="s"
            else:
                return True
        else:
            return False

    def isLaterallyReleased(transcription,position):
        if (transcription[position] in "td") and ((position<len(transcription)-1) and transcription[position+1]=="l"):
            return True
        elif (position>0 and transcription[position-1]=="y") and transcription[position]=="g" and \
             ((position<len(transcription)-1) and transcription[position+1]=="l"):
            return True
        else:
            return False
        
    def isUnreleased(transcription,position):
        return isStop(transcription,position) and ((position<len(transcription)-1) and isStop(transcription,position+1))

    def isNasallyReleased(transcription,position,stresses):
        return (transcription[position] in "gG") and \
           (position<len(transcription)-2 and isNasal(transcription,position+1) and ((isVowel(transcription[position+2]) and not stresses[position+2])))
            
    def phones(oneToOne):
        oneToOne = oneToOne[0]
        ipaList  = ""
        ipaList = list(ipaList)
        ipa = ""

        transcriptionWithoutStressMarks = list(oneToOne)
        primaryStressLocations = []
        secondaryStressLocations = []
        i = 0
        while(i<len(transcriptionWithoutStressMarks)):
            if transcriptionWithoutStressMarks[i] == "\"":
                primaryStressLocations.append(i)
                transcriptionWithoutStressMarks.pop(i)
                
            elif transcriptionWithoutStressMarks[i] == "%":
                secondaryStressLocations.append(i)
                transcriptionWithoutStressMarks.pop(i)
            i += 1
        
        transcriptionStresses = stressMap(oneToOne)

        for i in oneToOne:
            if i in "\"%":
                oneToOne = oneToOne.replace(i,"")
        
        for i in range(0, len(oneToOne)):
            ipa = ""
            ipa = list(ipa)
            if i in primaryStressLocations:
                ipa += "ˈ"
            elif i in secondaryStressLocations:
                ipa += "ˌ"
                
            #consonants
            if (isVowel(oneToOne[i])==False):
                #broad
                if oneToOne[i] == "b": ipa += "b"
                elif oneToOne[i] == "d": ipa += "d̪"
                elif oneToOne[i] == "f":
                    if ((i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and oneToOne[i+1] in "iIoOuU}")) or \
                       (i>0 and oneToOne[i-1]=="U"): ipa += "ɸ"
                    else: ipa += "f" #yes icf has rules regarding when it's [f] but there's only 2 members of this phoneme
                    
                elif oneToOne[i] == "g": ipa += "g"
                elif oneToOne[i] == "w": ipa += "ɣ"
                elif oneToOne[i] == "k": ipa += "k"
                elif oneToOne[i] == "g": ipa += "ɡ"
                elif oneToOne[i] == "w": ipa += "ɣ"
                elif oneToOne[i] == "k": ipa += "k"
                elif oneToOne[i] == "y": ipa += "ŋ"
                elif oneToOne[i] == "l": ipa += "l̪"
                elif oneToOne[i] == "m": ipa += "m"
                elif oneToOne[i] == "n": ipa += "n̪"
                elif oneToOne[i] == "p": ipa += "p"
                elif oneToOne[i] == "r": ipa += "ɾ"
                elif oneToOne[i] == "s": ipa += "s̻"
                elif oneToOne[i] == "t": ipa += "t̪"
                elif oneToOne[i] == "v":
                    if (i<len(oneToOne)-1 and (oneToOne[i+1]==" ")) or \
                        (i>0 and isBroad(oneToOne,i-1)) or \
                        ((i>0 and isVowel(oneToOne[i-1])) and (i<len(oneToOne)-1 and isVowel(oneToOne[i+1]))) or \
                        ((i<len(oneToOne)-2 and (oneToOne[i+1] in "lr") and (oneToOne[i+2] in "OuU"))): ipa += "β"
                         
                    elif (((i<len(oneToOne)-2 and (oneToOne[i+1] in "lr") and isVowel(oneToOne[i+2])))) or \
                           ((i>0 and (oneToOne[i-1] in "aA")) and (not transcriptionStresses[i])) or \
                           ((not transcriptionStresses[i]) and (i<len(oneToOne)-1 and (oneToOne[i+1] in "aA"))): "v"

                    elif (i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and isVowel(oneToOne[i+1])): ipa += "w"
                    
                    else: ipa += "w"
                    
                elif oneToOne[i] == "x": ipa += "x"
                
                #slender
                if oneToOne[i] == "B": ipa += "b"
                elif oneToOne[i] == "D": ipa += "d̠"
                elif oneToOne[i] == "J": ipa += "dʒ"
                elif oneToOne[i] == "Q": ipa += "d"
                elif oneToOne[i] == "F":
                    if i<len(oneToOne)-1:
                        if oneToOne[i+1] in "uU": ipa += "ɸ"
                        else: ipa += "f"
                elif oneToOne[i] == "G": ipa += "ɟ"
                elif oneToOne[i] == "W": ipa += "ʝ"
                elif oneToOne[i] == "K": ipa += "c"
                elif oneToOne[i] == "Y": ipa += "ɲ"
                elif oneToOne[i] == "L": ipa += "l"
                elif oneToOne[i] == "4": ipa += "l̠"
                elif oneToOne[i] == "M": ipa += "m"
                elif oneToOne[i] == "N": ipa += "n̠"
                elif oneToOne[i] == "Z": ipa += "n̠"
                elif oneToOne[i] == "P": ipa += "p"
                elif oneToOne[i] == "R": ipa += "ɾ"
                elif oneToOne[i] == "S":
                    if (i==0 or oneToOne[i-1]=="r") or (i<len(oneToOne)-1 and oneToOne[i+1]=="r"): ipa += "ʃ̺ˠʷ"
                    else: ipa += "ɕ"
                elif oneToOne[i] == "T": ipa += "t̠"
                elif oneToOne[i] == "C": ipa += "tʃ"
                elif oneToOne[i] == "H": ipa += "t"
                elif oneToOne[i] == "V":
                    if i<len(oneToOne)-1:
                        if oneToOne[i+1] in "uU": ipa += "β"
                        else: ipa += "v"
            
                elif oneToOne[i] == "X": ipa += "ç"

                #h
                elif oneToOne[i] == "h": ipa += "h"

                #consonant diacritics
                if isVelarised(oneToOne,i): ipa += "ˠ"
                elif isPalatalised(oneToOne,i): ipa += "ʲ"

                #consonant releases
                if isAspirated(oneToOne,i,transcriptionStresses): ipa += "ʰ"
                elif isLaterallyReleased(oneToOne,i): ipa += "ˡ"
                elif isUnreleased(oneToOne,i): ipa += "̚"
                elif isNasallyReleased(oneToOne,i,transcriptionStresses): ipa += "ⁿ"
                
                #space
                if oneToOne[i] == " ": ipa += " "

            else:
                #vowels

                if oneToOne[i]=="a":
                    #short allophones
                    if (i<len(oneToOne)-1 and oneToOne[i+1]=="h"):
                        if (i>0 and isSlender(oneToOne,i-1)): ipa += "æ̞" #this rule not completely icf but i extrapolated
                        elif (i>0 and isBroad(oneToOne,i-1)): ipa += "ä̠"

                    #long allophones
                    #æː
                    elif ((i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and ((isSlender(oneToOne,i+1) or oneToOne[i+1]=="s")))) or \
                         (((i>0 and (isSlender(oneToOne,i-1))) and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1)))) or \
                         (((i>0 and (isSlender(oneToOne,i-1))) and (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" ")))): ipa += "æ̞"
                    
                    elif (((i>0 and (isSlender(oneToOne,i-1))) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)))): ipa += "æ"
                    
                    elif (((i>0 and (isBroad(oneToOne,i-1))) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)))) or \
                         (((i>0 and oneToOne[i-1]=="h") and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1)))): ipa += "a̝"
                    #aː
                    elif ((i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and (isBroad(oneToOne,i+1)))) or \
                         (((i>0 and (isBroad(oneToOne,i-1))) and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1)))) or \
                         (((i>0 and (isBroad(oneToOne,i-1))) and (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" ")))): ipa += "ä̠"
                    
                    elif (((i>0 and (isBroad(oneToOne,i-1))) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)))) or \
                         (((i>0 and oneToOne[i-1]=="h") and (i<len(oneToOne)-1 and (oneToOne[i+1] in "gwkyx")))): ipa += "ä̟"
                    else: ipa += "ä̠"
                    
                if oneToOne[i]=="A":
                    if (i==0 or oneToOne[i-1]==" " or isBroad(oneToOne,i-1)): ipa += "ɑ"
                    elif i>0 and isSlender(oneToOne,i-1): ipa += "ɑ̟"
                    elif (i==0 and isSlender(oneToOne,i-1)) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)): ipa += "ɑ̽"
                    else: ipa += "ɑ"

                elif oneToOne[i]=="e":
                    if (i==0 or oneToOne[i-1]==" " or isSlender(oneToOne,i-1)) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)): ipa += "e̞"
                    elif (i>0 and isSlender(oneToOne,i-1)) and (i<len(oneToOne)-1 and (oneToOne[i+1]=="r" or oneToOne[i+1]==" ") or (i==len(oneToOne)-1)): ipa +="ɛ̽"
                    elif (i>0 and isBroad(oneToOne,i-1)) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)): ipa += "ɛ̠"
                    else: ipa += "e̞"
                    #to do: add special e allophone in mé etc

                elif oneToOne[i]=="E":
                    if transcriptionStresses[i] and \
                       ((i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)))\
                       or (i>0 and isSlender(oneToOne,i-1)): ipa += "e"
                    
                    elif (transcriptionStresses[i] and ((i==0 or oneToOne[i-1]==" ") and ((i<len(oneToOne)-1 and isBroad(oneToOne,i+1))) or \
                          ((i>0 and isBroad(oneToOne,i-1)) and (i<len(oneToOne)-1 and ((isSlender(oneToOne,i+1) or oneToOne[i+1]=="s")))))) or \
                          (((i>0 and (isSlender(oneToOne,i-1))) and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1)))): ipa += "e̞"
                           
                    elif ((i>0 and isBroad(oneToOne,i-1)) and ((i<len(oneToOne)-1 and (oneToOne[i+1]==" " or isBroad(oneToOne,i+1))) or i==len(oneToOne)-1)): ipa += "e̽"
                    else: ipa += "e"
                    
                elif oneToOne[i]=="i":
                    if transcriptionStresses[i] and (i==0 or oneToOne[i-1]==" ") and \
                       (isSlender(oneToOne,i-1)) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)): ipa += "i̽"
                    elif transcriptionStresses[i] and \
                            ( \
                                (\
                                (i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)) \
                                ) or \
                                (\
                                    ((i==0 or oneToOne[i-1]==" ") and isSlender(oneToOne,i-1)) and (i<len(oneToOne)-1 and oneToOne[i+1]=="s")
                                ) or \
                                (\
                                    (i>0 and isBroad(oneToOne,i-1)) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)) \
                                )\
                            ): ipa += "ɪ"
                    
                    elif (i>0 and not isVowel(oneToOne[i-1])) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)): ipa += "ɪ"

                    elif i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" "): ipa += "ɪ̽"
                    elif (i>0 and isSlender(oneToOne,i-1)) and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1)): ipa += "ɪ̈"
                    else: ipa += "ɪ"

                elif oneToOne[i]=="I":
                    if ((i==0 or oneToOne[i-1]==" ") and (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" "))) or \
                       ((i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1))) or \
                       (i>0 and isSlender(oneToOne,i-1)): ipa += "i"
                    elif ((i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1))) or \
                         ((i>0 and isBroad(oneToOne,i-1)) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1))): ipa += "i̞"

                    elif ((i>0 and isBroad(oneToOne,i-1)) and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1))) or \
                         ((i>0 and isBroad(oneToOne,i-1)) and (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" "))): ipa += "i̽"
                    else: ipa += "i"

                elif oneToOne[i]=="o":
                    if ((i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1))) or \
                       ((i>0 and isBroad(oneToOne,i-1)) and (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" "))) or \
                       ((i>0 and isBroad(oneToOne,i-1)) and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1))) or \
                       ((i>0 and isSlender(oneToOne,i-1)) and (i<len(oneToOne)-1 and oneToOne[i+1]=="x")): ipa += "ʌ"
                    elif ((i>0 and isBroad(oneToOne,i-1)) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1))) or \
                        ((i>0 and isSlender(oneToOne,i-1)) and (i<len(oneToOne)-1 and (oneToOne[i+1] not in "x"))): ipa += "ʌ̟"
                    else: ipa += "ʌ"

                elif oneToOne[i]=="O":
                    if (i==0 or oneToOne[i-1]==" " or isBroad(oneToOne,i-1)): ipa += "o̞"
                    elif (((i>0 and (isSlender(oneToOne,i-1))) and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1)))) or \
                        (((i>0 and (isSlender(oneToOne,i-1))) and (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" ")))): ipa += "o̽"
                    elif (((i>0 and (isSlender(oneToOne,i-1))) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)))): ipa += "o̽"
                    else: ipa += "o̞"

                elif oneToOne[i]=="u":
                    if (i>0 and (isSlender(oneToOne,i-1) or oneToOne[i-1]=="s")) and (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" ")) or \
                       (((i>0 and (oneToOne[i-1]=="t")) and (i<len(oneToOne)-1 and (oneToOne[i+1] in "st")))): ipa += "ö";print("IPA IS NOW "+str(ipa))
                    
                    elif ((i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1))) or \
                         ((i>0 and isBroad(oneToOne,i-1)) and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1))): ipa += "ʊ"
                          
                    elif ((i>0 and isBroad(oneToOne,i-1)) and (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" "))): ipa += "o̟"

                    elif (((i>0 and (isSlender(oneToOne,i-1))) and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1)))): ipa += "ʊ̟"

                    else: ipa += "ʊ"

                elif oneToOne[i]=="U":
                    if (i==0 or oneToOne[i-1]==" " or isBroad(oneToOne,i-1)): ipa += "u̞"
                    elif (((i>0 and (isSlender(oneToOne,i-1))) and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1)))) or \
                        (((i>0 and (isSlender(oneToOne,i-1))) and (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" ")))): ipa += "u̽"
                    elif (((i>0 and (isSlender(oneToOne,i-1))) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)))): ipa += "ü̞"
                    else: ipa += "u̞̞"

                elif oneToOne[i]=="@":
                    if ((i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1))) or \
                        (i>0 and isSlender(oneToOne,i-1)) and (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" ")) or \
                        ((i>0 and isSlender(oneToOne,i-1)) and (i<len(oneToOne)-1 and oneToOne[i+1]=="s")): ipa += "ɘ"

                    elif ((i>0 and isSlender(oneToOne,i-1)) and (i<len(oneToOne)-1 and (oneToOne[i+1] in "dnr"))): ipa += "ə"

                    elif ((i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and (oneToOne[i+1] in "drst"))) or \
                        ((i>0 and (oneToOne[i-1] in "drst")) and (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" "))): ipa += "ɜ"

                    elif ((i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and (oneToOne[i+1] not in "drst") and isBroad(oneToOne,i))) or \
                         ((i>0 and (oneToOne[i-1] not in "dmrst")) and isBroad(oneToOne,i-1)) or \
                         ((i>0 and isSlender(oneToOne,i-1)) and (i<len(oneToOne)-1 and (oneToOne[i+1] in "lx"))): ipa += "ɜ̠"

                    elif (i>0 and oneToOne[i]=="m") and (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" ")) or \
                         ((i>0 and isBroad(oneToOne,i-1)) and (i<len(oneToOne)-1 and (oneToOne[i+1] in "kw"))): ipa += "ɘ̠"
                    
                    else: ipa += "ə"
                        
                elif oneToOne[i]=="1":
                    if (i>0 and oneToOne[i-1]=="r"): ipa += "i̽ˑɜ̠"
                    elif i<len(oneToOne)-1 and (oneToOne[i+1] in "dst"): ipa += "iˑə̞"
                    elif i<len(oneToOne)-1 and isBroad(oneToOne,i+1): ipa += "iˑɜ̠"
                    elif i<len(oneToOne)-1 and isSlender(oneToOne,i+1): ipa += "iˑɛ̈"
                    elif (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" ")): ipa += "iˑə̟"
                    else: ipa += "iˑə̟"

                elif oneToOne[i]=="2":
                    if (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" ")): ipa += "o̝ˑə̞˗"
                    elif i<len(oneToOne)-1 and isSlender(oneToOne,i+1): ipa += "o̝ˑə̟"
                    elif i<len(oneToOne)-1 and isBroad(oneToOne,i+1): ipa += "o̝ˑʌ̈"
                    else: ipa += "o̝ˑə̞˗"

                elif oneToOne[i]=="3": ipa += "e̞ˑɪ̞̆˗"
                    
                elif oneToOne[i]=="{":
                    if (i==0 or oneToOne[i-1]==" " or isSlender(oneToOne,i-1)) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)): ipa += "ɛ̟ˑi"
                    
                    elif (((i>0 and (isSlender(oneToOne,i-1))) and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1)))): ipa += "ɛˑi̞"
                    
                    elif ((i>0 and isBroad(oneToOne,i-1)) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1))): ipa += "ɜ̞˖ˑi"
                    
                    elif ((i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and (isBroad(oneToOne,i+1)))) or \
                         (((i>0 and (isBroad(oneToOne,i-1))) and (i<len(oneToOne)-1 and isBroad(oneToOne,i+1)))) or \
                         (((i>0 and (isBroad(oneToOne,i-1))) and (i==len(oneToOne)-1 or (i<len(oneToOne)-1 and oneToOne[i+1]==" ")))): ipa += "ɐ̠ˑi̞"
                    else: ipa += "ɛ̟ˑi"
                
                elif oneToOne[i]=="}":
                    if (((i>0 and (isSlender(oneToOne,i-1))) and (i<len(oneToOne)-1 and (oneToOne[i+1] in "gwyx")))) or \
                         (((i>0 and (isSlender(oneToOne,i-1))) and (i<len(oneToOne)-1 and isSlender(oneToOne,i+1)))): ipa += "ɛ̠ˑʊ̝"

                    elif (((i>0 and (isSlender(oneToOne,i-1))) and (i<len(oneToOne)-1 and (oneToOne[i+1]=="k")))): "ɛ̠ˑu̞"

                    elif ((i==0 or oneToOne[i-1]==" ") and (i<len(oneToOne)-1 and (isBroad(oneToOne,i+1)))) or \
                         (i>0 and isBroad(oneToOne,i-1)): ipa += "ɑ̽ˑʊ̝"
                    else: ipa += "ɛ̠ˑʊ̝"

                #vowel diacritics
                if isNasalised(oneToOne,i):
                    if ipa[len(ipa)-1]=="˗" or ipa[len(ipa)-1]=="˖":
                        ipa[len(ipa)-2:len(ipa)-2]= "̃";print("one")
                    else:
                        ipa += "̃";print("two")
                    print("IPA IS NOW 2 "+str(ipa))    
                #vowel length
                if oneToOne[i] in "AEIOU":                   
                    if transcriptionStresses[i]:
                        ipa += "ː";
                    else:
                        ipa += "ˑ"
                elif oneToOne[i]=="a":
                    if not (i<len(oneToOne)-1 and oneToOne[i+1]=="h"):
                        if transcriptionStresses[i]:
                            ipa += "ː";
                        else:
                            ipa += "ˑ"


            ipaList += ipa
        print("ipa list: "+str(ipaList))
        return ipaList

    ulsterIrish = Dialect("u","/","/",ulsterPhonology)
    connachtIrish = Dialect("c","/","/",connachtPhonology)
    munsterIrish = Dialect("m","/","/",munsterPhonology)
    oneToOneDialect = Dialect("c","[","]",oneToOnePhonology)
    
    ulsterIrishTranscription = transcribe(ulsterIrish)
    connachtIrishTranscription = transcribe(connachtIrish)
    munsterIrishTranscription = transcribe(munsterIrish)
    oneToOneTranscription = transcribe(oneToOneDialect)
    
    msg = ""
    if len(ulsterIrishTranscription) > 0:
        transcription = transcribe(ulsterIrish)
        for i in range(len(transcription)):
            msg += '/' + transcription[i] + '/'
            if i < len(transcription):
                msg += ' '       
        msg = (msg).format(message)
        await message.channel.send(msg)

    msg = "" 
    if len(connachtIrishTranscription) > 0:
        transcription = transcribe(connachtIrish)
        for i in range(len(transcription)):
            msg += '/' + transcription[i] + '/'
            if i < len(transcription):
                msg += ' '       
        msg = (msg).format(message)
        await message.channel.send(msg)

    msg = ""
    if len(munsterIrishTranscription) > 0:
        transcription = transcribe(munsterIrish)
        for i in range(len(transcription)):
            msg += '/' + transcription[i] + '/'
            if i < len(transcription):
                msg += ' '       
        msg = (msg).format(message)
        await message.channel.send(msg)

    msg = ""
    if len(oneToOneTranscription) > 0:
        print(oneToOneDialect)
        print(transcribe(oneToOneDialect))

        outputList = phones(transcribe(oneToOneDialect))
        output = ""
        for i in range(0,len(outputList)):
            output += outputList[i]

        #print(str(output))
        msg = "[" + output + "]"
        msg = (msg).format(message)
        await message.channel.send(msg)
    
    #~~~~~~~~~~~~~~~ PSEUDO-GAELIC SCRIPT ~~~~~~~~~~~~~~~
        
    if message.content.find("g/")>-1:
        #has opening and closing brackets and space before opening bracket
        if not(message.content.find("g/")>0 and message.content[message.content.find("g/")-1]!=" ") and message.content[message.content.find("g/")+2:].find("/")>0:
            latin = message.content[message.content.find("g/")+2:]
            latin = latin[:latin.find("/")+1]
            #make sure there's no spaces before the opening bracket and after the closing bracket (this stops people accidentally triggering the bot)
            if latin[0]!=" " and latin[-1]!=" ":
                gaelic = ""
                for i in range(0, len(latin)-1):
                    if latin[i] in "bcdfgmpstBCDFGMPST":
                        if latin[i+1].lower() == "h":
                            if latin[i]=="b": gaelic+="b\u0307";i+=1;continue
                            elif latin[i]=="c" and latin[i-1]!="#": gaelic+="c\u0307";i+=1;continue
                            elif latin[i]=="d": gaelic+="ꝺ\u0307";i+=1;continue
                            elif latin[i]=="f": gaelic+="ꝼ\u0307";i+=1;continue
                            elif latin[i]=="g": gaelic+="ᵹ\u0307";i+=1;continue
                            elif latin[i]=="m": gaelic+="m\u0307";i+=1;continue
                            elif latin[i]=="p": gaelic+="p\u0307";i+=1;continue
                            elif latin[i]=="s": gaelic+="ꞅ\u0307";i+=1;continue
                            elif latin[i]=="t": gaelic+="ꞇ\u0307";i+=1;continue

                            elif latin[i]=="B": gaelic+="b\u0307";i+=1;continue
                            elif latin[i]=="C": gaelic+="C\u0307";i+=1;continue
                            elif latin[i]=="D": gaelic+="Ꝺ\u0307";i+=1;continue
                            elif latin[i]=="F": gaelic+="Ꝼ\u0307";i+=1;continue
                            elif latin[i]=="G": gaelic+="Ᵹ\u0307";i+=1;continue
                            elif latin[i]=="M": gaelic+="M\u0307";i+=1;continue
                            elif latin[i]=="P": gaelic+="P\u0307";i+=1;continue
                            elif latin[i]=="S": gaelic+="S\u0307";i+=1;continue
                            elif latin[i]=="T": gaelic+="Ꞇ\u0307";i+=1;continue
                            continue
                        else:
                            if latin[i]=="b": gaelic+="b"
                            elif latin[i]=="c" and latin[i-1]!="#": gaelic+="c"
                            elif latin[i]=="d": gaelic+="ꝺ"
                            elif latin[i]=="f": gaelic+="ꝼ"
                            elif latin[i]=="g": gaelic+="ᵹ"
                            elif latin[i]=="m": gaelic+="m"
                            elif latin[i]=="p": gaelic+="p"
                            elif latin[i]=="s": gaelic+="ꞅ"
                            elif latin[i]=="t": gaelic+="ꞇ"

                            elif latin[i]=="B": gaelic+="b"
                            elif latin[i]=="C": gaelic+="C"
                            elif latin[i]=="D": gaelic+="Ꝺ"
                            elif latin[i]=="F": gaelic+="Ꝼ"
                            elif latin[i]=="G": gaelic+="Ᵹ"
                            elif latin[i]=="M": gaelic+="M"
                            elif latin[i]=="P": gaelic+="P"
                            elif latin[i]=="S": gaelic+="S"
                            elif latin[i]=="T": gaelic+="Ꞇ"
                            continue
                    elif latin[i] in "aeiouAEIOU":
                        if latin[i+1] == "~":
                            if latin[i]=="a": gaelic+="ⲁ́";i+=1;continue
                            elif latin[i]=="e": gaelic+="é";i+=1;continue
                            elif latin[i]=="i": gaelic+="í";i+=1;continue
                            elif latin[i]=="o": gaelic+="ó";i+=1;continue
                            elif latin[i]=="u": gaelic+="ú";i+=1;continue

                            elif latin[i]=="A": gaelic+="Ⲁ";i+=1;continue
                            elif latin[i]=="E": gaelic+="Є";i+=1;continue
                            elif latin[i]=="I": gaelic+="Í";i+=1;continue
                            elif latin[i]=="O": gaelic+="Ó";i+=1;continue
                            elif latin[i]=="U": gaelic+="Ú";i+=1;continue
                        elif latin[i+1] == "|":
                            if latin[i]=="a": gaelic+="ⲁ";i+=1;continue
                            elif latin[i]=="e": gaelic+="è";i+=1;continue
                            elif latin[i]=="i": gaelic+="ì";i+=1;continue
                            elif latin[i]=="o": gaelic+="ò";i+=1;continue
                            elif latin[i]=="u": gaelic+="ù";i+=1;continue

                            elif latin[i]=="A": gaelic+="Ⲁ";i+=1;continue
                            elif latin[i]=="E": gaelic+="Є";i+=1;continue
                            elif latin[i]=="I": gaelic+="Ì";i+=1;continue
                            elif latin[i]=="O": gaelic+="Ò";i+=1;continue
                            elif latin[i]=="U": gaelic+="Ù";i+=1;continue
                        else:
                            if latin[i]=="a": gaelic+="ⲁ"
                            elif latin[i]=="e": gaelic+="e"
                            elif latin[i]=="i": gaelic+="ı"
                            elif latin[i]=="o": gaelic+="o"
                            elif latin[i]=="u": gaelic+="u"

                    elif latin[i]=="A": gaelic+="Ⲁ́"
                    elif latin[i]=="E": gaelic+="Є"
                    elif latin[i]=="I": gaelic+="I"
                    elif latin[i]=="O": gaelic+="O"
                    elif latin[i]=="U": gaelic+="U"
                    elif latin[i]=="á": gaelic+="ⲁ́"
                    elif latin[i]=="à": gaelic+="ⲁ̀"
                    elif latin[i]=="é": gaelic+="é"
                    elif latin[i]=="è": gaelic+="è"
                    elif latin[i]=="h":
                        if i>0 and latin[i-1] in "bcdfgmpstBCDFGMPST":
                            gaelic+=""
                        else:
                            gaelic+="h";
                    elif latin[i]=="í": gaelic+="í"
                    elif latin[i]=="ì": gaelic+="ì"
                    elif latin[i]=="j": gaelic+="ȷ"
                    elif latin[i]=="k": gaelic+="к"
                    elif latin[i]=="l": gaelic+="ᒐ"
                    elif latin[i]=="n": gaelic+="n"
                    elif latin[i]=="ó": gaelic+="ó"
                    elif latin[i]=="ò": gaelic+="ò"
                    elif latin[i]=="q": gaelic+="q"
                    elif latin[i]=="r": gaelic+="ꞃ"
                    elif latin[i]=="ú": gaelic+="ú"
                    elif latin[i]=="ù": gaelic+="ù"
                    elif latin[i]=="v": gaelic+="v"
                    elif latin[i]=="w": gaelic+="w"
                    elif latin[i]=="x": gaelic+="x"
                    elif latin[i]=="y": gaelic+="y"
                    elif latin[i]=="z": gaelic+="z"

                    elif latin[i]=="Á": gaelic+="Ⲁ́"
                    elif latin[i]=="À": gaelic+="Ⲁ̀"
                    elif latin[i]=="É": gaelic+="Є́"
                    elif latin[i]=="È": gaelic+="Є̀"
                    elif latin[i]=="H":
                        if i>0 and latin[i-1] in "bcdfgmpstBCDFGMPST":
                            gaelic+=""
                        else:
                            gaelic+="Һ"
                    elif latin[i]=="Í": gaelic+="Í"
                    elif latin[i]=="Ì": gaelic+="Ì"
                    elif latin[i]=="J": gaelic+="J"
                    elif latin[i]=="K": gaelic+="K"
                    elif latin[i]=="L": gaelic+="ᒐ"
                    elif latin[i]=="N": gaelic+="N"
                    elif latin[i]=="Ó": gaelic+="Ó"
                    elif latin[i]=="Ò": gaelic+="Ò"
                    elif latin[i]=="Q": gaelic+="Q"
                    elif latin[i]=="R": gaelic+="R"
                    elif latin[i]=="Ú": gaelic+="Ú"
                    elif latin[i]=="Ù": gaelic+="Ù"
                    elif latin[i]=="V": gaelic+="V"
                    elif latin[i]=="W": gaelic+="W"
                    elif latin[i]=="X": gaelic+="X"
                    elif latin[i]=="Y": gaelic+="Y"
                    elif latin[i]=="Z": gaelic+="Z"

                    #scribal abbreviations
                    elif latin[i]=="#":
                        #overdot
                        if latin[i+1]==".":
                            gaelic+="\u0307"
                        #suspension stroke
                        elif latin[i+1]=="-":
                            gaelic+="\u0305"
                        #m stroke
                        elif latin[i+1]=="~":
                            gaelic+="\u0303"
                        #"con" abbreviation
                        elif latin[i+1]=="c":
                            gaelic+="\u2184"
                        elif latin[i+1]=="C":
                            gaelic+="\u2183"
                            
                    elif latin[i]=="&": gaelic+="⁊"
                    elif latin[i]=="~": gaelic+=""
                    elif latin[i]=="." and latin[i-1]=="#": gaelic+=""
                    elif latin[i]=="-" and latin[i-1]=="#": gaelic+=""
                    elif latin[i]=="|": gaelic+=""
                    else: gaelic+=latin[i]

                msg = (gaelic).format(message)
                await message.channel.send(msg)

                        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Activity(name="c!help for info"))

client.run(TOKEN)

