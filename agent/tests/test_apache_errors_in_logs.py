import os
import pytest
import requests
import allure


@pytest.mark.apache
@allure.feature("Core functionality")
@allure.story("Log analysis")
def test_apache_logs_for_errors(ssh_client):
    """
    Checks that there are no apache errors in the last LOG_ERROR_TIMEOUT_MIN minutes (5 by default)
    """
    timespan = int(os.getenv("LOG_ERROR_TIMEOUT_MIN", "5"))

    with allure.step(f"Looking for errors in /var/log/apache2/ in last {timespan} minutes"):
        command = f"sudo find /var/log/apache2/ -name 'error.log*' -mmin -{timespan} -exec grep -i 'error' {{}} \\;"
        stdin, stdout, stderr = ssh_client.exec_command(command)

        error_output = stdout.read().decode().strip()

    with allure.step("Check that there are no errors in output"):
        assert error_output == "", f"Found errors in logs:\n{error_output}"

