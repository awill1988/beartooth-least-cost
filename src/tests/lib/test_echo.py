from lib import echo


def test_echo():
    raised_err = False
    try:
        echo("yolo")
    except Exception:
        raised_err = True
    assert raised_err is False
