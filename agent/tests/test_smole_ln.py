import pytest
import allure


@pytest.mark.smoke
@allure.feature("Smoke Tests")
@allure.story("ln utility")
def test_ln_functionality(ssh_client):
    """
    Checks the basic functionality of tar:
    creating symlink, checking its contents.
    """
    original_file = "/tmp/original.txt"
    link_file = "/tmp/symlink.txt"
    content = "hello symlink"

    try:
        with allure.step("Creating original file"):
            ssh_client.exec_command(f"echo '{content}' > {original_file}")

        with allure.step("Creating symlink"):
            stdin, stdout, stderr = ssh_client.exec_command(f"ln -s {original_file} {link_file}")
            exit_code = stdout.channel.recv_exit_status()
            assert exit_code == 0, f"Error during symlink creation: {stderr.read().decode()}"

        with allure.step("Reading contents via symlink"):
            stdin, stdout, stderr = ssh_client.exec_command(f"cat {link_file}")
            linked_content = stdout.read().decode().strip()
            assert linked_content == content, "Symlink contents are incorrect"

    finally:
        with allure.step("Cleanup: deleting test files"):
            ssh_client.exec_command(f"rm -f {original_file} {link_file}")
