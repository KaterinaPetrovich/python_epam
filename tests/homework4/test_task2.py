from unittest.mock import Mock, patch

import pytest

from homework4.task2 import count_dots_on_i


def test_positive_count_dots_on_i():
    test_data = "tyuiortyuiopoiuyt"

    def fake_get(url):
        fake_response = Mock()
        fake_response.text = test_data
        return fake_response

    with patch("requests.get", fake_get):
        assert count_dots_on_i("https://example.org") == 3


def test_error_count_dots_on_i():
    fake_get = Mock(side_effect=ValueError())
    with patch("requests.get", fake_get):
        with pytest.raises(ValueError):
            count_dots_on_i("https://example.org")
