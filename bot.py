import telethon
from telethon import events
from telethon.sync import functions
from telethon import TelegramClient
import telethon
import random
from random import choices
import time ;import os
from telethon.tl.functions.messages import GetPeerDialogsRequest
from telethon.sessions import StringSession
from config import *

auction = []

band = []

auction.append("vipjz\n")

@StrPython.on(
events.NewMessage(
outgoing=True, pattern=r"حجز"))
async def StrPychecker(event):
        clicks = 1
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        
        type = str(msg[0])
      
        username = await rando(type)
        await event.reply(f"Done Start On This Type  - {type}")

        while True:
                clicks += 1
                try:
                	os.remove("clicks.txt")
                except :
                	open("clicks.txt","a").write(str(clicks)+"\n")
                else:
                	open("clicks.txt","a").write(str(clicks)+"\n")
                try:
             	   await StrPython(GetPeerDialogsRequest(peers=[username]))
                except Exception as err:
                    if "No user has" in str(err):
                        try:
                        	await StrPython(functions.account.UpdateUsernameRequest(username=username))           
                        
                        	await StrPython.send_file(event.chat_id, "https://t.me/m_aBd/14",caption=f'''
DoNe Cliem 
⌯ User ⤷ @{username}
⌯ Save ⤷ Account
⌯ Clicks ⤷ {clicks}
⌯ Program ⤷ @kckkkkc''')
                        	os.remove("clicks.txt")
                        	break
                        except Exception as USFL:
                        	await StrPython.send_message(event.chat_id,f"User is error : @{username}\nError: {USLF}")
                    else:
                        continue                    
                        
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    	await StrPython.send_message(event.chat_id,f"User is band  : {username}")
                    	band.append(username)
                    	
                except telethon.errors.rpcerrorlist.UsernameOccupiedError:
                    	time.sleep(1);continue
                    	
                except telethon.errors.rpcerrorlist.FloodWaitError as ses:
                    	await StrPython.send_message(event.chat.id,f"Flood & {ses.seconds}")
                    	
                    	break
                except telethon.errors.rpcerrorlist.UsernamePurchaseAvailableError: 
                    	
                    	auction.append(username+"\n")
                    	
              
                except Exception as Error:
                   await StrPython.send_message(event.chat.id,f"Error in the check : {Error}\nUser is Err : @{username}") 
                   break
                   
       
ban = open("band.txt","r").read().split()
band.append(ban)

abcd = "qwertyuiopassdfghjklzxcvbnm"
number = "1234567890"

async def rando(type):
	if type == "#X***":
		q = random.choices(abcd)
		w = random.choices(abcd)
		user =[w[0],"x",q[0],q[0],q[0]]
		username = "".join(user)
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "x#***":
		q = random.choices(abcd)
		w = random.choices(abcd)
		user = ["x",w[0],q[0],q[0],q[0]]
		username = "".join(user)
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "##**#*":
		q = random.choices(abcd)
		w = random.choices(abcd)
		b = random.choices(abcd)
		user =[q[0],q[0],w[0],w[0],q[0],w[0]]
		username = "".join(user)
		
		
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "###**#":
		q = random.choices(abcd)
		w = random.choices(abcd)
		user = [q[0],q[0],q[0],w[0],w[0],q[0]]
		username = "".join(user)
		return username
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "تيست":
		q = random.choice(abcd)
		w = random.choice(abcd)
		user =[q[0],nu[0],w[0],q[0],w[0]]
		username = "".join(user)
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "wq***":
		q = random.choice(abcd)
		w = random.choice(abcd)
		nu = random.choices(number)
		num = random.choices(number)
		user = [w[0],q[0],nu[0],nu[0],nu[0]]
		username = "".join(user)
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "بوتات":
		q = random.choices(abcd)
		w = random.choices(abcd)
		b = random.choices(abcd)
		user = [q[0],w[0],b[0]]
		username = "".join(user)
		username = username+"bot"
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "بوت":
		q = random.choices(abcd)
		w = random.choices(abcd)
		b = random.choices(abcd)
		user = [q[0],b[0],"_",b[0]]
		username = "".join(user)
		username = username+"bot"
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username

@StrPython.on(events.NewMessage(outgoing=True, pattern=r"تشغيل الحجز"))
async def Shhtah(event):
	await event.reply(""" Welcome Selict Type
**لصيد ثلاثي بوت :** `حجز بوتات`
**لصيد رباعي بوت :** `حجز بوت`
**لصيد ثلاثي ارقام :** `حجز wq***`
**لصيد XLYYY :** `حجز #x***`
**لصيد سداسي :**  `حجز ###**#`
**لصيد ثلاثي :** `حجز ###**#`
**لصيد LXYYY : **`حجز x#***`
**للتجربه : **`حجز تيست`

""")

@StrPython.on(events.NewMessage(outgoing=True, pattern=r"الضغطات"))
async def Shhtah(event):
	try:
		n = open("clicks.txt","r").read()
		
	except:
		await event.reply("طافي يابه 🗽")
	else:
		
		await event.reply(f"عدد الضغطات حاليا : {n}")
	
	
	
	
	

for x in StrPython.iter_dialogs():
		if x.is_user and not x.entity.bot:
			
				too = x.id
	
				try:
					StrPython.send_message(too, msg)
				except BaseException:continue
StrPython.send_file("me","https://t.me/m_aBd/15",caption=f"""**Welcome To checker
bY [aBooD] (t.me/kckkkkc) .
*اليك الاوامر ادناة* .
`الأمر الاول : `ايقاف الحجز
`الأمر الثاني : `تشغيل الحجز
`الأمر الثالث* : `الضغطات*
""")
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     			    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
	
@StrPython.on(events.NewMessage(outgoing=True, pattern=r"ايقاف الحجز"))
async def Shhtah(event):
	await StrPython.send_message(event.chat_id,"جارِ ...")
	
	await StrPython.disconnect()
	time.sleep(5)
	
	await StrPython.start()
	await event.reply("تم")
print("Run")
StrPython.run_until_disconnected()
