import requests


def test_universe():
    assert True


def test_another():
    assert 1 + 1 == 2


def test_2():
    assert 1 == 1


def test_up():
    assert requests.get('http://localhost:5050/up').text == 'Hello, World'
