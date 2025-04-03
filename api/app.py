from flask import Flask, request, jsonify, render_template
from web3 import Web3
from flask_cors import CORS  # Import Flask-CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Connessione a Ganache
ganache_url = "http://192.168.1.26:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
assert web3.is_connected(), "Errore nella connessione a Ganache"

# Dati del contratto
contract_address = "0xFeeBbE8c0aA130CC8EbEB6981A721b8Ff2819dd0"

# Percorso del file JSON generato da Truffle
contract_json_path = os.path.join(os.path.dirname(__file__), '../build/contracts/RealEstateMarketplace.json')

# Caricamento dell'ABI dal file JSON
with open(contract_json_path, 'r') as file:
    contract_data = json.load(file)
    contract_abi = contract_data['abi']

# Creazione dell'istanza del contratto
contract = web3.eth.contract(address=contract_address, abi=contract_abi)


# Account predefinito (per test in locale)
default_account = web3.eth.accounts[0]

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/register_property', methods=['POST'])
def register_property():
    data = request.json
    tx_hash = contract.functions.registerProperty(
        data['description'],
        int(data['price'])
    ).transact({"from": default_account})

    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return jsonify({"status": "success", "tx_hash": tx_receipt.transactionHash.hex()})

@app.route('/buy_property/<int:property_id>', methods=['POST'])
def buy_property(property_id):
    data = request.json
    tx_hash = contract.functions.buyProperty(property_id).transact({
        "from": data['buyer_address'],
        "value": int(data['amount'])
    })

    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return jsonify({"status": "success", "tx_hash": tx_receipt.transactionHash.hex()})

@app.route('/properties', methods=['GET'])
def get_properties():
    properties = contract.functions.getProperties().call()
    property_list = []
    for prop in properties:
        if prop[0] != 0:  # Controlla che la proprietà esista
            property_list.append({
                "id": prop[0],
                "owner": prop[1],
                "description": prop[2],
                "price": prop[3],
                "isForSale": prop[4]
            })

    return jsonify(property_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
