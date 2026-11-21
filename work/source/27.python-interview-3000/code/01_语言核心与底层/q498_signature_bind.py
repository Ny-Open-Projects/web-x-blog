import inspect

def make_request(method, url, *, headers=None, timeout=30):
    return {"method": method, "url": url, "headers": headers or {}, "timeout": timeout}

CALL_SPEC = {"method": "GET", "url": "/api/items", "extra": "ignored by design"}

def call_with_mapping(func, spec):
    sig = inspect.signature(func)
    accepted = {k: v for k, v in spec.items() if k in sig.parameters}
    bound = sig.bind(**accepted)          # 缺失必填参数在这里报错
    bound.apply_defaults()
    return func(*bound.args, **bound.kwargs)

def volume(a, b, /, factor=1):            # 3.8 起支持 positional-only
    return a * b * factor

if __name__ == "__main__":
    print(call_with_mapping(make_request, CALL_SPEC))
    sig = inspect.signature(volume)
    bound = sig.bind(2, 3, factor=2)
    print("positional-only bind:", volume(*bound.args, **bound.kwargs))
