from project import validate_username, validate_password, save_credentials
import pytest

def test_validate_username():
    assert validate_username("valid123") == True
    assert validate_username("invalid@user") == False
    assert validate_username("short") == False
    assert validate_username("toolongusername") == False

def test_validate_password():
    assert validate_password("valid123") == True
    assert validate_password("invalid@pass") == False
    assert validate_password("short") == False
    assert validate_password("toolongpassword") == False

def test_save_credentials(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "user_credentials.txt"

    save_credentials("user3", "password3", filename=test_file)

    with test_file.open() as file:
        content = file.read()

    assert "user3,password3" in content
