import warnings

def approx(expected, tol=1e-9):
    return ("approx", expected, tol)

def assert_equal(actual, expected):
    if isinstance(expected, tuple) and expected[0] == "approx":
        _, exp, tol = expected
        assert abs(actual - exp) <= tol, f"{actual} != {exp} within {tol}"
    else:
        assert actual == expected, f"{actual} != {expected}"

def avg(xs):
    return sum(xs) / len(xs)

def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b

if __name__ == "__main__":
    # pytest 写法:assert sum(x) == pytest.approx(0.3);with pytest.raises(ValueError, match="zero")
    assert_equal(sum([0.1, 0.2]), approx(0.3, tol=1e-9))
    try:
        divide(1, 0)
    except ValueError as e:
        assert "zero" in str(e)
        print("异常断言通过:", e)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        warnings.warn("deprecated", DeprecationWarning)
        assert any(issubclass(x.category, DeprecationWarning) for x in w)
        print("警告断言通过")
