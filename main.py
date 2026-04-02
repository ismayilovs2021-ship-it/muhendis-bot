import requests
import time
import random
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# --- RENDER PORT HİYLƏSİ ---
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Multi-Language Bot is Running!")

def run_server():
    try:
        server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
        server.serve_forever()
    except: pass

threading.Thread(target=run_server, daemon=True).start()

# --- MƏLUMATLAR ---
TOKEN = "8357425880:AAG-4PEylzM4aQb1RxEYbLdCDVE--KmaONg"
# Bura həm qrup, həm kanal ID-ni dırnaqda yaz (vergüllə ayır)
QURUPLAR = ["-1003824053223"] 

yaddas = []
translator_az = GoogleTranslator(source='en', target='az')
translator_tr = GoogleTranslator(source='en', target='tr')

sekil_kateqoriyalari = [
    "https://images.unsplash.com/photo-1485827404703-89b55fcc595e", # Robot
    "https://images.unsplash.com/photo-1518770660439-4636190af475", # Chip/Circuit
    "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158", # Engineering Lab
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b", # Cyber Security
    "https://images.unsplash.com/photo-1517077304055-6e89abbf09b0", # Tech Work
    "https://images.unsplash.com/photo-1531297484001-80022131f5a1", # Future Tech
    "https://images.unsplash.com/photo-1581092160562-40aa08e78837", # Mechanical
    "https://images.unsplash.com/photo-1504639725590-34d0984388bd", # Coding/Software
    "https://images.unsplash.com/photo-1451187530230-b237ee702656", # Space/Satellite
    "https://images.unsplash.com/photo-1563770660941-20978e870e93", # Data Center
    "https://images.unsplash.com/photo-1581092341396-d44445300a1f", # Industrial
    "https://images.unsplash.com/photo-1531746790731-6c087fecd05a", # AI/Brain
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c", # Teamwork Tech
    "https://images.unsplash.com/photo-1581092918056-0c4c3acd3789", # Electrical
    "https://images.unsplash.com/photo-1460925895917-afdab827c52f", # Tech Analysis
    "https://images.unsplash.com/photo-1535223289827-42f1e9919769", # Virtual Reality
    "https://images.unsplash.com/photo-1509062522246-3755977927d7", # Education Tech
    "https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc", # Drone
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085", # Laptop/Dev
    "https://images.unsplash.com/photo-1581092795360-fd1ca04f0952", # Automation
    "https://images.unsplash.com/photo-1555664424-778a1e5e1b48", # Logic Board
    "https://images.unsplash.com/photo-1516110833967-0b5716ca1387", # Network/Web
    "https://images.unsplash.com/photo-1581094481213-9118c7647240", # Factory/Eng
    "https://images.unsplash.com/photo-1558494949-ef010cbdcc51", # Server/Cloud
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d", # Innovation
    "https://images.unsplash.com/photo-1581093458791-9f3c3900df4b", # Research
    "https://images.unsplash.com/photo-1515879218367-8466d910aaa4", # Python/Coding
    "https://images.unsplash.com/photo-1518433278988-2b2a197e9994", # Science Art
    "https://images.unsplash.com/photo-1496065187959-7f07b8353c55", # Lab Experiment
    "https://images.unsplash.com/photo-1487014679447-9f8336841d58", # Digital Future
    "https://images.unsplash.com/photo-1517433447747-24440dca3063", # Circuit Board Macro
    "https://images.unsplash.com/photo-1504384764586-bb4cdc1707b0", # Modern Tech Lab
    "https://images.unsplash.com/photo-1496171367470-9ed9a91ea931", # Computer Design
    "https://images.unsplash.com/photo-1451187863213-d1bcbaae3fa3", # Digital Network
    "https://images.unsplash.com/photo-1531482615713-2afd69097998", # Engineering Meeting
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085", # Web Development
    "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5", # Coding Green
    "https://images.unsplash.com/photo-1535223289827-42f1e9919769", # VR Headset
    "https://images.unsplash.com/photo-1580894732234-8b5dc4ce0a66", # Tech Hardware
    "https://images.unsplash.com/photo-1518770660439-4636190af475", # CPU Chipset
    "https://images.unsplash.com/photo-1485827404703-89b55fcc595e", # Humanoid Robot
    "https://images.unsplash.com/photo-1504164996022-09080787b6b3", # Blueprint/Draft
    "https://images.unsplash.com/photo-1581094794329-c8112a89af12", # Robotics Arm
    "https://images.unsplash.com/photo-1432888622747-4eb9a8f2c20e", # Software Architecture
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c", # Tech Teamwork
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b", # Security Shield
    "https://images.unsplash.com/photo-1551288049-bbbda536339a", # Data Analytics
    "https://images.unsplash.com/photo-1523961131990-5ea7c61b2107", # Artificial Intel
    "https://images.unsplash.com/photo-1526628953301-3e589a6a8b74", # Clean Tech Lab
    "https://images.unsplash.com/photo-1581093583449-80dca9db283e"  # Engineer Control
]

def xeber_paylas():
    while True:
        try:
            url = "https://news.google.com/rss/search?q=engineering+technology&hl=en-US&gl=US&ceid=US:en"
            res = requests.get(url, timeout=20)
            soup = BeautifulSoup(res.content, features="xml")
            items = soup.find_all('item')
            
            choice = random.choice(items)
            title_en = choice.title.text
            link = choice.link.text

            if link not in yaddas:
                try:
                    title_az = translator_az.translate(title_en)
                    title_tr = translator_tr.translate(title_en)
                except:
                    title_az, title_tr = title_en, title_en
                
                photo_url = random.choice(sekil_kateqoriyalari)
                
                # Səliqəli 3 dilli format
                caption = (
                    f"🚀 **Engineering News / Mühəndislik Xəbəri**\n\n"
                    f"🇦🇿 **AZ:** {title_az}\n\n"
                    f"🇹🇷 **TR:** {title_tr}\n\n"
                    f"🇬🇧 **EN:** {title_en}\n\n"
                    f"🔗 [Read More / Oxu / Oku]({link})"
                )
                
                for qrup in QURUPLAR:
                    params = {'chat_id': qrup, 'photo': photo_url, 'caption': caption, 'parse_mode': 'Markdown'}
                    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendPhoto", data=params)
                
                yaddas.append(link)
                if len(yaddas) > 50: yaddas.pop(0)
                
                # Test üçün 10 saniyə elədim, xəbər gələndən sonra 12800 edərsən
                time.sleep(100)
            else:
                time.sleep(10)
        except Exception as e:
            time.sleep(20)

if __name__ == "__main__":
    xeber_paylas()
