import global_functions
import portal_functions
import portal_html_element
import time

# EXAMPLE TEST - search host in portal - EXAMPLE TEST #
#
# get a webdriver of type 'Chrome' (default)
web_driver = global_functions.get_web_driver("Chrome")
# log in to our portal
portal_functions.login_to_portal(web_driver)
# fill in the search field of the portal with a host (string) and click the search button
portal_functions.fillin_search_field_and_click_search_button(web_driver, portal_html_element.host_to_search)
# click on the host to load its properties
portal_functions.click_link_by_element_id(web_driver, portal_html_element.host_to_search)
time.sleep(2)
# assert phrase 'DNS Name' exits in the HTML of the page
assert "DNS Name" in web_driver.page_source
# close the driver
web_driver.close()

