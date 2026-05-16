import yfinance as yf
import pandas as pd

print("Aksiyalar ma'lumotlari yuklanmoqda...")

# Apple (AAPL) kompaniyasining oxirgi 5 kunlik ma'lumotlarini soatbay yuklab olish
df = yf.download("AAPL", period="5d", interval="1h")

# Oddiy tahlil: Narx o'zgarishi foizini hisoblash
df['Change_%'] = (df['Close'] - df['Open']) / df['Open'] * 100

# Natijani terminalda ko'rish
print("\n--- Oxirgi olingan ma'lumotlar ---")
print(df[['Open', 'Close', 'Change_%']].tail())