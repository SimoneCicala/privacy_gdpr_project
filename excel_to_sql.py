import openpyxl  # Openpyxl è una libreria che permette di manipolare file Excel (.xlsx)
import sqlite3   # SQLite3 è una libreria per interagire con database SQLite

# Funzione che permette di leggere i dati da un file Excel
# Il nome del file è definito come parametro della funzione (default: "user_data.xlsx")
def read_from_excel(filename="user_data.xlsx"):
    # Caricamento del file Excel specificato
    # Il file viene aperto in modalità lettura
    workbook = openpyxl.load_workbook(filename)
    
    # Ottengo il foglio di lavoro attivo del file Excel
    # Nel nostro caso, si riferisce al primo (e unico) foglio di lavoro
    sheet = workbook.active

    # Inizializzo una lista vuota per contenere i dati letti dal file Excel
    data = []

    # Itero sulle righe del foglio, saltando la prima riga (intestazione)
    # 'min_row=2' fa partire la lettura dalla seconda riga del foglio
    # 'values_only=True' restituisce solo i valori delle celle, senza formati o metadati
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Salta l'intestazione
        data.append(row)  # Aggiungo la riga alla lista 'data'

    return data  # Ritorno la lista contenente tutte le righe lette dal foglio Excel

# Funzione che permette di creare una tabella nel database SQLite
# I dati da inserire nella tabella sono passati come parametro (data)
# Il nome del database è definito nel parametro della funzione (default: "user_data.db")
def create_sql_table(data, db_name="user_data.db"):
    # Connessione al database SQLite specificato
    conn = sqlite3.connect(db_name)
    
    # Creo un oggetto cursore per eseguire le operazioni SQL nel database
    cursor = conn.cursor()

    # Creazione della tabella 'utenti' nel database, se non esiste già
    # La tabella contiene 5 colonne: id, nome, cognome, email, telefono
    # Colonne id (si autoincrementa), nome, cognome, email, telefono
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utenti (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cognome TEXT,
            email TEXT,
            telefono TEXT
        )
    ''')

    # Inserimento dei dati nella tabella 'utenti'
    # 'executemany' permette di inserire più righe (dati) in una sola operazione
    cursor.executemany('''
        INSERT INTO utenti (nome, cognome, email, telefono)
        VALUES (?, ?, ?, ?)
    ''', data)  # I dati da inserire sono quelli letti dal file Excel

    # Salvo le modifiche effettuate nel database
    conn.commit()

    # Chiudo la connessione al database
    conn.close()

    # Stampo un messaggio di conferma dell'avvenuto inserimento dei dati
    print(f"Dati inseriti con successo nel database '{db_name}'.")

# Questo blocco viene eseguito solo se il file è eseguito come script principale
# Non verrà eseguito se il file è importato come modulo
if __name__ == "__main__":
    # Chiamo la funzione 'read_from_excel' per leggere i dati dal file Excel
    excel_data = read_from_excel()

    # Chiamo la funzione 'create_sql_table' per inserire i dati letti dal file Excel nel database
    create_sql_table(excel_data)
