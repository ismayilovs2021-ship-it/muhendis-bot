import requests
import time
import random
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Sənin məlumatların
TOKEN = "8357425880:AAG-4PEylzM4aQb1RxEYbLdCDVE--KmaONg"
CHAT_ID = "-1003824053223"

yaddas = []
translator = GoogleTranslator(source='en', target='az')

sekil_kateqoriyalari = [
    "https://images.unsplash.com/photo-1485827404703-89b55fcc595e", 
    "https://images.unsplash.com/photo-1518770660439-4636190af475", 
    "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158", 
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b", 
    "https://images.unsplash.com/photo-1517077304055-6e89abbf09b0", 
    "https://images.unsplash.com/photo-1531297484001-80022131f5a1"
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
                # İngiliscə başlığı Azərbaycan dilinə tərcümə edirik
                try:
                    title_az = translator.translate(title_en)
                except:
                    title_az = title_en # Tərcümədə xəta olsa, ingiliscə qalsın
                
                photo_url = random.choice(sekil_kateqoriyalari)
                
                caption = f"🚀 **Yeni Mühəndislik Xəbəri**\n\n📌 {title_az}\n\n🔗 [Xəbəri oxu]({link})"
                
                params = {
                    'chat_id': CHAT_ID,
                    'photo': photo_url,
                    'caption': caption,
                    'parse_mode': 'Markdown'
                }
                
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendPhoto", data=params)
                
                yaddas.append(link)
                if len(yaddas) > 50: yaddas.pop(0)
                
                # Sənin qoyduğun 3.5 saatlıq vaxt
                time.sleep(120)
            else:
                time.sleep(30)
                
        except Exception as e:
            print(f"Xəta: {e}")
            time.sleep(60)

if __name__ == "__main__":
    xeber_paylas()
