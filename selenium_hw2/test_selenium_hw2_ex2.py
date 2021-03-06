from selenium import webdriver
import pytest
import allure

url = "https://epam.github.io/JDI/index.html"

# to run smoke with 3 threads: pytest -m "smoke" -n3
# to run regression with 3 threads: pytest -m "regression" -n3
# to run only smoke and only regression: pytest -m "smoke or regression"
# to run smoke and regression: pytest -m "smoke and regression"


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@allure.suite('smoke')
@pytest.mark.smoke
class TestOnlySmoke():
    @allure.testcase('smoke')
    def test_copy1(self, browser):
        browser.get(url)
        # Assert Browser title
        assert browser.title == "Home Page"

        # Perform login
        browser.find_element_by_id("user-icon").click()
        browser.find_element_by_id("name").send_keys("epam")
        browser.find_element_by_id("password").send_keys("1234")
        browser.find_element_by_id("login-button").click()

    @allure.testcase('smoke')
    def test_copy2(self, browser):
        browser.get(url)
        # Assert Browser title
        assert browser.title == "Home Page"

        # Perform login
        browser.find_element_by_id("user-icon").click()
        browser.find_element_by_id("name").send_keys("epam")
        browser.find_element_by_id("password").send_keys("1234")
        browser.find_element_by_id("login-button").click()

    @allure.testcase('smoke')
    def test_copy3(self, browser):
        browser.get(url)
        # Assert Browser title
        assert browser.title == "Home Page"

        # Perform login
        browser.find_element_by_id("user-icon").click()
        browser.find_element_by_id("name").send_keys("epam")
        browser.find_element_by_id("password").send_keys("1234")
        browser.find_element_by_id("login-button").click()


@allure.suite('regression')
@pytest.mark.regression
class TestOnlyRegression():
    @allure.testcase('regression')
    def test_copy1(self, browser):
        browser.get(url)
        # Assert Browser title
        assert browser.title == "Home Page"

        # Perform login
        browser.find_element_by_id("user-icon").click()
        browser.find_element_by_id("name").send_keys("epam")
        browser.find_element_by_id("password").send_keys("1234")
        browser.find_element_by_id("login-button").click()

    @allure.testcase('regression')
    def test_copy2(self, browser):
        browser.get(url)
        # Assert Browser title
        assert browser.title == "Home Page"

        # Perform login
        browser.find_element_by_id("user-icon").click()
        browser.find_element_by_id("name").send_keys("epam")
        browser.find_element_by_id("password").send_keys("1234")
        browser.find_element_by_id("login-button").click()

    @allure.testcase('regression')
    def test_copy3(self, browser):
        browser.get(url)
        # Assert Browser title
        assert browser.title == "Home Page"

        # Perform login
        browser.find_element_by_id("user-icon").click()
        browser.find_element_by_id("name").send_keys("epam")
        browser.find_element_by_id("password").send_keys("1234")
        browser.find_element_by_id("login-button").click()


@allure.suite('TwoRegressionOnlyOneSmoke')
class TestTwoRegressionOnlyOneSmoke():
    @allure.testcase('regression')
    @pytest.mark.regression
    def test_copy1(self, browser):
        browser.get(url)
        # Assert Browser title
        assert browser.title == "Home Page"

        # Perform login
        browser.find_element_by_id("user-icon").click()
        browser.find_element_by_id("name").send_keys("epam")
        browser.find_element_by_id("password").send_keys("1234")
        browser.find_element_by_id("login-button").click()

    @allure.testcase('regression')
    @pytest.mark.regression
    def test_copy2(self, browser):
        browser.get(url)
        # Assert Browser title
        assert browser.title == "Home Page"

        # Perform login
        browser.find_element_by_id("user-icon").click()
        browser.find_element_by_id("name").send_keys("epam")
        browser.find_element_by_id("password").send_keys("1234")
        browser.find_element_by_id("login-button").click()

    @allure.testcase('smoke')
    @pytest.mark.smoke
    def test_copy3(self, browser):
        browser.get(url)
        # Assert Browser title
        assert browser.title == "Home Page"

        # Perform login
        browser.find_element_by_id("user-icon").click()
        browser.find_element_by_id("name").send_keys("epam")
        browser.find_element_by_id("password").send_keys("1234")
        browser.find_element_by_id("login-button").click()


@allure.suite('both')
class TestBoth():
    @allure.testcase('both')
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_copy1(self, browser):
        browser.get(url)
        # Assert Browser title
        assert browser.title == "Home Page"

        # Perform login
        browser.find_element_by_id("user-icon").click()
        browser.find_element_by_id("name").send_keys("epam")
        browser.find_element_by_id("password").send_keys("1234")
        browser.find_element_by_id("login-button").click()

    @allure.testcase('both')
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_copy2(self, browser):
        browser.get(url)
        # Assert Browser title
        assert browser.title == "Home Page"

        # Perform login
        browser.find_element_by_id("user-icon").click()
        browser.find_element_by_id("name").send_keys("epam")
        browser.find_element_by_id("password").send_keys("1234")
        browser.find_element_by_id("login-button").click()

    @allure.testcase('both')
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_copy3(self, browser):
        browser.get(url)
        # Assert Browser title
        assert browser.title == "Home Page"

        # Perform login
        browser.find_element_by_id("user-icon").click()
        browser.find_element_by_id("name").send_keys("epam")
        browser.find_element_by_id("password").send_keys("1234")
        browser.find_element_by_id("login-button").click()
