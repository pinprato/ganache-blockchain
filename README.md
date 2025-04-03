# Real Estate Marketplace

Benvenuti nel progetto **Real Estate Marketplace**, un'applicazione decentralizzata (DApp) per la gestione di un marketplace immobiliare basata su Ethereum. Questo progetto utilizza **Flask** per il backend, **Web3.py** per interagire con la blockchain e **Truffle** per la gestione dei contratti intelligenti.

---

## Obiettivo del Progetto

L'obiettivo di questo progetto è creare un marketplace immobiliare decentralizzato in cui gli utenti possono:
1. Registrare proprietà immobiliari.
2. Visualizzare le proprietà disponibili.
3. Acquistare proprietà utilizzando Ether.

---

## Requisiti

Prima di iniziare, assicurati di avere i seguenti strumenti installati:

1. **Node.js** (versione >= 14.x) e **npm** (incluso con Node.js).
2. **Python** (versione >= 3.8).
3. **Ganache** (per creare una blockchain locale).
4. **Truffle** (per compilare e distribuire i contratti intelligenti).
5. **pip** (gestore di pacchetti Python).

---

## Configurazione del Server Ganache

Ganache sarà eseguito su un server dedicato con indirizzo IP `192.168.17.10`. Segui questi passaggi per configurarlo:

