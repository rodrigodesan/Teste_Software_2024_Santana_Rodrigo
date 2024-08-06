from atividade1.main import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        assert Calculator.sum(1,2) == 3
        assert Calculator.sum(2,5,7) == 14

    def test_substract(self):
        assert Calculator.substract(5,3) == 2
        assert Calculator.substract(5,3,2) == 0

    def test_multiply(self):
        assert Calculator.multiply(4,3) == 12
        assert Calculator.multiply(3,6,2) == 36

    def test_divide(self):
        assert Calculator.divide(10,2) == 5
        assert Calculator.divide(12,3,2) == 2


    # Stackoverflow answer, https://stackoverflow.com/questions/23337471/how-do-i-properly-assert-that-an-exception-gets-raised-in-pytest
    def test_divide_passes(self):
        with pytest.raises(Exception) as e_info:
            Calculator.divide(1,0)
        assert e_info.type == ZeroDivisionError

    def test_divide_passes_without_info(self):
        with pytest.raises(Exception):
            Calculator.divide(1,0)

    def test_divide_fails(self):
        with pytest.raises(Exception) as e_info:
            Calculator.divide(1,1)

    def test_divide_fails_without_info(self):
        with pytest.raises(Exception):
            Calculator.divide(1,1)

    # Don't do this. Assertions are caught as exceptions.
    def test_divide_passes_but_should_not(self):
        try:
            Calculator.divide(1,1)
            assert False
        except Exception:
            assert True

    # Even if the appropriate exception is caught, it is bad style,
    # because the test result is less informative
    # than it would be with pytest.raises(e)
    # (it just says pass or fail.)

    def test_divide_passes_but_bad_style(self):
        try:
            Calculator.divide(1,0)
            assert False
        except ZeroDivisionError:
            assert True

    def test_fails_but_bad_style(self):
        try:
            Calculator.divide(1,1)
            assert False
        except ZeroDivisionError:
            assert True
