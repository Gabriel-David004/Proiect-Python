# Proiect-Python

# Proiectul ATM Console

## Prezentare Generală
Proiectul ATM Console este o simulare simplă a unui Bancomat (ATM) realizată în Python. Este format din două componente principale:

1. **Clasa `cardHolder`**: Definește structura și comportamentul unui utilizator al bancomatului, incluzând detalii despre cont și metode pentru gestionarea acestuia.
2. **Aplicația Console ATM**: Oferă o interfață simplistă pentru utilizator, cu opțiuni de depunere, retragere și verificare a soldului.

## Funcționalități
- Autentificare utilizator cu număr de card și PIN.
- Depunere de bani într-un cont.
- Retragere de bani cu validarea soldului disponibil.
- Verificarea soldului contului.

---

## Structura Proiectului
Proiectul este organizat în următoarele fișiere:

1. **`cardHolder.py`**: Conține clasa `cardHolder`.
   - Atribute: Numărul cardului, PIN-ul, prenumele, numele de familie și soldul contului.
   - Metode: Getteri, setteri și o metodă pentru afișarea detaliilor utilizatorului.

2. **`Project2(ATM Console).py`**: Scriptul principal al aplicației.
   - Gestionează intrările utilizatorului, afișarea meniului și interacțiunile cu clasa `cardHolder`.
   - Include date predefinite pentru utilizatori pentru testare.

---

## Pași pentru Începerea Utilizării

### Cerințe Preliminare
- Python 3.6 sau o versiune mai recentă instalată pe sistemul dumneavoastră.


## Instrucțiuni de Utilizare
1. Introduceți numărul cardului de debit atunci când vi se solicită. Dacă numărul cardului există în sistem, treceți la pasul următor.
2. Introduceți PIN-ul pentru autentificare.
3. După autentificare, alegeți din opțiunile disponibile:
   - Depunere de bani
   - Retragere de bani
   - Verificare sold
   - Ieșire
4. Urmați instrucțiunile afișate pentru a finaliza tranzacțiile.

---

## Exemplu de Output
```
Please insert your debit card: 1234567
Please enter your pin: 1234
Welcome Gabriel
Please choose from one of the following options...
1. Deposit
2. Withdraw
3. Show Balance
4. Exit
```

---

## Documentație Cod

### Clasa `cardHolder` (`cardHolder.py`)
Clasa `cardHolder` reprezintă un utilizator și oferă metode pentru gestionarea contului acestuia. Mai jos este un rezumat al caracteristicilor sale:

- **Atribute**:
  - `cardNum` (str): Numărul cardului.
  - `pin` (int): PIN-ul pentru autentificare.
  - `firstName` (str): Prenumele utilizatorului.
  - `lastName` (str): Numele de familie al utilizatorului.
  - `balance` (float): Soldul curent al contului.

- **Metode**:
  - `get_*` și `set_*`: Metode pentru accesarea și modificarea atributelor.
  - `printOut()`: Afișează toate detaliile utilizatorului.

### Consola ATM (`Project2(ATM Console).py`)
Scriptul principal al aplicației gestionează interacțiunile și operațiunile utilizatorului.

- **Funcții**:
  - `printMenu()`: Afișează opțiunile meniului.
  - `deposit(cardHolder)`: Gestionează depunerile de bani.
  - `withdraw(cardHolder)`: Gestionează retragerile de bani.
  - `check_balance(cardHolder)`: Afișează soldul utilizatorului.

- **Flux**:
  - Solicită numărul cardului și PIN-ul.
  - Autentifică utilizatorul.
  - Oferă un meniu cu opțiuni de tranzacții.

