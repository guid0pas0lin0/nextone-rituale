import json, re
from langdetect import detect
from profanity_check import predict_prob

raw = json.load(open("data/confessions_raw.json"))
clean = json.load(open("data/confessions.json"))
rejected = []

for item in raw:
    text = item["text"][:280]
    if predict_prob([text])[0] > 0.7: 
        rejected.append({"id": item["id"], "reason": "profanity"})
        continue
    if re.search(r'\b(\+39|@[A-Za-z0-9_]+|https?://)\b', text):
        rejected.append({"id": item["id"], "reason": "pii/url"})
        continue
    item["text"] = text
    item["lang"] = detect(text)
    clean.append(item)

json.dump(clean, open("data/confessions.json","w"), ensure_ascii=False, indent=2)
open("data/confessions_raw.json","w").write("[]")
