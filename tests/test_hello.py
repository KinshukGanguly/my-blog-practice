from hello import greet


def test_greet():
    assert greet("Kinshuk_default") == "Hello, Kinshuk_default!"
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"
    assert greet("") == "Hello, !"
    assert greet("123") == "Hello, 123!"