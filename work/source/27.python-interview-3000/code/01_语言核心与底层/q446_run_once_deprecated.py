import functools
import warnings

def run_once(func):
    """真实逻辑只执行一次,之后返回缓存结果"""
    result = None
    called = False

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal result, called
        if not called:
            result = func(*args, **kwargs)
            called = True
        return result
    return wrapper

def deprecated(reason):
    def deco(func):
        warned = False

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal warned
            if not warned:                    # 只警告一次
                warnings.warn(
                    f"{func.__name__} is deprecated: {reason}",
                    DeprecationWarning,
                    stacklevel=2,
                )
                warned = True
            return func(*args, **kwargs)
        return wrapper
    return deco

@run_once
def init_config():
    print("  [init_config] heavy work")
    return {"mode": "prod"}

@deprecated("use new_api instead")
def old_api():
    return "old result"

if __name__ == "__main__":
    print(init_config())
    print(init_config())                      # 不再打印 heavy work
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        print(old_api())
        print(old_api())                      # 第二次不重复告警
        print("warnings captured:", len(caught))
