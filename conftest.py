
import pytest


@pytest.fixture()
def navigation(page):
    page.goto("https://www.amazon.in")