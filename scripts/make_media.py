import json, os, subprocess, textwrap, random

conf = json.load(open("data/confessions.json"))[-10:]
bg = random.choice(os.listdir("media/backgrounds"))
os.makedirs("media/out", exist_ok=True)

for c in conf:
  sid = c["id"]
  # Genera SRT (sottotitoli) – niente TTS per restare leggerissimi
  srt = f"1\n00:00:00,000 --> 00:00:09,000\n{c['text']}\n"
  open(f"media/out/{sid}.srt","w").write(srt)
  # Video 9:16 10s con drawtext (fallback se srt non supportato)
  cmd = f"""ffmpeg -y -loop 1 -i media/backgrounds/{bg} -t 10 \
  -vf "scale=1080:1920, drawtext=fontsize=48:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:text='{c['text'].replace("'","’")[:120]}'" \
  -c:v libx264 -pix_fmt yuv420p media/out/{sid}.mp4"""
  subprocess.run(cmd, shell=True, check=True)
