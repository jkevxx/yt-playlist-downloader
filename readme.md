# Donwload music of YouTube

Here are the clear steps to **pull a Python project on another machine** and set it up properly with the virtual environment.

---

## 1. Clone the repository from GitHub

Open a terminal in the new machine and run:

```bash
git clone https://github.com/jkevxx/yt-playlist-downloader.git
```

Then go inside the folder:

```bash
cd yt-playlist-downloader
```

---

## 2. Create a virtual environment

Create a new virtual environment (never copy the one from the original machine):

```bash
python3 -m venv venv
```

or Windows:

```bash
py -m venv venv
```

---

## 3. Activate the virtual environment

**macOS/Linux:**

```bash
source venv/bin/activate
```

**Windows (cmd):**

```bash
venv\Scripts\activate
```

**Windows (PowerShell):**

```bash
.\venv\Scripts\Activate.ps1
```

---

## 4. Install dependencies from `requirements.txt`

```bash
pip install -r requirements.txt
```

This recreates the environment exactly as it was on the original machine.

---

## 5. Run the project

```bash
# JSON file creation
python main.py
```

or:

```bash
# Download music from JSON file
python download_from_json.py.py
```
