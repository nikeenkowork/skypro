def test_log_success(capsys):
    from src.decorators import log

    @log()
    def add(a, b):
        return a + b

    result = add(2, 5)

    assert result == 7

    captured = capsys.readouterr()
    assert "add ok, result=7" in captured.out


def test_log_error(capsys):
    from src.decorators import log

    @log()
    def div(a, b):
        return a / b

    result = div(1, 0)

    assert result is None

    captured = capsys.readouterr()
    assert "div error: ZeroDivisionError" in captured.out


def test_log_success_to_file(tmp_path):
    from src.decorators import log
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(6, 5)

    assert result == 30

    content = log_file.read_text(encoding="utf-8")
    assert "multiply ok, result=30" in content
