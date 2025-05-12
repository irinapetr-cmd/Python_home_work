import pytest
from string_utils import StringUtils

utils = StringUtils()

# Тесты для capitalize()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("тест", "Тест"),
    ("123abc", "123abc"),
])
def test_capitalize(input_str, expected):
    assert utils.capitalize(input_str) == expected

@pytest.mark.negative
def test_capitalize_edge_cases():
    assert utils.capitalize("") == ""
    assert utils.capitalize("   ") == "   "
    assert utils.capitalize(None) is None

# Тесты для trim()
@pytest.mark.positive
def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("  hello ") == "hello "
    assert utils.trim("no_spaces") == "no_spaces"

@pytest.mark.negative
def test_trim_negative():
    assert utils.trim("") == ""
    assert utils.trim(None) is None

# Тесты для contains()
@pytest.mark.positive
def test_contains_positive():
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "Pro") is True
    assert utils.contains("04 апреля 2023", "апреля") is True

@pytest.mark.negative
def test_contains_negative():
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("", "a") is False
    assert utils.contains(" ", " ") is True
    assert utils.contains(None, "x") is False

# Тесты для delete_symbol()
@pytest.mark.positive
def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("Hello world", "l") == "Heo word"
    assert utils.delete_symbol("123-456-789", "-") == "123456789"

@pytest.mark.negative
def test_delete_symbol_negative():
    assert utils.delete_symbol("", "a") == ""
    assert utils.delete_symbol("NoChange", "z") == "NoChange"
    assert utils.delete_symbol(None, "a") is None

