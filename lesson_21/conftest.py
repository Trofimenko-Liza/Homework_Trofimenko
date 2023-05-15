import pytest

from lesson_21.code_for_testing import Human

@pytest.fixture
def human() -> Human:
    #print('we are in setup')
    human = Human('Alex', 30, 'Black')
    human.grow()
    yield human
