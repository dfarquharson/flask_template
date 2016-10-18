import requests
import pep8
import os


def test_universe():
    assert True


def test_pep8_compliance():
    assert len(pep8.StyleGuide()
               .check_files(filter(lambda x: x.endswith('.py'),
                            os.listdir('.')))
               .get_statistics()) == 0


def test_up():
    assert requests.get('http://localhost:5050/up').text == 'Hello, World'
