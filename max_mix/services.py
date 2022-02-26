
# Create your views here.

from . import models

def count_customers_use_case(name):
    result = models.Customer.objects.filter(name=name).count()

    if result > 1:
        raise Exception('Only one customer!')
    
    return result