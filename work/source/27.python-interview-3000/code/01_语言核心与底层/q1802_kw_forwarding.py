"""参数转发的陷阱:重复关键字、展开顺序与签名漂移。"""


def service(url, *, timeout=1.0, retries=3, verify=True):
    return {"url": url, "timeout": timeout, "retries": retries, "verify": verify}


def forward_bad(url, **options):
    # 陷阱一:调用方传 retries,这里又显式传 retries -> 调用时 TypeError
    return service(url, timeout=options.get("timeout", 1.0),
                   retries=2, **options)


def forward_good(url, **options):
    # 正解:先弹出已消费的键,其余原样转发
    retries = options.pop("retries", 2)
    return service(url, retries=retries, **options)


def order_rule():
    # 陷阱二:f(**kw, timeout=1) 展开顺序在后,重名键直接 TypeError
    kwargs = {"timeout": 9}
    try:
        service("http://x", **kwargs, timeout=1)
    except TypeError as e:
        return str(e)[:40]
    return "没报错?"


def drift_demo():
    # 纯 ** 转发不受中间层参数增减影响
    def outer(**kw):
        return service("http://x", **kw)
    return outer(timeout=5)


if __name__ == "__main__":
    try:
        forward_bad("http://x", retries=9)
    except TypeError as e:
        print("重复关键字:", str(e)[:56])
    print("先弹出再转发:", forward_good("http://x", retries=9, verify=False))
    print("展开顺序规则:", order_rule())
    print("纯 ** 转发无漂移:", drift_demo())
