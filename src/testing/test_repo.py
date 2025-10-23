import unittest
from testing import RepositoryRedis

repo = RepositoryRedis()

class TestTepo(unittest.TestCase):
    
    def redis_test_insert_dados_str(self):
        print('Teste inserção de dados string...')
        self.assertAlmostEqual(repo.insert('rash_teste', 'teste', '1'), True)
    
    def redis_test_insert_dados_int(self):
        print('Teste inserção de dados int...')
        self.assertAlmostEqual(repo.insert('rash_teste', 'teste', 1), True)
        
    def redis_teste_get_dados(self):
        print('testando get de dados....')
        repo.insert('teste_hash', 'teste', 'dado')
        chave_1 = {
            'teste': 'dado'
        }
        chave_2 = repo.get_hash_all('teste_hash')
        self.assertDictEqual(chave_1, chave_2, msg=None)
        
if __name__ == '__main__':
    unittest.main()