"""可变参数 API 的签名演化:加参数不破坏老调用方。"""
import inspect
import warnings


def send_v2(to, subject, body, *, cc=None, priority="normal"):
    """新参数一律 keyword-only。"""
    extra = f" cc={cc}" if cc else ""
    return f"v2 -> {to}: {subject}{extra}"


def send_bad(to, cc, subject, body):
    """反例:把新参数插在中间,位置调用全部错位。"""
    return f"bad -> {to} cc={cc} subj={subject}"


def send_bridge(to, subject, body, *args, **kwargs):
    """兼容桥:旧位置参数触发废弃告警,翻译成新关键字后转发。"""
    if args:
        warnings.warn("第四个位置参数已废弃,请改用 cc=", DeprecationWarning)
        kwargs.setdefault("cc", args[0])
    return send_v2(to, subject, body, **kwargs)


if __name__ == "__main__":
    print(send_v2("a@x.com", "hi", "body"))
    print(send_v2("a@x.com", "hi", "body", cc="b@x.com"))

    print("旧签名调用新签名函数会错位:", send_bad("a@x.com", "hi", "body", None))

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        print(send_bridge("a@x.com", "hi", "body", "b@x.com"))
    print("桥接层触发废弃告警:", len(caught) == 1)

    print("v2 签名:", inspect.signature(send_v2))
