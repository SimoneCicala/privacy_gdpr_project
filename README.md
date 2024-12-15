# Privacy e sicurezza aziendale: il ruolo del GDPR nella gestione dei dati personali con applicazioni pratiche in Python

Questo progetto simula la gestione dei dati personali in conformità con il GDPR (Regolamento Generale sulla Protezione dei Dati). Il sistema genera dati casuali per utenti, li salva in un file Excel e li trasferisce in un database SQLite.

## Per iniziare

1. **Configurazione**:
   - Modifica il file `config.py` per impostare il numero di utenti da generare, il nome del file Excel, e altre impostazioni.

2. **Generazione dei dati**:
   - Esegui `generate_data.py` per generare i dati degli utenti e salvarli in un file Excel.

3. **Trasferimento dei dati al db**:
   - Esegui `excel_to_sql.py` per caricare i dati dal file Excel nel database SQLite.

4. **Interrogazione del db**:
   - Utilizza `explore_db.py` esegue una select * sulla tabella utenti e ritorna il risultato 
   - Utilizza `db_manager.py` per eseguire query sul database e cercare utenti per nome/cognome/email/telefono.

## Requisiti

- `openpyxl` per la gestione dei file Excel.
- `sqlite3` (integrato in Python) per la gestione del database SQLite.
- `Faker` per la generazione di dati casuali.

## Installazione delle dipendenze

Installa le dipendenze con:

```bash
pip install -r requirements.txt

Se dovessero essere riscontrati errori nell'installazione delle dipendenze aggiungere come parametro --break-system-packages