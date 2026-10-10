# Lab 012

Discover a hidden administrative endpoint with FFUF.

## Goal

Use content discovery to find an exposed admin panel that is not linked from the application.

## Run

```bash
git clone https://github.com/elisonkaloshi/labs-012.git
cd labs-012
chmod +x setup.sh
./setup.sh
source .venv/bin/activate
python app.py
```

Open:

```text
http://127.0.0.1:5012
```

Run FFUF against the application:

```bash
ffuf -u http://127.0.0.1:5012/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt
```

The important result is:

```text
admin
```

Open:

```text
http://127.0.0.1:5012/admin
```

The exposed admin panel returns:

```text
Secret: LAB-012-FFUF
```
