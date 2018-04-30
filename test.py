from datetime import datetime
from Blockchain import Blockchain
import unittest


class BlockchainTest(unittest.TestCase):
    def test_create_block(self):
        nonce = 7
        previous_hash = '1A7CC8AEBDAFF51AC03199242D5DE20F60DF03983D5AC6CAA40270E3DB880484'
        transactions = self.__create_transactions()
        block = {
            'index': 2,
            'timestamp': datetime.now().strftime('%Y/%m/%d'),
            'transactions': transactions,
            'nonce': nonce,
            'previous_hash': previous_hash,
        }

        block_chain = Blockchain()
        result = block_chain.create_block(nonce, previous_hash, transactions)
        self.assertEquals(block, result)

    def test_add_block(self):
        index = 0
        nonce = 7
        previous_hash = '1A7CC8AEBDAFF51AC03199242D5DE20F60DF03983D5AC6CAA40270E3DB880484'
        transactions = self.__create_transactions()
        block = {
            'index': index + 1,
            'timestamp': datetime.now().strftime('%Y/%m/%d'),

            'transactions': transactions,
            'nonce': nonce,
            'previous_hash': previous_hash,
        }

        block_chain = Blockchain()
        result = block_chain.add_block(block)

        self.assertEquals(len(block_chain.chain), len(result))

    def test_find_nonce(self):
        index = 0
        nonce = 5852
        prev_nonce = 2
        prev_block_hash = '1A7CC8AEBDAFF51AC03199242D5DE20F60DF03983D5AC6CAA40270E3DB880484'
        prev_transactions = self.__create_transactions()
        new_transactions = self.__create_transactions()
        prev_block = {
            'index': index + 1,
            'timestamp': datetime.now().strftime('%Y/%m/%d'),
            'transactions': prev_transactions,
            'nonce': prev_nonce,
            'previous_hash': prev_block_hash,
        }

        block_chain = Blockchain()
        result = block_chain.find_nonce(prev_block, new_transactions)

        self.assertEquals(nonce, result)

    def test_hash(self):
        index = 0
        nonce = 7
        previous_hash = '1A7CC8AEBDAFF51AC03199242D5DE20F60DF03983D5AC6CAA40270E3DB880484'
        transactions = self.__create_transactions()

        block = {
            'index': index + 1,
            'timestamp': datetime.now().strftime('%Y/%m/%d'),
            'transactions': transactions,
            'nonce': nonce,
            'previous_hash': previous_hash,
        }
        expected = '7d781b5d02908753307fd235b4e969fb5acf14406bab54f7a771100b53fdf07d'

        block_chain = Blockchain()
        result = block_chain.hash(block)

        self.assertEquals(expected, result)

    def __create_transactions(self):
        transactions = [
            {
                'sender': 'C9835017E3A3B3DD8CFE5EF9074324273AE6D2683F039131A19756297A34F2A1',
                'recipient': '0CE0EFA846DB97FCDF0E31C6FD47BF5757558DF83AF583DDFFF1CA954BC86365',
                'amount': 12345,
            },
            {
                'sender': '0CE0EFA846DB97FCDF0E31C6FD47BF5757558DF83AF583DDFFF1CA954BC86365',
                'recipient': 'C9835017E3A3B3DD8CFE5EF9074324273AE6D2683F039131A19756297A34F2A1',
                'amount': 12345,
            }
        ]

        return transactions


if __name__ == '__main__':
    unittest.main()
