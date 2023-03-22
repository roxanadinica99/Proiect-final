from browser import Browser
from pages.main_page import Main_Page
from pages.products_page import Products_page


def before_all(context):
    context.browser = Browser()
    context.main_page_object = Main_Page()
    context.products_page_object = Products_page()


def after_all(context):
    context.browser.quit()