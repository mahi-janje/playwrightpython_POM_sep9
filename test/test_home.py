from playwright.sync_api import Page, expect
import pytest

@pytest.mark.smoke
def test_HomeScreenUI(page: Page,navigation):
    expect(page.get_by_role("link", name="Amazon.in")).to_be_visible()
    expect(page.get_by_role("searchbox", name="Search Amazon.in")).to_be_visible()
    page.get_by_role("link", name="items in cart").click()
    expect(page.get_by_role("link", name="items in cart")).to_be_visible()