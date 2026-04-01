import requests
import time
import random
from bs4 import BeautifulSoup

# Sənin məlumatların
TOKEN = "8357425880:AAG-4PEylzM4aQb1RxEYbLdCDVE--KmaONg"
CHAT_ID = "-1003824053223"

yaddas = []

def xəbər_tap_və_paylaş():
    while True:
        try:
            # Google News-dan mühəndislik xəbərləri (Whitelisted mənbə)
            url = "https://news.google.com/rss/search?q=engineering+technology&hl=en-US&gl=US&ceid=US:en"
            cavab = requests.get(url, timeout=20)
            sup = BeautifulSoup(cavab.content, features="xml")
            maddələr = sup.find_all('item')
            
            secilen = random.choice(maddələr)
            basliq = secilen.title.text
            link = secilen.link.text

            if link not in yaddas:
                mesaj = f"🚀 **Yeni Mühəndislik Xəbəri**\n\n📌 {basliq}\n\n🔗 [Xəbərə keçid]({link})"
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                              data={'chat_id': CHAT_ID, 'text': mesaj, 'parse_mode': 'Markdown'})
                
                yaddas.append(link)
                if len(yaddas) > 50: yaddas.pop(0)
                
                # Yoxlanış üçün: 120 saniyə (2 dəqiqə) gözləyir
                gozleme = 120
                print(f"Xəbər paylaşıldı. 2 dəqiqə gözlənilir...")
                time.sleep(gozleme)
            else:
                time.sleep(60) # Eyni xəbərdirsə, 1 dəqiqə gözlə yenisinə bax
        except Exception as e:
            print(f"Xəta: {e}")
            time.sleep(60)

if __name__ == "__main__":
    xəbər_tap_və_paylaş()
