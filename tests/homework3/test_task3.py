from homework3.task3 import Filter, make_filter, sample_data


def test_apply():
    positive_even = Filter([lambda a: a % 2 == 0, lambda a: a > 0])
    assert positive_even.apply(range(6)) == [2, 4]


def test_creation_functions():
    assert len(make_filter(name='polly', type='bird').functions) == 2


def test_make_filter():
    result = make_filter(name='polly').apply(sample_data)[0]
    assert result == sample_data[1]


def test_make_filter_not_existing_key():
    result = make_filter(ame='polly').apply(sample_data)
    assert result == []


def test_make_filter_all_arguments_participation():
    res = make_filter(name='polly', type="bird").apply(sample_data)
    assert len(res) == 1
