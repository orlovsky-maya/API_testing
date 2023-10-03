import pytest


@pytest.fixture()
def set_up():
    print('SET_UP')
    yield
    print('EXIT')


@pytest.fixture(scope='module')
def start_finish():
    print('START')
    yield
    print('FINISH')
