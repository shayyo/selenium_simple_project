import environment
import portal_html_element
import time


def login_to_portal(driver):
    """this method receives a web_driver and performs login to Portal with it"""
    driver.get(environment.portal_url)
    driver.find_element_by_id(portal_html_element.username_field_id).send_keys(environment.portal_user)
    driver.find_element_by_id(portal_html_element.password_field_id).send_keys(environment.portal_pass)
    driver.find_element_by_name(portal_html_element.submit_button_name).click()
    return driver


def fillin_search_field_and_click_search_button(driver, element):
    """this method fills-in the 'search field' in Portal and then clicks the 'search button'"""
    driver.find_element_by_id(portal_html_element.search_field_id).send_keys(element)
    driver.find_element_by_id(portal_html_element.submit_search_button_id).click()
    time.sleep(5)


def click_link_by_element_id(driver, element):
    """this method receives a webdriver and an HTML element and clicks it"""
    driver.find_element_by_id(element).click()

