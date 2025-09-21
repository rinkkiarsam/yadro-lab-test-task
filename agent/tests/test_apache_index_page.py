import pytest
import requests
import allure


@pytest.mark.apache
@allure.feature("Core functionality")
@allure.story("Index page contents")
def test_index_page(ssh_credentials):
    """
    Checks that /index.html is accessible and contains expected text.
    """
    url = f"http://{ssh_credentials['hostname']}:{ssh_credentials['http_port']}/index.html"

    with allure.step(f"Sending GET-request to {url}"):
        response = requests.get(url)

    with allure.step("Check response status and contents"):
        assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
        with open('./tests/expected_index.html', 'r') as file:
            text = file.read().rstrip('\n')
            assert response.text == text, "Contents of main page don't match with expected"
