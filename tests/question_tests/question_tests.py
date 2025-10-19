from src.question_a.question_a import is_prime

def test_is_prime_false():
    assert is_prime(4) == False

def test_is_prime_true_5():
    assert is_prime(5) == True

def test_is_prime_true_11():
    assert is_prime(11) == True

def test_is_prime_edge_cases():
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True

#test for question b 
from src.question_b import get_fahrenheit


def test_get_fahrenheit_zero():
    assert get_fahrenheit(0) == 32

def test_get_fahrenheit_five():
    assert get_fahrenheit(5) == 41

def test_get_fahrenheit_ten():
    assert get_fahrenheit(10) == 50

# test for question c 
from src.question_c.question_c import use_local_variable

def test_use_local_variable():
    num = 100
    use_local_variable(num)
    print(f"In test case after function call, num = {num}") 

    # test for question d
from src.question_d.get_miles_per_hour import get_miles_per_hour

def test_get_miles_per_hour():
    result = get_miles_per_hour(32, 60)
    assert round(result, 6) == 19.883872

    



