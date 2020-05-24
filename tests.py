import global_functions
import portal_functions
import portal_html_element
import time

# search host in portal
web_driver = global_functions.get_web_driver("Chrome")
portal_functions.login_to_portal(web_driver)
portal_functions.fillin_search_field_and_click_search_button(web_driver, portal_html_element.host_to_search)
portal_functions.click_link_by_element_id(web_driver, "hostname0")
time.sleep(2)
assert "DNS Name" in web_driver.page_source
web_driver.close()

