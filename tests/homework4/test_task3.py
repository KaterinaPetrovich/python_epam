from homework4.task3 import my_precious_logger


def test_error_my_precious_logger(capsys):
    text = "error some text"
    my_precious_logger(text)
    out, err = capsys.readouterr()
    assert err == text
    assert out == ""


def test_out_my_precious_logger(capsys):
    text = "some text"
    my_precious_logger(text)
    out, err = capsys.readouterr()
    assert err == ""
    assert out == text
