import pytest

from lesson_21.Homework17_Trofimenko.code_for_test2 import Ukranian_section

@pytest.fixture
def mymuseum() -> Ukranian_section:
    mymuseum = Ukranian_section()
    mymuseum.exhibit()
    yield mymuseum
