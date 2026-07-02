import json
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='en', target='cs')

def translate_dict(d):
    translated = {}
    for k, v in d.items():
        if isinstance(v, dict):
            translated[k] = translate_dict(v)
        elif isinstance(v, str):
            try:
                # avoid translating template strings like {{name}} if possible, but deep-translator might mess them up.
                # Since it's a simple translation, we'll just translate and let it be for now, 
                # but let's be careful.
                translated[k] = translator.translate(v)
            except Exception as e:
                print(f"Error translating '{v}': {e}")
                translated[k] = v
        else:
            translated[k] = v
    return translated

print("Reading en.json...")
with open('locales/en.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

print("Translating...")
cs_data = translate_dict(en_data)

print("Writing cs.json...")
with open('locales/cs.json', 'w', encoding='utf-8') as f:
    json.dump(cs_data, f, ensure_ascii=False, indent=2)

print("Updating languages.json...")
with open('locales/languages.json', 'r', encoding='utf-8') as f:
    langs = json.load(f)

langs['cs'] = {
    "label": "Čeština",
    "llmInstruction": "Odpovídejte prosím česky."
}

with open('locales/languages.json', 'w', encoding='utf-8') as f:
    json.dump(langs, f, ensure_ascii=False, indent=2)

print("Done.")
