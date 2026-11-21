import os  # noqa: F401  未使用导入,ruff F401 会提醒
import sys


def old_style(items):
    # ruff UP 规则会建议用 list comprehension 或内置函数
    result = []
    for i in items:
        if i % 2 == 0:
            result.append(i * 2)
    return result


def test_even_doubled():
    assert old_style([1, 2, 3, 4]) == [4, 8]
