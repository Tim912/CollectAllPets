



# CAP AFK Script – Installations Guide

**1. Downloads**

Lade beides in der jeweils **neusten Version** herunter:

* [Python](https://www.python.org/downloads/)
* [Tesseract (UB Mannheim Version)](https://github.com/UB-Mannheim/tesseract/wiki)

> **Bei der Python-Installation unbedingt „Add to PATH“ anhaken!**



**2. Installation prüfen**

Öffne die Eingabeaufforderung (**CMD**) und prüfe:

```
pip --version
python --version
```

Wenn beides eine Version anzeigt, passt alles.



**3. Benötigte Python-Pakete installieren**

Gib diese Befehle (einzeln) ein:

```
pip install pytesseract
pip install pillow
pip install opencv-python
pip install psutil
pip install requests
```



**4. Skript downloaden**

Lade das Skript (`roblox_monitor.py`) im Releases-Bereich dieses Repos herunter.



**5. Discord Webhook erstellen**

1. Eigenen Server erstellen
2. In die Einstellungen
3. Integrationen
4. Webhook erstellen
5. Webhook personalisieren
6. Webhook-Link kopieren und speichern



**6. Skript konfigurieren**

Öffne `roblox_monitor.py` z.B. mit Notepad++ oder VS Code. Passe diese Zeilen an:

```python
WEBHOOK_URL = "https://discord.com/api/webhooks/..."  # Dein Discord Webhook-Link
PROCESS_NAME = "RobloxPlayerBeta.exe"                 # Anpassen je nach Version
LOG_PATH = os.path.expandvars(r"%LOCALAPPDATA%\Roblox\logs")   # Ggf. Pfad anpassen
KEYWORDS = ["Disconnect reason received", "Client:Disconnect"]
BOOSTR_TRIGGERS = [".9"]
CHECK_INTERVAL = 60  # Intervall in Sekunden
```



**7. Skript starten**

Speichere das Skript z.B. auf den Desktop.
Öffne die Eingabeaufforderung und führe aus:

```
cd Desktop
python roblox_monitor.py
```



**Das Skript läuft jetzt und schickt Status-Updates an deinen Discord-Webhook!**

# Roblox Starten!
---

MIT License

Copyright (c) 2025 Tim912

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
