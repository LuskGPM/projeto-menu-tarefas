import unittest
from ..src.backend import RepositoryRedis

repo = RepositoryRedis()

class TestRepoRedis(unittest.TestCase):
    
    def test_redis_insert_dados_str(self):
        print('Teste inserção de dados string...')
        self.assertAlmostEqual(repo.insert('rash_teste', 'teste', '1'), None)
    
    def test_redis_insert_dados_int(self):
        print('Teste inserção de dados int...')
        self.assertAlmostEqual(repo.insert('rash_teste', 'teste', 1), None)
        
    def test_redis_get_dados(self):
        print('testando get de dados....')
        repo.insert('teste_hash', 'teste', 'dado')
        chave_1 = {
            'teste': 'dado'
        }
        chave_2 = repo.get_hash_all('teste_hash')
        self.assertDictEqual(chave_1, chave_2, msg=None)

class TestRepoMySQL(unittest.TestCase):
    pass
