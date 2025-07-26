import os
import psutil
import time
import requests
from datetime import datetime
##
## INFO! Ihr könnt das Script renamen und den path ändern falls ihr emulater nutzt wodurch ihr dann auch 10 stück offen haben könnt 
##
WEBHOOK_URL = "https://discord.com/api/webhooks/..."  # Hier euer Webhook 
PROCESS_NAME = "RobloxPlayerBeta.exe" # Anpassen je nach microsoft oder roblox.com version 
LOG_PATH = os.path.expandvars(r"%LOCALAPPDATA%\Roblox\logs")   # Euer log path müsst ihn anpassen jenachdem welche version ihr habt (standart für roblox.com version)
KEYWORDS = ["Disconnect reason received", "Client:Disconnect", "InGame.ConnectionError.DisconnectIdle"]

BOOSTR_TRIGGERS = [".9"]
CHECK_INTERVAL = 60  ## Interval in Sekunden kann auch bis 20min oder so hoch gestellt werden

letzter_status = None
letzter_boostr = True

def webhook_send(title, desc, color, ping=False):
    data = {
        "content": "@everyone" if ping else "",
        "embeds": [{
            "title": title,
            "description": desc,
            "color": color,
            "footer": {"text": "CAP Script 1 Copyright 2025 Trixi900"},
            "timestamp": datetime.utcnow().isoformat()
        }]
    }
    try:
        requests.post(WEBHOOK_URL, json=data)
    except Exception as e:
        print(f"Webhook-Fehler: {e}")

def roblox_offen():
    for proc in psutil.process_iter(attrs=["name"]):
        try:
            if PROCESS_NAME.lower() in proc.info["name"].lower():
                return True
        except:
            pass
    return False

def check_log():
    if not os.path.exists(LOG_PATH):
        return False, False

    files = sorted(
        [f for f in os.listdir(LOG_PATH) if f.endswith(".log")],
        key=lambda f: os.path.getmtime(os.path.join(LOG_PATH, f)),
        reverse=True
    )
    if not files:
        return False, False

    filepath = os.path.join(LOG_PATH, files[0])
    found_error = False
    found_boostr = False
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()[-300:]
            for line in lines:
                line_lower = line.lower()
                if any(k in line_lower for k in KEYWORDS):
                    found_error = True
                if any(b in line for b in BOOSTR_TRIGGERS):
                    found_boostr = True
    except Exception as e:
        print("Fehler beim Lesen:", e)

    return found_error, found_boostr

def watchdog():
    global letzter_status, letzter_boostr
    while True:
        jetzt = datetime.now().strftime("%H:%M:%S")
        roblox_status = roblox_offen()
        fehler, boostr = check_log()


        if letzter_status is not None and letzter_status and not roblox_status:
            webhook_send("❌ Roblox geschlossen", f"Roblox wurde um `{jetzt}` geschlossen oder gekickt.", 0xff0000, ping=True)


        if letzter_status is not None and not letzter_status and roblox_status:
            webhook_send("✅ Roblox gestartet", f"Roblox läuft seit `{jetzt}`", 0x00ff00)


        if letzter_boostr and not boostr:
            webhook_send("⚠️ Kein .9 mehr!", f"Seit `{jetzt}` wurde kein `.9` Boostr mehr gefunden.", 0xffcc00, ping=True)


        if fehler:
            webhook_send("❗ Fehler erkannt", f"`{jetzt}`: Disconnect, Leave oder Error gefunden.", 0xff5555, ping=True)


        statusbericht = f"""**Statusbericht**
🟢 Roblox läuft: `{roblox_status}`
📦 x.9 Boostr (Nur in Script2) : `{boostr}`
🚨 Fehler im Log: `{fehler}`
🕐 Letzter Check: `{jetzt}`"""
        webhook_send("📊 Status Update", statusbericht, 0x3498db)

        letzter_status = roblox_status
        letzter_boostr = boostr
        time.sleep(CHECK_INTERVAL)

watchdog()