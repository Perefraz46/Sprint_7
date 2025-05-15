import pytest
from methods.courier_methods import CourierMethods
from src.helpers import create_courier_data
from methods.order_methods import OrderMethods


@pytest.fixture()
def courier_data():
    payload = create_courier_data()
    yield payload


@pytest.fixture()
def courier_data_with_delete_courier(courier_data):
    yield courier_data
    login = courier_data['login']
    password = courier_data['password']
    cour_meth = CourierMethods()
    courier_id = cour_meth.courier_login(login, password).json()["id"]
    cour_meth.courier_delete(courier_id)


@pytest.fixture()
def courier_methods():
    yield CourierMethods()


@pytest.fixture()
def order_methods():
    yield OrderMethods()
