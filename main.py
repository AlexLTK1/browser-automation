
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page1 = context.new_page()
    page1.close()
    page.goto("https://neetcode.io/courses")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Cancel").click()
    page.locator(".card-img").first.click()
    page.frame_locator("iframe").get_by_role("button", name="Play").click()
    page.frame_locator("iframe").get_by_role("button", name="Pause").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)