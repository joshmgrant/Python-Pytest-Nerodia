import pytest


def test_add_one_item(browser):
    browser.goto('www.saucedemo.com/inventory.html')
    browser.button(class_name='add-to-cart-button').click()

    assert browser.span(class_name='shopping_cart_badge').text == '1'
    
    browser.goto("https://www.saucedemo.com/cart.html")
    assert len(browser.divs(class_name='inventory_item_name')) == 1

def test_add_two_items(browser):
    browser.goto('www.saucedemo.com/inventory.html')
    browser.button(class_name='add-to-cart-button').click()
    browser.button(class_name='add-to-cart-button').click()

    assert browser.span(class_name='shopping_cart_badge').text == '2'
    
    browser.goto("https://www.saucedemo.com/cart.html")
    assert len(browser.divs(class_name='inventory_item_name')) == 2
