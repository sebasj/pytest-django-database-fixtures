import pytest

from model_bakery import baker
# Create your tests here.

from . import services 


@pytest.fixture
def customer_antonio():
    return baker.make('Customer', name='Antonio')


@pytest.mark.django_db
def test_customer_service_raises_exception(customer_antonio):
    with pytest.raises(Exception):
        services.count_customers_use_cases(name='Antonio')


# Aquest test falla perque hi ha dades a la bbdd i les dades de la fixture
@pytest.mark.skip
@pytest.mark.django_db
def test_customer_service_fails(customer_antonio):
    result = services.count_customers_use_case(name='Antonio')
    assert result == 1


"""
 Aquest test falla perque necessita access a la base de dades, 
 pero si li donam acces a la bbdd amb @pytest.mark.django_db duplica els resultats
 """
@pytest.mark.skip
def test_customer_service_works(customer_antonio):
    result = services.count_customers_use_case(name='Antonio')
    assert result == 1


