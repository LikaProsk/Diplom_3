from selenium.common import MoveTargetOutOfBoundsException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from typing import Tuple
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:
    def __init__(self, driver):
        self.driver = driver

    def _open_page(self, page_url):
        self.driver.get(page_url)

    def _get_elements(self, locator: Tuple[str, str], wait_time: int = 10):
        wait = WebDriverWait(self.driver, wait_time)
        elements = wait.until(EC.presence_of_element_located(locator)).find_elements(locator[0], locator[1])

        return elements

    def _click_element(self, locator: Tuple[str, str]):
        self.driver.find_element(locator[0], locator[1]).click()

    def _send_keys(self, locator: Tuple[str, str], value: str):
        self.driver.find_element(locator[0], locator[1]).send_keys(value)

    def _get_element_text(self, locator: Tuple[str, str]):
        return self.driver.find_element(locator[0], locator[1]).text

    def _get_element_text_and_wait(self, locator: Tuple[str, str], wait_time: int = 10):
        wait = WebDriverWait(self.driver, wait_time)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def _get_element_attribute(self, locator: Tuple[str, str], attribute_name: str):
        return self.driver.find_element(locator[0], locator[1]).get_attribute(attribute_name)

    def _check_element_visibility_and_wait(self, locator: Tuple[str, str], wait_time: int = 10):
        wait = WebDriverWait(self.driver, wait_time)
        element = wait.until(EC.visibility_of_element_located(locator))

        return element

    def _is_element_displayed(self, locator: Tuple[str, str]):
        return self.driver.find_element(locator[0], locator[1]).is_displayed()

    def _click_element_and_wait(self, locator: Tuple[str, str], wait_time: int = 20):
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(EC.invisibility_of_element(locator))
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def _move_to_element(self, locator: Tuple[str, str]):
        element = self.driver.find_element(locator[0], locator[1])
        actions = ActionChains(self.driver)
        try:
            actions.move_to_element(element).perform()
        except MoveTargetOutOfBoundsException as error:
            print(error)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def _move_element_and_click(self, locator: Tuple[str, str]):
        element = self.driver.find_element(locator[0], locator[1])
        actions = ActionChains(self.driver)
        try:
            actions.move_to_element(element).click().perform()
        except MoveTargetOutOfBoundsException as error:
            print(error)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def _switch_to_window(self, window_handles_index: int):
        self.driver.switch_to.window(self.driver.window_handles[window_handles_index])

    def _check_open_page(self, url: str):
        wait = WebDriverWait(self.driver, 50)
        assert wait.until(EC.url_contains(url))

    def _drag_and_drop(self, source: Tuple[str, str], target: Tuple[str, str]):
        action = ActionChains(self.driver)

        source_element = self.driver.find_element(source[0], source[1])
        target_element = self.driver.find_element(target[0], target[1])
        action.drag_and_drop(source_element, target_element).perform()

    def _check_exists(self, locator: Tuple[str, str]):
        try:
            self.driver.find_element(locator[0], locator[1])
        except NoSuchElementException:
            return False
        return True
