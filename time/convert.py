# -*- coding: utf-8 -*-
import datetime
import six


def convert_date(date):
    """ 将日期转换成datetime.date对象
    Args:
        yyyy-mm-dd字符串、datetime.date、datetime.date、pandas.Timestamp类型的日期
    Return:
        1. date对应的datetime.date对象
    Notice:
        如果date不满足上述格式，则抛出异常
    """
    from pandas import Timestamp

    if isinstance(date, six.string_types):
        if ':' in date:
            date = date[:10]
        return datetime.datetime.strptime(date, '%Y-%m-%d').date()
    elif isinstance(date, datetime.date):
        return date
    elif isinstance(date, (datetime.datetime, Timestamp)):
        return date.date()
    else:
        raise Exception("date 必须是datetime.date, datetime.datetime或者如下格式的字符串:'2015-01-05'")
