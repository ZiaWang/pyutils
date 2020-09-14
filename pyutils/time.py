# -*- coding: utf-8 -*-

"""
time
~~~~~~
Introduce:
    提供了日期相关的工具函数

Notice:
    1. 此模块下的函数，尽量都要基于python标准库实现，不要使用第三方模块，这样可移植性更好。
    2. 此模块下的函数，尽量功能都最简单，不要掺入复杂的功能，应有较好的可扩展性。

"""

import datetime
import six


def convert_date(date):
    """ 将日期转换成datetime.date对象
    Args:
        yyyy-mm-dd字符串、datetime.date、datetime.date、pandas.Timestamp类型的日期
    Return:
        1. date对应的datetime.date对象
    Notice:
        1. 如果date不满足上述格式，则抛出异常
        2. date is subclass of datetime
    """
    if isinstance(date, six.string_types):
        if ':' in date:
            date = date[:10]
        return datetime.datetime.strptime(date, '%Y-%m-%d').date()
    elif isinstance(date, datetime.datetime):
        return date.date()
    elif isinstance(date, datetime.date):
        return date
    else:
        raise ValueError("date 必须是datetime.date, datetime.datetime或者如下格式的字符串:'2015-01-05'")


def date_range(start_date, end_date, include_end=True):
    """ 获取指定一段时间区间之内的日期
    Args:
        start_date: 起始时间
        end_date: 结束时间
        include_end: 返回结果中是否包含end_date
    Return:
        返回一个列表，每个元素都是一个datetime.date对象
    """
    start_date = convert_date(start_date)
    end_date = convert_date(end_date)

    if end_date < start_date:
        raise ValueError("end_date必须大于或等于start_date")

    ret = []

    current_date = start_date
    while current_date <= end_date:
        if current_date < end_date:
            ret.append(current_date)
        else:
            if include_end:
                ret.append(current_date)
            else:
                break

        current_date += datetime.timedelta(days=1)
    return ret
