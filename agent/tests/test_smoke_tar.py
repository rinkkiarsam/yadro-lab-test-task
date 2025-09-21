import pytest
import  allure


@pytest.mark.smoke
@allure.feature("Smoke Tests")
@allure.story("tar utility")
def test_tar_functionality(ssh_client):
    """
    Checks the basic functionality of tar:
    creating an archive, verifying its existence, and unpacking it.
    """
    test_file = "/tmp/test_tar_file.txt"
    archive_file = "/tmp/test_archive.tar"

    try:
        with allure.step("Creating test file on target"):
            ssh_client.exec_command(f"echo 'tar test' > {test_file}")

        with allure.step(f"Archiving file via tar to {archive_file}"):
            stdin, stdout, stderr = ssh_client.exec_command(f"tar -cf {archive_file} {test_file}")
            exit_code = stdout.channel.recv_exit_status()
            assert exit_code == 0, f"Error during archication: {stderr.read().decode()}"

        with allure.step("Check that archive exists"):
            stdin, stdout, stderr = ssh_client.exec_command(f"ls {archive_file}")
            assert archive_file in stdout.read().decode(), "Archive was not created successfully"

    finally:
        with allure.step("Cleanup: deleting test files"):
            ssh_client.exec_command(f"rm -f {test_file} {archive_file}")
