"""functools.wraps 缺席的实测后果:元数据丢失清单。"""
import functools
import inspect


def loud(func):
    def wrapper(*args, **kwargs):
        print("调用前")
        return func(*args, **kwargs)
    return wrapper


def loud_fixed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("调用前")
        return func(*args, **kwargs)
    return wrapper


@loud
def charge(amount):
    """扣款:金额必须为正。"""
    return amount


@loud_fixed
def charge_fixed(amount):
    """扣款:金额必须为正。"""
    return amount


if __name__ == "__main__":
    print("无 wraps -> __name__:", charge.__name__, "| __doc__:", charge.__doc__)
    print("无 wraps -> 签名:", inspect.signature(charge))
    print("有 wraps -> __name__:", charge_fixed.__name__, "| __doc__:", charge_fixed.__doc__)
    print("有 wraps -> 签名:", inspect.signature(charge_fixed))
    print("__wrapped__ 指向原函数:", charge_fixed.__wrapped__.__name__)
