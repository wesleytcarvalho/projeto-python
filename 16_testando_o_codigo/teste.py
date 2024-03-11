import unittest
from atividades import comer, dormir


class AtividadesTestes(unittest.TestCase):
    
    def test_comer_saudavel(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma'
        )

    def test_nao_sauldavel(self):
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza.'
        )

    def test_dormindo_pouco(self):
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormi por 4 horas. :('
        )

    def test_dormi_muito(self):
        self.assertEqual(
            dormir(8),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )


if __name__ == '__main__':
    unittest.main()