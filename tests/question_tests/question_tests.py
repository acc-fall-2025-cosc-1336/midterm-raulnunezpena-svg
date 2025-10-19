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


