import pytest

from lesson_21.Homework17_Trofimenko.code_for_test2 import Ukranian_section
from lesson_21.Homework17_Trofimenko.code_for_test2 import Italian_section
from lesson_21.Homework17_Trofimenko.code_for_test2 import France_section

@pytest.mark.regression
def test_Add_Exhibit_Ukrainian_Section():
    uamuseum = Ukranian_section()
    uamuseum.add_new_exhibit()
    assert uamuseum.add_new_exhibit() == 'Kobzar Shevchenko'


@pytest.mark.smoke
def test_add_exhibit_Italian_section():
    itmuseum = Italian_section()
    itmuseum.add_new_exhibit()
    assert itmuseum.add_new_exhibit() == 'Sistine Madonna'


@pytest.mark.regression
@pytest.mark.smoke
def test_add_exhibit_france_section():
    frmuseum = France_section()
    frmuseum.add_new_exhibit()
    assert frmuseum.add_new_exhibit() == 'Victoire de Samothrace'

