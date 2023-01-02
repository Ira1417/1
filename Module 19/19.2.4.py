from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator
        
    def test_multipily_positive(self):
        assert self.calc.multipily(self, 5, 5) == 25

    def test_division_positive(self):
        assert self.calc.division(self, 15, 5) == 3

    def test_subtraction_positive(self):
        assert self.calc.subtraction(self, 7, 2) == 5

    def test_adding_positive(self):
        assert self.calc.adding(self, 3, 10) == 13

    def teardown(self):
        print('Выполнение метода Teardown')
