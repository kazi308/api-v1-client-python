import unittest
from blockchain.blockexplorer import *


class TestGetAddress(unittest.TestCase):
    def test_getAddressByBase58(self):
        address = get_address('1jH7K4RJrQBXijtLj1JpzqPRhR7MdFtaW')
        self.assertEqual('1jH7K4RJrQBXijtLj1JpzqPRhR7MdFtaW', address.address)
        self.assertEqual('07feead7f9fb7d16a0251421ac9fa090169cc169', address.hash160)
        self.assertEqual(0, address.final_balance)
        self.assertEqual(2, address.n_tx)
        self.assertEqual(20000, address.total_received)
        self.assertEqual(20000, address.total_sent)
        self.assertEqual(2, len(address.transactions))

    def test_getAddressByHash160(self):
        address = get_address('07feead7f9fb7d16a0251421ac9fa090169cc169')
        self.assertEqual('1jH7K4RJrQBXijtLj1JpzqPRhR7MdFtaW', address.address)
        self.assertEqual('07feead7f9fb7d16a0251421ac9fa090169cc169', address.hash160)
        self.assertEqual(0, address.final_balance)
        self.assertEqual(2, address.n_tx)
        self.assertEqual(20000, address.total_received)
        self.assertEqual(20000, address.total_sent)
        self.assertEqual(2, len(address.transactions))

    def test_getAddressWithFilter(self):
        address = get_address('07feead7f9fb7d16a0251421ac9fa090169cc169', filter=4)
        self.assertEqual('1jH7K4RJrQBXijtLj1JpzqPRhR7MdFtaW', address.address)
        self.assertEqual('07feead7f9fb7d16a0251421ac9fa090169cc169', address.hash160)
        self.assertEqual(0, address.final_balance)
        self.assertEqual(2, address.n_tx)
        self.assertEqual(20000, address.total_received)
        self.assertEqual(20000, address.total_sent)
        self.assertEqual(2, len(address.transactions))

    def test_getAddressWithLimit(self):
        address = get_address('07feead7f9fb7d16a0251421ac9fa090169cc169', limit=1)
        self.assertEqual('1jH7K4RJrQBXijtLj1JpzqPRhR7MdFtaW', address.address)
        self.assertEqual('07feead7f9fb7d16a0251421ac9fa090169cc169', address.hash160)
        self.assertEqual(0, address.final_balance)
        self.assertEqual(2, address.n_tx)
        self.assertEqual(20000, address.total_received)
        self.assertEqual(20000, address.total_sent)
        self.assertEqual(1, len(address.transactions))

    def test_getAddressWithOffset(self):
        address = get_address('07feead7f9fb7d16a0251421ac9fa090169cc169', offset=1)
        self.assertEqual('1jH7K4RJrQBXijtLj1JpzqPRhR7MdFtaW', address.address)
        self.assertEqual('07feead7f9fb7d16a0251421ac9fa090169cc169', address.hash160)
        self.assertEqual(0, address.final_balance)
        self.assertEqual(2, address.n_tx)
        self.assertEqual(20000, address.total_received)
        self.assertEqual(20000, address.total_sent)
        self.assertEqual(1, len(address.transactions))


class TestGetXpub(unittest.TestCase):
    def test_getXpub(self):
        xpub = get_xpub('xpub6CmZamQcHw2TPtbGmJNEvRgfhLwitarvzFn3fBYEEkFTqztus7W7CNbf48Kxuj1bRRBmZPzQocB6qar9ay6buVkQk73ftKE1z4tt9cPHWRn')
        self.assertEqual('xpub6CmZamQcHw2TPtbGmJNEvRgfhLwitarvzFn3fBYEEkFTqztus7W7CNbf48Kxuj1bRRBmZPzQocB6qar9ay6buVkQk73ftKE1z4tt9cPHWRn', xpub.address)
        self.assertEqual(20000, xpub.final_balance)
        self.assertEqual(1, xpub.n_tx)
        self.assertEqual(20000, xpub.total_received)
        self.assertEqual(0, xpub.total_sent)
        self.assertEqual(1, len(xpub.transactions))
        self.assertEqual(0, xpub.change_index)
        self.assertEqual(1, xpub.account_index)
        self.assertEqual(20, xpub.gap_limit)


if __name__ == '__main__':
    unittest.main()
