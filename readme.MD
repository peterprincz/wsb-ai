## Ollama tepelitése
https://ollama.com/download
## Deepseek futtatása
`ollama run deepseek-r1:1.5b`
## Fejlesztői környezet
### Környezeti változó beállitása
reddit_password = TITOK
### Venv kialakitása
`python -m venv venv` (Csak ha még nincs)
`venv\Scripts\activate`
### Függöségek telepitése
`pip install -r requirements.txt`
## Tesztek futtatása
`python -m pytest test/${test_file}.py`