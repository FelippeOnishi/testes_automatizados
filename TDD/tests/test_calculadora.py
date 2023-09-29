from src.calculadora import Calculadora


class Test_Calculadora:

    def test_adicao(self):
        resultado = Calculadora.adicao(2, 3)
        assert resultado == 5

    def test_adicao2(self):
        resultado = Calculadora.adicao(2 , 5)
        assert resultado == 7

    def test_divisao(self):
        resultado = Calculadora.divisao(2 , 2)
        assert resultado == 1

    def test_divisao2(self):
        resultado = Calculadora.divisao(6, 0)
        assert resultado == 'Erro'

    def test_multi(self):
        resultado = Calculadora.multiplicacao(2, 4)
        assert resultado == 8