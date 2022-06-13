import pytest

from droid import DroidSettings
from fraud_checker.routes import APP_ROUTES

pytest_plugins = 'droid.pytest_plugin'


@pytest.fixture
def droid_settings():
    return DroidSettings(routes=APP_ROUTES)
