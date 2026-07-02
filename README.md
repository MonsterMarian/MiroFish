# MiroFish 🐟

MiroFish je interaktivní open-source aplikace pro simulaci a analýzu ontologií, grafů znalostí (GraphRAG) a komplexních systémů. Pomocí umělé inteligence dokáže automaticky extrahovat entity a vztahy z vašich dokumentů a vizualizovat je v reálném čase.

Tato verze obsahuje podporu pro **český jazyk** a moderní **Dark Mode** (tmavý režim).

## Předpoklady

K plnému běhu aplikace potřebujete dvě hlavní věci:
1. **Node.js** (pro frontend)
2. **Python 3.10+** (pro backend)
3. **Zep API klíč** (pro grafové operace)

### Jak získat Zep API klíč

Aplikace využívá pro sestavování grafu znalostí službu Zep Cloud. 
Zde je návod, jak zdarma získat API klíč:
1. Přejděte na stránku [Zep Cloud (app.getzep.com)](https://app.getzep.com/).
2. Vytvořte si účet (nebo se přihlaste, např. přes Google nebo GitHub).
3. V administraci (Dashboard) klikněte na záložku **API Keys**.
4. Vygenerujte si nový API klíč a zkopírujte jej.
5. Zkopírovaný klíč následně vložíte ve frontendové aplikaci v **Kroku 02: Sestavení GraphRAG**, konkrétně do pole pro ZEP API KEY, případně ho uložte do souboru `.env` v backendu jako `ZEP_API_KEY=z_váš_vygenerovaný_klíč`.

## Instalace a spuštění

### 1. Spuštění Backendu
Otevřete terminál a přejděte do složky `backend`:
```bash
cd backend
python -m venv .venv
# Aktivace virtuálního prostředí:
# Windows:
.venv\Scripts\activate
# Mac/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
python run.py
```
Backend standardně běží na portu `5001`.

### 2. Spuštění Frontendu
Otevřete nový terminál a přejděte do složky `frontend`:
```bash
cd frontend
npm install
npm run dev
```
Frontend bude dostupný na `http://localhost:3000`.

## Novinky v této verzi
- **Lokalizace:** Přidána plná podpora češtiny.
- **Vzhled:** Prémiový tmavý režim (Dark Mode) s lepší čitelností a moderními barvami.
- **Opravy:** Stabilnější napojení na Zep Cloud Graph API.