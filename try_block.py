from Blockchain import Blockchain
import unittest


class ExecutionBlockChain(unittest.TestCase):
    def test_block_chain(self):
        transaction1 = {
            "data": 'Transaction data 1'
        }
        transaction2 = {
            "data": 'Transaction data 2'
        }
        transaction3 = {
            "data": 'Transaction data 3'
        }
        transaction4 = {
            "data": 'Transaction data 4'
        }

        '''トランザクションを追加。ここで様々な取引が行われる'''
        blockchain = Blockchain()

        blockchain.add_transaction(transaction1)
        blockchain.add_transaction(transaction2)
        blockchain.add_transaction(transaction3)
        blockchain.add_transaction(transaction4)

        '''ここからはBlockを作成する'''
        previous_block = blockchain.get_previous_block()

        '''まずはnonceの発見から'''
        previous_hash = blockchain.hash(previous_block)
        current_transactions = blockchain.current_transactions
        nonce = blockchain.find_nonce(previous_hash, current_transactions)

        '''nonceが見つかったので、それを元に新しいブロックを作る'''
        new_block = blockchain.create_block(nonce,
                                            previous_hash,
                                            current_transactions)

        '''トランザクションでブロックを作ったので、リセットをかける'''
        blockchain.reset_current_transactions()

        '''生成されたブロックを追加'''
        blockchain.add_block(new_block)

        self.assertEquals(len(blockchain.current_transactions), 0)
        self.assertEquals(len(blockchain.chain), 2)


if __name__ == '__main__':
    unittest.main()
