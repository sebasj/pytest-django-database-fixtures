import pytest

from django.conf import settings


@pytest.fixture
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': settings.BASE_DIR / 'db.sqlite3',
    }