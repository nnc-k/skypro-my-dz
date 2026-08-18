import pytest

from src.decorators import log


def test_log_success_console(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(1, 2)

    captured = capsys.readouterr()

    assert result == 3
    assert captured.out == "add ok\n"


def test_log_error_console(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()

    assert (
        captured.out
        == "divide error: ZeroDivisionError. Inputs: (1, 0), {}\n"
    )


def test_log_success_file(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def add(a, b):
        return a + b

    result = add(1, 2)

    assert result == 3
    assert log_file.read_text(encoding="utf-8") == "add ok\n"


def test_log_error_file(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    assert (
        log_file.read_text(encoding="utf-8")
        == "divide error: ZeroDivisionError. Inputs: (1, 0), {}\n"
    )