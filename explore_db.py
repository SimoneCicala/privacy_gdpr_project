import sqlite3  # SQLite3 è una libreria per interagire con database SQLite

# Connessione al database
# 'user_data.db' è il nome del file del database a cui ci connettiamo
conn = sqlite3.connect('user_data.db')

# Creazione di un cursore per eseguire le query SQL nel database
cursor = conn.cursor()

# Esegui una query per selezionare tutti i dati dalla tabella 'utenti'
# La query "SELECT * FROM utenti" recupera tutte le righe dalla tabella 'utenti'
cursor.execute("SELECT * FROM utenti")

# Recupera tutte le righe restituite dalla query eseguita
# 'fetchall()' restituisce una lista di tuple, ciascuna rappresentante una riga
rows = cursor.fetchall()

# Stampa i dati
# Itera su tutte le righe restituite dalla query
# Ogni 'row' è una tupla contenente i valori di una singola riga della tabella
for row in rows:
    print(row)  # Stampa ogni riga del risultato

# Chiudi la connessione al database
# Chiudiamo la connessione per liberare risorse
conn.close()
