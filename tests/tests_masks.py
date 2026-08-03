import pytest
from src.masks import get_mask_account


def test_get_mask_account():
    assert get_mask_account("1234567890123456") == "**3456"
    assert get_mask_account("1234560") == "**4560"
    assert get_mask_account("012") == ValueError("Некорректный номер счета.")