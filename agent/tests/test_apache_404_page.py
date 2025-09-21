import os
import pytest
import requests
import allure


@pytest.mark.apache
@allure.feature("Core functionality")
@allure.story("404 page")
def test_nonexistent_page_returns_404(ssh_credentials):
    """
    Checks that request of a nonexistent page returns error 404.
    """
    url = f"http://{ssh_credentials['hostname']}:{ssh_credentials['http_port']}/does-not-exist"

    with allure.step(f"Sending GET-request to {url}"):
        response = requests.get(url)

    with allure.step("Check response status"):
        assert response.status_code == 404, f"Expected status 404, got {response.status_code}"

