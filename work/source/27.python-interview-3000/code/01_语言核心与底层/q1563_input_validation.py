

def normalize_port(value):
    """宽容输入:接受 int 或数字字符串,严格输出 int。"""
    if isinstance(value, bool):        # bool 是 int 子类,先排除
        raise ValueError("port 不能是布尔值, got %r" % value)
    try:
        port = int(value)
    except (TypeError, ValueError):
        raise ValueError("port 必须是整数或数字字符串, got %r" % value) from None
    if not 1 <= port <= 65535:
        raise ValueError("port 必须在 1-65535, got %s" % port)
    return port


def connect(host, port, retries=3):
    if not isinstance(host, str) or not host.strip():
        raise ValueError("host 必须是非空字符串, got %r" % host)
    port = normalize_port(port)
    if not isinstance(retries, int) or retries < 0:
        raise ValueError("retries 必须是非负整数, got %r" % retries)
    return host.strip(), port, retries


if __name__ == "__main__":
    print(connect(" db.internal ", "5432"))
    print(connect("localhost", 6432, retries=0))

    for bad in [("", 80), ("h", "abc"), ("h", 0), ("h", True), ("h", 80, -1)]:
        try:
            connect(*bad)
        except ValueError as err:
            print("rejected:", err)

    print("bool 是 int 子类, 必须显式排除: isinstance(True, int) =",
          isinstance(True, int))
