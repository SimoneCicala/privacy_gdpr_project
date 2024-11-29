import sqlite3  # SQLite3 è una libreria per interagire con database SQLite

# Classe che gestisce la connessione e le operazioni sul database
class DatabaseManager:
    def __init__(self, db_name):
        """Inizializza la connessione al database."""
        # Inizializza il nome del database
        self.db_name = db_name

        # Connessione al database specificato dal nome
        self.conn = sqlite3.connect(self.db_name)

        # Creazione di un cursore per eseguire le query SQL
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        """Esegue una query SQL con parametri opzionali."""
        try:
            # Se sono presenti parametri, esegue la query con i parametri passati
            if params:
                self.cursor.execute(query, params)
            else:
                # Altrimenti esegue la query senza parametri
                self.cursor.execute(query)

            # Restituisce tutti i risultati della query eseguita
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            # Se c'è un errore durante l'esecuzione della query, stampa l'errore
            print(f"Errore nell'esecuzione della query: {e}")
            return []  # Restituisce una lista vuota in caso di errore

    def close_connection(self):
        """Chiude la connessione al database."""
        # Chiude la connessione al database
        self.conn.close()

# Questo blocco viene eseguito solo se il file è eseguito come script principale
# Non verrà eseguito se il file è importato come modulo
if __name__ == "__main__":
    # Nome del database da utilizzare
    db_name = "user_data.db"

    # Inizializzazione della classe DatabaseManager per gestire il database
    db_manager = DatabaseManager(db_name)

    # Messaggio di benvenuto per l'utente
    print("Benvenuto! Puoi cercare utenti per Nome o Cognome.")

    # Richiedi all'utente di inserire il campo da cercare (nome o cognome)
    search_field = input("Inserisci il campo da cercare (nome/cognome): ").lower()

    # Richiedi all'utente di inserire il valore da cercare per il campo selezionato
    search_value = input(f"Inserisci il valore da cercare per {search_field}: ")

    # Controlla se il campo inserito è valido
    if search_field in ["nome", "cognome"]:
        # Costruisci la query per cercare nel campo selezionato (nome o cognome)
        query = f"SELECT * FROM utenti WHERE {search_field} LIKE ?"

        # Esegui la query con il valore di ricerca inserito dall'utente
        results = db_manager.execute_query(query, (f"%{search_value}%",))

        # Mostra i risultati trovati
        if results:
            print("\nRisultati trovati:")
            for row in results:
                print(row)  # Stampa ogni risultato trovato
        else:
            print("Nessun risultato trovato.")  # Messaggio se non sono stati trovati risultati
    else:
        # Messaggio di errore se il campo non è valido (né "nome" né "cognome")
        print("Campo non valido. Usa 'nome' o 'cognome'.")

    # Chiudi la connessione al database
    db_manager.close_connection()
