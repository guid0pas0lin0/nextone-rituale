import json, re
raw = json.load(open("data/confessions_raw.json"))
clean = json.load(open("data/confessions.json"))
for item in raw:
    t = item.get("text","")[:280]
    if re.search(r'(https?://|@|#|\+39|\d{9,})', t): continue
    if len(t.strip())<5: continue
    clean.append({"id": item.get("id", len(clean)+1), "text": t})
json.dump(clean, open("data/confessions.json","w"), ensure_ascii=False, indent=2)
open("data/confessions_raw.json","w").write("[]")
print("Moderazione OK:", len(clean))
