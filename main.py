import os
import shutil
import json
from datetime import datetime

folder = os.path.expanduser('~/Downloads')
log_name = 'sort_log.txt'

def add_to_log(msg):
    now = datetime.now().strftime("%H:%M")
    f = open(log_name, 'a', encoding='utf-8')
    f.write(f"[{now}] {msg}\n")
    f.close()

try:
    with open('config.json', 'r') as f:
        cfg = json.load(f)
except:
    cfg = {"Images": [".jpg", ".png"], "Docs": [".pdf", ".docx"]}
    add_to_log("No config, using defaults")

if not os.path.exists(folder):
    print("Folder not found")
    exit()

count = 0
for item in os.listdir(folder):
    full_path = os.path.join(folder, item)
    
    if os.path.isdir(full_path) or item in [log_name, 'config.json']:
        continue
        
    ext = os.path.splitext(item)[1].lower()

    for target_dir, exts in cfg.items():
        if ext in exts:
            dest = os.path.join(folder, target_dir)
            
            if not os.path.exists(dest):
                os.makedirs(dest)
            
            try:
                shutil.move(full_path, os.path.join(dest, item))
                add_to_log(f"Moved {item} to {target_dir}")
                count += 1
            except:
                add_to_log(f"Fail: {item}")
            break

add_to_log(f"XxX Done. Files relocated: {count}\n XxX")