import requests
import time
import random
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# --- RENDER PORT HİYLƏSİ (Botun sönməməsi üçün) ---
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Engineering Bot is Active!")

def run_server():
    try:
        server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
        server.serve_forever()
    except: pass

threading.Thread(target=run_server, daemon=True).start()

# --- MƏLUMATLAR ---
TOKEN = "8357425880:AAG-4PEylzM4aQb1RxEYbLdCDVE--KmaONg"
# Yeni ID-ni bura əlavə etdim
QURUPLAR = ["-1003772396405"] 

# PAYLAŞILAN XƏBƏRLƏRİN YADDAŞI
yaddas = []

translator_az = GoogleTranslator(source='en', target='az')
translator_tr = GoogleTranslator(source='en', target='tr')

# 50 Müxtəlif Şəkil Linki (Qısa olması üçün bura bir neçəsini qoyuram, sən hamısını saxlaya bilərsən)
sekil_kateqoriyalari = [
    "https://images.unsplash.com/photo-1485827404703-89b55fcc595e", "https://images.unsplash.com/photo-1518770660439-4636190af475",
    "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158", "https://images.unsplash.com/photo-1550751827-4bd374c3f58b"
]

def xeber_paylas():
    while True:
        try:
            # Google News-dan ən son mühəndislik xəbərlərini çəkirik
            url = "https://news.google.com/rss/search?q=engineering+technology+robotics+space&hl=en-US&gl=US&ceid=US:en"
            res = requests.get(url, timeout=20)
            soup = BeautifulSoup(res.content, features="xml")
            items = soup.find_all('item')
            
            # Xəbərləri qarışdırırıq ki, hər dəfə eyni sıra ilə yoxlamasın
            random.shuffle(items)
            
            tapildi = False
            for choice in items:
                link = choice.link.text
                
                # ƏGƏR BU LİNK YADDAŞDA YOXDURSA (Yəni yenidirsə):
                if link not in yaddas:
                    title_en = choice.title.text
                    
                    # Tərcümələr
                    try:
                        title_az = translator_az.translate(title_en)
                        title_tr = translator_tr.translate(title_en)
                    except:
                        title_az, title_tr = title_en, title_en
                    
                    photo_url = random.choice(sekil_kateqoriyalari)
                    
                    caption = (
                        f"🚀 **New Engineering Update**\n\n"
                        f"🇦🇿 **AZ:** {title_az}\n\n"
                        f"🇹🇷 **TR:** {title_tr}\n\n"
                        f"🇬🇧 **EN:** {title_en}\n\n"
                        f"🔗 [Read More]({link})"
                    )
                    
                    for qrup in QURUPLAR:
                        params = {'chat_id': qrup, 'photo': photo_url, 'caption': caption, 'parse_mode': 'Markdown'}
                        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendPhoto", data=params)
                    
                    # Bu linki yaddaşa əlavə et ki, bir daha paylaşmasın
                    yaddas.append(link)
                    if len(yaddas) > 100: yaddas.pop(0) # Son 100 xəbəri yadda saxla
                    
                    tapildi = True
                    print(f"Yeni xəbər paylaşıldı: {title_en}")
                    break # Bir dənə yeni xəbər paylaşdıqsa, dayan və gözləməyə keç
            
            if tapildi:
                # Yeni xəbər tapıldısa, növbəti xəbər üçün 2 saat (7200 saniyə) gözlə
                time.sleep(100) 
            else:
                # Yeni xəbər yoxdursa, 10 dəqiqə sonra yenidən yoxla
                print("Yeni xəbər tapılmadı, 10 dəqiqə gözlənilir...")
                time.sleep(600)
                
        except Exception as e:
            print(f"Xəta baş verdi: {e}")
            time.sleep(60)

if __name__ == "__main__":
    xeber_paylas()
