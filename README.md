# Car Rental – Database Application

Jednoduchá konzolová aplikace v Pythonu pro správu půjčovny aut s databází Microsoft SQL Server.

---

## Požadavky

- Python 3.10 nebo novější
- Microsoft SQL Server (nebo LocalDB)
- ODBC Driver 17 for SQL Server
- Operační systém Windows

---

## Instalace

1. Naklonuj repozitář:
```bash
git clone https://github.com/MrToxc/Rental---Database-project-D1.git
cd car-rental
```

2. Nainstaluj potřebné knihovny:
```bash
pip install pyodbc
```

---

## Databáze

Databáze se vytváří manuálně v prostředí Microsoft SQL Server Management Studio (MSSQL).

1. Vytvoř databázi (např. `Rental`)
2. Otevři soubor:
```
databaseInit.sql
```
3. Spusť skript v MSSQL  
   (skript obsahuje kompletní DDL pro vytvoření databázového schématu)

---

## Konfigurace

V kořenovém adresáři projektu vytvoř soubor:

```
rental_config.json
```

Obsah souboru:
```json
{
  "driver": "{ODBC Driver 17 for SQL Server}",
  "server": "(localdb)\\MSSQLLocalDB",
  "database": "Rental",
  "uid": "Example_rental_user",
  "pwd": "ExamplePasswor"
}
```


---

## Spuštění aplikace

Automatizované testy pro kontrolu spusť příkazem:
```bash
python -m unittest discover -s Test\Unit -p "Test*.py" -t
```

Aplikaci spusť příkazem:
```bash
python App.py
```

Pokud je databáze správně vytvořena a konfigurace platná, aplikace se úspěšně připojí k databázi.

---

Import dat do databáze z CSV souborů spusť příkazem:
```bash
python Import.py
```

## Řešení problémů

- Aplikace se nespustí  
  Zkontroluj verzi Pythonu a nainstalované knihovny

- Chyba připojení k databázi  
  Ověř přihlašovací údaje v `rental_config.json`

- SQL chyba  
  Zkontroluj, zda byl správně spuštěn `databaseInit.sql`

---

## Licence

Projekt je určen výhradně pro školní a studijní účely.

---

## Autor

Václav Křivka  
SPŠE Ječná
