import os
from dotenv import load_dotenv

# .env fayldan o'zgaruvchilarni yuklash
load_dotenv()

# Bot va API sozlamalari
BOT_TOKEN = os.getenv("BOT_TOKEN")
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")

# API-Football sozlamalari
FOOTBALL_API_URL = "https://v3.football.api-sports.io"
FOOTBALL_API_HEADERS = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': FOOTBALL_API_KEY
}

# Liga ID lari
LEAGUES = {
    'EPL': 39,      # Premier League
    'LALIGA': 140,  # La Liga
    'SERIA_A': 135, # Serie A
    'BUNDESLIGA': 78, # Bundesliga
    'LIGUE_1': 61,  # Ligue 1
}

# Xatolik xabarlari
ERROR_MESSAGES = {
    'API_ERROR': "Ma'lumot olishda xatolik yuz berdi. Iltimos, keyinroq urinib ko'ring.",
    'NO_DATA': "Ma'lumot topilmadi.",
    'NO_LIVE_MATCHES': "Hozirda jonli translyatsiya qilinayotgan o'yinlar yo'q."
}
