# import requests
# requests.get(address) - gets the page at the address
# response.status_code == requests.code.ok - check the page respnse is good
# response.raise_for_status() - use to confirm succesful response
#    try:
#    res.raise_for_status()
#    except Exception as exc:
#    print('There was a problem: %s' % (exc))
# output to file via write binary open(filename, 'wb')
#   for chunk in res.iter_content(100000):
#       file.write(chunk)
# bs4.BeautifulSoup(response.text)
# soup.select() returns a list
# soup.select('div') All elements named < div >
# soup.select('#author') The element with an id attribute of author
# soup.select('.notice') All elements that use a CSS class attribute named notice
# soup.select('div span') All elements named < span > that are within an element named < div >
# soup.select('div > span') All elements named < span > that are directly within an element named < div >, with no other element in between
# soup.select('input[name]') All elements named < input > that have a name attribute with any value
# soup.select('input[type="button"]') All elements named < input > that have an attribute named type with value button
# elements = soup.select(thing)
# elements.getText() - returns the text between the open and close tags
# element.get() - access attribute values for an element
# element.attr - shows all the HTML attributes of the tag as a dictionary
# from selenium import webdriver
# browser - webdriver.Firefox()
# browser.get(webaddress)
# browser.find_element_by_class_name(name)
# browser.find_elements_by_class_name(name)
#       Elements that use the CSS class name
# browser.find_element_by_css_selector(selector)
# browser.find_elements_by_css_selector(selector)
#       Elements that match the CSS selector
# browser.find_element_by_id(id)
# browser.find_elements_by_id(id)
#       Elements with a matching id attribute value
# browser.find_element_by_link_text(text)
# browser.find_elements_by_link_text(text)
#       <a > elements that completely match the text provided
# browser.find_element_by_partial_link_text(text)
# browser.find_elements_by_partial_link_text(text)
#       <a > elements that contain the text provided
# browser.find_element_by_name(name)
# browser.find_elements_by_name(name)
#       Elements with a matching name attribute value
# browser.find_element_by_tag_name(name)
# browser.find_elements_by_tag_name(name)
#       Elements with a matching tag name (case insensitive 
#       an < a > element is matched by 'a' and 'A')
# only arguments for *_by_tag_name are case insensitive
# tag_name - The tag name, such as 'a' for an < a > element
# get_attribute(name) - The value for the element’s name attribute 
# text - The text within the element, such as 'hello' in < span > hello < /span >
# clear() - For text field or text area elements, clears the text typed into it
# is_displayed() - Returns True if the element is visible otherwise returns False
# is_enabled() - For input elements, returns True if the element is enabled otherwise returns False
# is_selected() - For checkbox or radio button elements, returns True if the element is selected otherwise returns False
# location - A dictionary with keys 'x' and 'y' for the position of the element in the page
# element.send_heys('text') - enters the text into the field
# element.click - simulates a click on a field
# element.submit() - has the same result as clicking submit for the form in which that element is
# selenium.wedriver.common.keys - module containing keys that can't be typed as text
# Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT
#   The keyboard arrow keys
# Keys.ENTER, Keys.RETURN 
#   The enter and return keys
# Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP
#   The home, end, pagedown, and pageup keys
# Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE
#   The esc, backspace, and delete keys
# Keys.F1, Keys.F2, . . ., Keys.F12 
#   The F1 to F12 keys at the top of the keyboard
# Keys.TAB 
#   The tab key
# browser.back() - Clicks the Back button.
# browser.forward() - Clicks the Forward button.
# browser.refresh() - Clicks the Refresh/Reload button.
# browser.quit() - Clicks the Close Window button.
