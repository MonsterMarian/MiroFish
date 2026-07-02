import json
import re
import sys

with open('locales/en.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

with open('locales/cs.json', 'r', encoding='utf-8') as f:
    cs_data = json.load(f)

def extract_placeholders(text):
    if not isinstance(text, str):
        return []
    return re.findall(r'\{[^}]+\}', text)

def fix_dict(en_d, cs_d):
    for k, v in en_d.items():
        if isinstance(v, dict):
            if k in cs_d and isinstance(cs_d[k], dict):
                fix_dict(v, cs_d[k])
        elif isinstance(v, str):
            en_ph = extract_placeholders(v)
            if en_ph:
                if k in cs_d and isinstance(cs_d[k], str):
                    cs_ph = extract_placeholders(cs_d[k])
                    if len(en_ph) != len(cs_ph) or any(a != b for a, b in zip(en_ph, cs_ph)):
                        cs_d[k] = v

fix_dict(en_data, cs_data)

with open('locales/cs.json', 'w', encoding='utf-8') as f:
    json.dump(cs_data, f, ensure_ascii=False, indent=2)

print("Fixed cs.json")
