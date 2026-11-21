"""Signature.replace:程序化构造新签名并挂到包装函数上。"""
import inspect


def query(sql, *, timeout=30, trace=False):
    return sql


def public_wrapper(*args, **kwargs):
    """对外隐藏 trace 参数,内部再补上。"""
    kwargs.setdefault("trace", False)
    return query(*args, **kwargs)


if __name__ == "__main__":
    sig = inspect.signature(query)
    print("原签名:", sig)

    kept = [p for name, p in sig.parameters.items() if name != "trace"]
    public_wrapper.__signature__ = sig.replace(parameters=kept)
    print("包装后对外签名:", inspect.signature(public_wrapper))

    bound = inspect.signature(public_wrapper).bind("select 1", timeout=5)
    print("bind 校验通过:", bound.arguments)

    try:
        inspect.signature(public_wrapper).bind("select 1", trace=True)
    except TypeError as e:
        print("trace 已移出对外契约:", e)
