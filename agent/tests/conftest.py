import pytest
import os
import paramiko


def pytest_configure(config):
    """
    Register custom markers.
    """
    config.addinivalue_line(
        "markers", "smoke: mark smoke test"
    )
    config.addinivalue_line(
        "markers", "apache: mark apache server test"
    )

@pytest.fixture(scope='session')
def ssh_credentials():
    """
    Returns SSH credentials: username, password, hostname, ssh and http ports of the target container.
    """
    env = {
        "username": os.getenv("SSH_USER"),
        "password": os.getenv("SSH_PASSWORD"),
        "hostname": os.getenv("SSH_HOSTNAME", "target"),
        "ssh_port": int(os.getenv("SSH_PORT", 22)),
        "http_port": int(os.getenv("HTTP_PORT", 80))
    }

    return env


@pytest.fixture(scope='session')
def ssh_client(ssh_credentials):
    """
    Creates an SSH client connected to the target.
    The client is closed automatically after test are finished.
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=ssh_credentials["hostname"],
            port=ssh_credentials["ssh_port"],
            username=ssh_credentials["username"],
            password=ssh_credentials["password"]
        )
        yield client
    except Exception as e:
        pytest.skip(f"Could not connect via SSh to {ssh_credentials['hostname']}: {e}")
    finally:
        if client:
            client.close()

