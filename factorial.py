import unittest

def factorial(n):
    if n == 1:
        return 1
    resultado = n * factorial(n-1)
    return resultado
    

class TestFactorial(unittest.TestCase):
    def test_con_1(self):
        resultado = factorial(1)
        self.assertEqual(resultado, 1)

    def test_con_2(self):
        resultado = factorial(2)
        self.assertEqual(resultado, 2)

    def test_con_3(self):
        resultado = factorial(3)
        self.assertEqual(resultado, 6)
    
    def test_con_4(self):
        resultado = factorial(6)  # Cambiado de 4 a 6
        self.assertEqual(resultado, 720)  # El factorial de 6 es 720
    
    def test_con_5(self):
        resultado = factorial(8)  # Cambiado de 5 a 8
        self.assertEqual(resultado, 40320)  # El factorial de 8 es 40320
    
    def test_con_6(self):
        resultado = factorial(10)  # Cambiado de 6 a 10
        self.assertEqual(resultado, 3628800)  # El factorial de 10 es 3628800
    
    def test_con_7(self):
        resultado = factorial(12)  # Cambiado de 7 a 12
        self.assertEqual(resultado, 479001600)  # El factorial de 12 es 479001600
    


if __name__ == '__main__':
 unittest.main()
