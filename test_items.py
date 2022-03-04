import time
def test_button_add_to_basket(browser):
    time.sleep(30)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert button != [], '"Add to cart" button not found'

