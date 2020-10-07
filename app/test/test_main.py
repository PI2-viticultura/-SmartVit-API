
# Importamos a biblioteca de testes
import unittest


class TestHello(unittest.TestCase):

    def test_service_exist(self):
        self.assertTrue(5 == 5)


if __name__ == '__main__':
    unittest.main()
