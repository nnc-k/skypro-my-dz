import pytest


@pytest.fixture
def operations():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2024-03-11T10:00:00",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2023-01-01T12:00:00",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2022-05-05T09:30:00",
        },
    ]