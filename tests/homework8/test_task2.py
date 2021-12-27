from homework8.task2 import TableData

presidents = TableData(database_name="./homework8/example.sqlite", table_name="presidents")


def test_contains():
    assert ("Yeltsin" in presidents) is True


def test_count_length():
    assert len(presidents) == 3


def test_getitem():
    assert presidents["Yeltsin"] == [("Yeltsin", 999, "Russia")]


def test_iteration():
    count = 0
    for p in presidents:
        count += 1
    assert count == 3
