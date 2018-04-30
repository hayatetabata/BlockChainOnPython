from datetime import datetime
import hashlib
import json


class Blockchain():
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        genesis_block = self.create_block(nonce="", previous_hash="", transactions=[])
        self.chain.append(genesis_block)

    def create_block(self, nonce, previous_hash, transactions):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': datetime.now().strftime('%Y/%m/%d'),
            'transactions': transactions,
            'nonce': nonce,
            'previous_hash': previous_hash,
        }
        return block

    def add_block(self, block):
        self.chain.append(block)
        return self.chain

    def reset_current_transactions(self):
        self.current_transactions = []

    def add_transaction(self, transaction):
        self.current_transactions.append(transaction)
        return self.current_transactions

    def get_previous_block(self):
        return self.chain[-1]

    def find_nonce(self, previous_block, transactions):
        nonce = 0

        while True:
            if self.__is_valid_nonce(nonce, self.hash(previous_block), transactions):
                break
            nonce += 1

        return nonce

    def __is_valid_nonce(self, nonce, previous_hash, transactions):
        transactions_hash = ','.join(map(self.hash, transactions))
        hash_string = hashlib.sha256((previous_hash + transactions_hash + str(nonce)).encode()).hexdigest()
        if hash_string[:3] == '000':
            return True

        return False

    def hash(self, dict):
        hash_string = json.dumps(dict).encode()
        return hashlib.sha256(hash_string).hexdigest()
