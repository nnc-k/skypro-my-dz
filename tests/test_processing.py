import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(operations):
    result = filter_by_state(operations)

    assert len(result) == 2
    assert result[0]["state"] == "EXECUTED"


def test_filter_by_state_cancelled(operations):
    result = filter_by_state(operations, "CANCELED")

    assert len(result) == 1
    assert result[0]["state"] == "CANCELED"


def test_sort_by_date_desc(operations):
    result = sort_by_date(operations)

    assert result[0]["date"] == "2024-03-11T10:00:00"
    assert result[-1]["date"] == "2022-05-05T09:30:00"


def test_sort_by_date_asc(operations):
    result = sort_by_date(operations, False)

    assert result[0]["date"] == "2022-05-05T09:30:00"
    assert result[-1]["date"] == "2024-03-11T10:00:00"