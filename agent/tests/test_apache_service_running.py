import pytest
import allure


@pytest.mark.apache
@allure.feature("Core functionality")
@allure.story("Process management")
def test_apache_service_active(ssh_client):
    """
    Checks that apache2 process is running on target host.
    """
    with allure.step("Grep for apache2 in running processes"):
        stdin, stdout, stderr = ssh_client.exec_command("pgrep -xl apache2")
        output = stdout.read().decode().strip()

    with allure.step("Check that apache2 process is found in grep output"):
        assert "apache2" in output, "apache2 process not found"

