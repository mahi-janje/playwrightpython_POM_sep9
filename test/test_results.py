from playwright.sync_api import Page, expect
import pytest

@pytest.mark.smoke
def test_resultsScreenUI(page: Page,navigation):
    page.goto("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    page.get_by_role("searchbox", name="Search Amazon.in").fill("iphone")
    page.get_by_role("searchbox", name="Search Amazon.in").press("Enter")
    page.get_by_role("button", name="Go", exact=True).click()
    expect(page.get_by_role("heading", name="Results", exact=True)).to_be_visible()
    expect(page.get_by_text("Eligible for Free Delivery")).to_be_visible()