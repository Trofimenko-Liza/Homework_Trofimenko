import pytest
from lesson_21.code_for_testing import Human

@pytest.mark.regression
def test_hair_colour_change():
    human = Human('Joshua', 18, 'Black')
    human.change_hair_colour('Blonde')
    assert human.colour == 'Blonde'

@pytest.mark.xfail(reason='Failed due to know bug', condition=True)
def test_growing(human, monkeypatch):
    monkeypatch.setattr(human, 'age', 60)
    human.grow()
    assert human.age == 61

@pytest.mark.skip('functional not implemented yet')
def test_growing2(human, monkeypatch):
    monkeypatch.setattr(human, 'age', 60)
    human.grow()
    assert human.age == 61

@pytest.mark.smoke
def test_hair_colour_change_01():
    human = Human('Joshua', 18, 'Black')
    human.change_hair_colour('Blonde')
    assert human.colour == 'Blonde'

@pytest.mark.smoke
@pytest.mark.regression
def test_hair_colour_change_02():
    human = Human('Joshua', 18, 'Black')
    human.change_hair_colour('Blonde')
    assert human.colour == 'Blonde'

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "new_colour, expected_colour", [("Red", "Red"), ("Green", "Green")]
)
def test_miltiple_colour_variations(human, new_colour, expected_colour):
    human.change_hair_colour(new_colour)
    assert human.colour == expected_colour

def test_change_colour_w_exeption(human):
    with pytest.raises(Exception):
        human.change_hair_colour("Brown")
