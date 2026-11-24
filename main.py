import os

REPLY = "I'm on vacation. Your email was forwarded to my replacement, a cron job with abandonment issues and full access to my feelings."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(REPLY)
