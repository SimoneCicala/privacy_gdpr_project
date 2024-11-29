import config # Importo il file di configurazione

# Mi assicuro che tutte le variabili sono definite nel file di configurazione
assert hasattr(config, 'NUM_USERS'), "NUM_USERS non è definito in config.py"
assert hasattr(config, 'EXCEL_FILENAME'), "EXCEL_FILENAME non è definito in config.py"
assert hasattr(config, 'FAKER_LOCALE'), "FAKER_LOCALE non è definito in config.py"
assert hasattr(config, 'EXCEL_HEADERS'), "EXCEL_HEADERS non è definito in config.py"

from faker import Faker # Faker è una libreria che consente di generare dati casuali con diverse localizzazioni, nel nostro caso utilizzeremo la location it_IT
import openpyxl # Openpyxl è una libreria che permette di manipolare file Excel

# Funzione utilizzata per generare dati casuali per un certo numero di utenti.
# Il numero di utenti è definito nel file di configurazione
def generate_user_data(num_users=config.NUM_USERS):
    # Creazione dell'istanza Faker localizzata
    fake = Faker(config.FAKER_LOCALE)

    # Inizializzo una lista vuota che conterrà i dati generati per ogni utente
    user_data = []

    # Per generare dati casuali utilizzo un ciclo che farà n iterazioni quanti num_users sono stati definiti nel file di configurazione
    # Ad ogni iterazione andrà a generare 4 informazioni identificative di un utente: "Nome", "Cognome", "Email", "Telefono" e le andrà ad aggiungere alla lista precedentemente creata
    for _ in range(num_users):
        user = {
            "Nome": fake.first_name(), # Genera un nome casuale (in base alla location inserita all'inizializzazione del Faker)
            "Cognome": fake.last_name(), # Genera un cognome casuale (in base alla location inserita all'inizializzazione del Faker)
            "Email": fake.email(), # Genera un indirizzo email casuale (in base alla location inserita all'inizializzazione del Faker)
            "Telefono": fake.phone_number() # Genera un n°di telefono casuale (in base alla location inserita all'inizializzazione del Faker)
        }
        user_data.append(user)

    return user_data # Ritorna la lista

# Funzione che permette di salvare i dati dentro un file Excel.
# Il nome del file che verrà generato è definito nel file di configurazione
def save_to_excel(data, filename=config.EXCEL_FILENAME):
    # Utilizzo try catch per gestire gli eventuali errori in fase di generazione Excel (Esempio file aperto o permessi insufficienti)
    try: 
        # Creo un nuovo oggetto Workbook (foglio di lavoro Excel), in questo passo sto creando un file Excel
        workbook = openpyxl.Workbook()

        # Prendo il foglio di lavoro attivo. 
        # Nel nostro caso si riferirà al primo (che è anche l'unico).
        sheet = workbook.active 

        # Rinomino il foglio di lavoro in "Utenti"
        sheet.title = "Utenti"

        # Scrittura delle intestazioni, le intestazioni sono definite nel file di configurazione
        sheet.append(config.EXCEL_HEADERS)

        # Scrittura dei dati degli utenti, itero tutta la lista degli utenti generati e li inserisco nel file excel
        for user in data:
            sheet.append([user["Nome"], user["Cognome"], user["Email"], user["Telefono"]])

        # Salvataggio del file, in questo passaggio viene creato fisicamente il file sul disco
        workbook.save(filename)
    except Exception as e:
        print(f"Errore durante il salvataggio del file Excel: {e}")

# Verifico che il file è eseguito come script principale.
# Viene eseguito solo se è eseguito direttamente e non se è importato come modulo.
if __name__ == "__main__":
    users = generate_user_data() # Prendo la lista degli utenti generati tramite la funzione generate_user_data()
    save_to_excel(users) # Passo gli utenti generati alla funzione save_to_excel per inserirli nel file Excel