1. Scarica e installa **Ganache** dal sito ufficiale: [Ganache](https://trufflesuite.com/ganache/).
2. Avvia Ganache e configura una rete locale:
   - **Host**: `192.168.17.10`
   - **Porta**: `7545`

(PER QUESTO CORSO FAREMO GIRARE GANACHE SUL PC DEL PROFESSORE)
3. Copia l'indirizzo RPC di Ganache (`http://192.168.17.10:7545`) e assicurati che sia accessibile dalla rete.

---

## Installazione del Progetto

### 1. Clona il repository
Clona il progetto nella tua macchina locale:
```bash
git clone https://github.com/pinprato/RealEstateMarketplace.git
cd RealEstateMarketplace
```

### 2. Installa le dipendenze di Node.js

Installa npm:
```bash
sudo apt install npm
```

Installa **Truffle** globalmente:
```bash
npm install -g truffle
```

Installa le dipendenze del progetto:
```bash
npm install
```

### 3. Configura il backend Flask
Entra nella directory `api/`:
```bash
cd api
```

Crea un ambiente virtuale Python:
```bash
python -m venv venv
```

Attiva l'ambiente virtuale:
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

Installa le dipendenze Python:
```bash
pip install -r requirements.txt
```

---

## Configurazione del Progetto

### 1. Compila i contratti intelligenti
Compila i contratti Solidity con Truffle:
```bash
truffle compile
```

### 2. Distribuisci i contratti sulla blockchain locale
Distribuisci i contratti utilizzando Truffle:
```bash
truffle migrate --network development
```

---

## Avvio del Progetto

### 1. Avvia il server Flask
Dalla directory `api/`, esegui il server Flask:
```bash
python app.py
```

Il server sarà disponibile su `http://127.0.0.1:5000`.

### 2. Apri l'applicazione nel browser
Apri il browser e vai su:
```
http://127.0.0.1:5000
```

---

## Struttura del Progetto

```
RealEstateMarketplace/
├── api/
│   ├── app.py                # Backend Flask
│   ├── static/               # File statici (CSS, JS)
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── script.js
│   ├── templates/
│   │   └── index.html        # Frontend HTML
├── build/
│   └── contracts/            # ABI e dati dei contratti distribuiti
├── contracts/
│   └── RealEstateContract.sol # Contratto Solidity
├── migrations/
│   └── 1_deploy_contracts.js # Script di migrazione Truffle
├── test/
│   └── test.js               # Test dei contratti
├── truffle-config.js         # Configurazione Truffle
└── README.md                 # Documentazione del progetto
```

---

## Funzionalità Principali

1. **Registrazione di proprietà**:
   - Gli utenti possono registrare una nuova proprietà fornendo una descrizione e un prezzo.
   - La proprietà viene salvata nello smart contract e resa disponibile per la vendita.

2. **Acquisto di proprietà**:
   - Gli utenti possono acquistare una proprietà esistente fornendo l'ID della proprietà e l'importo richiesto.
   - La proprietà viene trasferita al nuovo proprietario e lo stato viene aggiornato.

3. **Visualizzazione delle proprietà**:
   - Gli utenti possono visualizzare un elenco di tutte le proprietà disponibili, inclusi dettagli come ID, proprietario, descrizione, prezzo e stato di vendita.

---

## Problemi Comuni

### 1. Flask non si avvia
- **Causa**: L'ambiente virtuale Python non è stato attivato o le dipendenze non sono state installate.
- **Soluzione**: Assicurati di aver attivato l'ambiente virtuale con:
  ```bash
  venv\Scripts\activate  # Su Windows
  source venv/bin/activate  # Su Mac/Linux
  ```

### 2. Errore di connessione a Ganache
- Verifica che Ganache sia in esecuzione sull'indirizzo `192.168.17.10` e sulla porta `7545`.
- Controlla che l'indirizzo del contratto in `app.py` corrisponda a quello distribuito da Truffle.

### 3. Problemi con i file statici
- Assicurati che i file CSS e JS siano nella directory `static/` e che i percorsi siano corretti in `index.html`.

---

## Documentazione del Progetto

Per una spiegazione dettagliata del progetto, inclusi i dettagli dello smart contract e del backend Flask, clicca sul pulsante qui sotto per espandere la documentazione completa.

<details>
<summary><strong>Leggi la documentazione completa</strong></summary>

### Real Estate Marketplace Documentation

Benvenuti nella documentazione del progetto **Real Estate Marketplace**. Questo progetto è un'applicazione decentralizzata (DApp) per la gestione di un marketplace immobiliare basata su Ethereum. Utilizza uno smart contract scritto in Solidity e un backend Flask per interagire con la blockchain tramite Web3.py.

---

### 1. Lo Smart Contract

#### 1.1 Struttura dello Smart Contract
Il file `RealEstateContract.sol` contiene il codice dello smart contract. Questo contratto gestisce:
- La registrazione di proprietà immobiliari.
- La vendita di proprietà.
- La visualizzazione delle proprietà disponibili.

#### 1.2 Componenti principali

##### 1.2.1 Struttura `Property`
La struttura `Property` rappresenta una proprietà immobiliare:
```solidity
struct Property {
    uint256 id;
    address payable owner;
    string description;
    uint256 price;
    bool isForSale;
}
```

##### 1.2.2 Variabili di Stato
Le seguenti variabili di stato sono utilizzate per gestire le proprietà:
```solidity
uint256 public propertyCount = 0;
mapping(uint256 => Property) public properties;
```

##### 1.2.3 Eventi
Gli eventi sono utilizzati per notificare le operazioni eseguite sullo smart contract:
```solidity
event PropertyRegistered(uint256 id, address owner, string description, uint256 price);
event PropertySold(uint256 id, address newOwner, uint256 price);
```

##### 1.2.4 Funzione `registerProperty`
La funzione `registerProperty` consente agli utenti di registrare una nuova proprietà:
```solidity
function registerProperty(string memory _description, uint256 _price) public {
    propertyCount++;
    properties[propertyCount] = Property(propertyCount, payable(msg.sender), _description, _price, true);
    emit PropertyRegistered(propertyCount, msg.sender, _description, _price);
}
```

##### 1.2.5 Funzione `buyProperty`
La funzione `buyProperty` consente agli utenti di acquistare una proprietà:
```solidity
function buyProperty(uint256 _id) public payable {
    Property storage property = properties[_id];
    require(property.isForSale, "La proprieta non e in vendita");
    require(msg.value >= property.price, "Importo insufficiente");

    property.owner.transfer(property.price);
    property.owner = payable(msg.sender);
    property.isForSale = false;

    emit PropertySold(_id, msg.sender, property.price);
}
```

##### 1.2.6 Funzione `getProperties`
La funzione `getProperties` consente di ottenere l'elenco delle proprietà disponibili per la vendita:
```solidity
function getProperties() public view returns (Property[] memory) {
    Property[] memory availableProperties = new Property[](propertyCount);
    uint256 counter = 0;
    for (uint256 i = 1; i <= propertyCount; i++) {
        if (properties[i].isForSale) {
            availableProperties[counter] = properties[i];
            counter++;
        }
    }
    return availableProperties;
}
```

---

### 2. Connessione a Ganache

Per connettersi a Ganache, utilizza il seguente codice nel backend Flask:
```python
ganache_url = "http://192.168.1.26:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
assert web3.is_connected(), "Errore nella connessione a Ganache"

# Indirizzo del contratto distribuito
contract_address = "0xFeeBbE8c0aA130CC8EbEB6981A721b8Ff2819dd0"

# Creazione dell'istanza del contratto
contract = web3.eth.contract(address=contract_address, abi=contract_abi)
```

---

### Contract Address

Il **contract address** è un indirizzo univoco sulla blockchain Ethereum che identifica uno smart contract distribuito. È simile a un indirizzo di un portafoglio Ethereum, ma invece di rappresentare un account personale, rappresenta uno smart contract.

---

#### 1. Cos'è il Contract Address?
- Quando uno smart contract viene distribuito sulla blockchain, viene generato un indirizzo univoco chiamato **contract address**.
- Questo indirizzo è utilizzato per interagire con lo smart contract, ad esempio per chiamare le sue funzioni o leggere i suoi dati.
- Il contract address è essenziale per creare un'istanza del contratto nell'app Flask utilizzando Web3.py.

---

#### 2. Dove trovare il Contract Address su Ganache?
Se stai utilizzando Ganache come blockchain locale, puoi trovare il contract address dopo aver distribuito lo smart contract. Ecco come fare:
1. Avvia Ganache e assicurati che sia configurato correttamente.
2. Dopo aver distribuito il contratto con Truffle (ad esempio, utilizzando il comando `truffle migrate`), apri la scheda **Transactions** in Ganache.
3. Cerca la transazione di tipo **Contract Deployment**. Questa transazione rappresenta la distribuzione dello smart contract.
4. Il contract address sarà visibile nella colonna **Contract Address** accanto alla transazione.

---

#### 3. Come viene creato il Contract Address?
Il contract address viene generato automaticamente dalla blockchain Ethereum quando uno smart contract viene distribuito. È calcolato utilizzando:
- L'indirizzo dell'account che distribuisce il contratto.
- Il numero di transazioni inviate da quell'account (noto come **nonce**).

Questo processo garantisce che ogni contract address sia univoco.

---

#### 4. A cosa serve il Contract Address?
Il contract address è fondamentale per interagire con lo smart contract. Serve per:
- **Creare un'istanza del contratto**: L'app Flask utilizza il contract address insieme all'ABI per creare un'istanza del contratto con Web3.py.
- **Chiamare funzioni del contratto**: Ogni chiamata o transazione verso lo smart contract richiede il contract address per sapere a quale contratto inviare la richiesta.
- **Identificare il contratto sulla blockchain**: Il contract address è utilizzato per monitorare le transazioni e gli eventi associati al contratto.

---

#### 5. Come utilizzare il Contract Address nell'app Flask?
Dopo aver ottenuto il contract address da Ganache, puoi aggiungerlo al file `app.py` per creare un'istanza del contratto. Ecco un esempio:

```python
# Indirizzo del contratto distribuito (ottenuto da Ganache)
contract_address = "0xFeeBbE8c0aA130CC8EbEB6981A721b8Ff2819dd0"

# Creazione dell'istanza del contratto
contract = web3.eth.contract(address=contract_address, abi=contract_abi)
```

---

### 3. Endpoint Flask

#### 3.1 Endpoint per registrare una proprietà
L'endpoint `/register_property` consente di registrare una nuova proprietà:
```python
@app.route('/register_property', methods=['POST'])
def register_property():
    data = request.json
    tx_hash = contract.functions.registerProperty(
        data['description'],
        int(data['price'])
    ).transact({"from": default_account})

    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return jsonify({"status": "success", "tx_hash": tx_receipt.transactionHash.hex()})
```

#### 3.2 Endpoint per acquistare una proprietà
L'endpoint `/buy_property/<int:property_id>` consente di acquistare una proprietà:
```python
@app.route('/buy_property/<int:property_id>', methods=['POST'])
def buy_property(property_id):
    data = request.json
    tx_hash = contract.functions.buyProperty(property_id).transact({
        "from": data['buyer_address'],
        "value": int(data['amount'])
    })

    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return jsonify({"status": "success", "tx_hash": tx_receipt.transactionHash.hex()})
```

Esempio di richiesta JSON per acquistare una proprietà:
```json
{
    "buyer_address": "0x1234567890abcdef1234567890abcdef12345678",
    "amount": 1000000000000000000
}
```

#### 3.3 Endpoint per visualizzare le proprietà
L'endpoint `/properties` consente di ottenere l'elenco delle proprietà disponibili:
```python
@app.route('/properties', methods=['GET'])
def get_properties():
    properties = contract.functions.getProperties().call()
    property_list = [
        {
            "id": 1,
            "owner": "0x1234567890abcdef1234567890abcdef12345678",
            "description": "Appartamento in centro",
            "price": 1000000000000000000,
            "isForSale": true
        },
        {
            "id": 2,
            "owner": "0xabcdefabcdefabcdefabcdefabcdefabcdef",
            "description": "Villa con piscina",
            "price": 5000000000000000000,
            "isForSale": false
        }
    ]
    return jsonify(property_list)
```

#### 3.4 Monitoraggio degli eventi
Per monitorare gli eventi di registrazione delle proprietà, utilizza il seguente codice:
```python
# Creazione di un filtro per l'evento PropertyRegistered
event_filter = contract.events.PropertyRegistered.createFilter(fromBlock="latest")

# Recupero di tutti gli eventi corrispondenti
events = event_filter.get_all_entries()

# Elaborazione degli eventi
for event in events:
    property_id = event["args"]["id"]
    owner = event["args"]["owner"]
    description = event["args"]["description"]
    price = event["args"]["price"]
    print(f"Nuova proprietà registrata: ID={property_id}, Proprietario={owner}, Descrizione={description}, Prezzo={price}")
```

---

### Interazione con l'ABI

L'ABI (Application Binary Interface) è un elemento fondamentale per l'interazione tra l'app Flask e lo smart contract distribuito sulla blockchain Ethereum. Di seguito viene spiegato come l'ABI viene utilizzato nel progetto.

---

#### 1. Cos'è l'ABI?
L'ABI è una rappresentazione JSON che descrive l'interfaccia pubblica dello smart contract. Include:
- Le funzioni disponibili nel contratto (con i loro nomi, parametri e tipi di ritorno).
- Gli eventi che il contratto può emettere.
- Le variabili di stato accessibili.

L'ABI è generato automaticamente da strumenti come **Truffle** durante la compilazione del contratto Solidity. Si trova nel file JSON corrispondente al contratto, ad esempio:  
`build/contracts/RealEstateMarketplace.json`.

---

#### 2. Caricamento dell'ABI
Nel file `app.py`, l'ABI viene caricato dal file JSON generato da Truffle. Questo passaggio è necessario per creare un'istanza del contratto che l'app Flask può utilizzare per interagire con la blockchain.

Esempio di codice:
```python
# Percorso del file JSON generato da Truffle
contract_json_path = os.path.join(os.path.dirname(__file__), '../build/contracts/RealEstateMarketplace.json')

# Caricamento dell'ABI dal file JSON
with open(contract_json_path, 'r') as file:
    contract_data = json.load(file)
    contract_abi = contract_data['abi']
```

#### 6. Riassunto

1. **L'ABI** è un'interfaccia che descrive come interagire con lo smart contract.
2. **Caricamento dell'ABI**: L'app Flask carica l'ABI dal file JSON generato da Truffle.
3. **Creazione dell'istanza del contratto**: L'ABI e l'indirizzo del contratto vengono utilizzati per creare un'istanza del contratto con Web3.py.
4. **Interazione con il contratto**:
   - **Chiamate di sola lettura**: Utilizzano `.call()` per ottenere dati senza modificare lo stato della blockchain.
   - **Transazioni**: Utilizzano `.transact()` per modificare lo stato della blockchain.
5. **Eventi**: L'app Flask può ascoltare gli eventi emessi dal contratto per reagire a determinate azioni.

L'ABI è essenziale per consentire all'app Flask di comunicare con lo smart contract in modo strutturato e sicuro.

---

#### 7. Monitoraggio degli eventi

Gli eventi emessi dallo smart contract possono essere monitorati utilizzando Web3.py. Questo è utile per rilevare azioni specifiche, come la registrazione di una nuova proprietà o la vendita di una proprietà.

##### 7.1 Cos'è un evento?
- Gli eventi sono definiti nello smart contract e vengono emessi quando si verificano determinate azioni.
- Gli eventi consentono di notificare i client (come l'app Flask) senza dover interrogare continuamente la blockchain.

##### 7.2 Come monitorare gli eventi?
Per monitorare gli eventi, è necessario creare un filtro utilizzando Web3.py. Ecco un esempio per monitorare l'evento `PropertyRegistered`:

```python
# Creazione di un filtro per l'evento PropertyRegistered
event_filter = contract.events.PropertyRegistered.createFilter(fromBlock="latest")

# Recupero di tutti gli eventi corrispondenti
events = event_filter.get_all_entries()

# Elaborazione degli eventi
for event in events:
    property_id = event["args"]["id"]
    owner = event["args"]["owner"]
    description = event["args"]["description"]
    price = event["args"]["price"]
    print(f"Nuova proprietà registrata: ID={property_id}, Proprietario={owner}, Descrizione={description}, Prezzo={price}")
```

---

## Come Usare le API nell'App

Questa sezione descrive come utilizzare le API disponibili nell'app Flask per interagire con lo smart contract.

---

### 1. Registrare una Proprietà
Invia una richiesta POST all'endpoint `/register_property` con il seguente payload JSON:

```json
{
    "description": "Appartamento in centro",
    "price": 1000000000000000000
}
```

### 2. Acquistare una Proprietà
Invia una richiesta POST all'endpoint `/buy_property/<property_id>` con il seguente payload JSON:

```json
{
    "buyer_address": "0x1234567890abcdef1234567890abcdef12345678",
    "amount": 1000000000000000000
}
```

### 3. visualizzare le Proprietà
Invia una richiesta POST all'endpoint `/property` con il seguente payload JSON:
```json
[
    {
        "id": 1,
        "owner": "0x1234567890abcdef1234567890abcdef12345678",
        "description": "Appartamento in centro",
        "price": 1000000000000000000,
        "isForSale": true
    },
    {
        "id": 2,
        "owner": "0xabcdefabcdefabcdefabcdefabcdefabcdef",
        "description": "Villa con piscina",
        "price": 5000000000000000000,
        "isForSale": false
    }
]
```

</details>
