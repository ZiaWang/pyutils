# -*- coding: utf-8 -*-
from pyutils.time import convert_date
from pyutils.time import date_range

import datetime
import pytest


def test_convert_date():
    assert convert_date("2020-01-01") == datetime.date(2020, 1, 1)
    assert convert_date("2020-01-01 12:11:11") == datetime.date(2020, 1, 1)
    assert convert_date(datetime.date(2020, 1, 1)) == datetime.date(2020, 1, 1)
    assert convert_date(datetime.datetime(2020, 1, 1, 12, 12, 12)) == datetime.date(2020, 1, 1)

    with pytest.raises(ValueError):
        convert_date(20200101)


def test_date_range():
    assert date_range("2020-01-01", "2020-01-01") == [datetime.date(2020, 1, 1), ]
    assert date_range("2020-01-01", "2020-01-01", include_end=True) == [datetime.date(2020, 1, 1), ]
    assert date_range("2020-01-01", "2020-01-01", include_end=False) == []
    assert date_range("2020-01-01", "2020-01-02", include_end=False) == [datetime.date(2020, 1, 1), ]
    assert date_range("2020-01-01", "2020-01-02", include_end=True) == [datetime.date(2020, 1, 1),
                                                                        datetime.date(2020, 1, 2)]
    assert date_range("2020-01-01", "2020-01-05") == [datetime.date(2020, 1, 1),
                                                      datetime.date(2020, 1, 2),
                                                      datetime.date(2020, 1, 3),
                                                      datetime.date(2020, 1, 4),
                                                      datetime.date(2020, 1, 5)]

    assert date_range("2020-01-01", "2020-01-05", include_end=False) == [datetime.date(2020, 1, 1),
                                                                         datetime.date(2020, 1, 2),
                                                                         datetime.date(2020, 1, 3),
                                                                         datetime.date(2020, 1, 4)]

    with pytest.raises(ValueError):
        date_range("2020-01-03", "2020-01-01")
