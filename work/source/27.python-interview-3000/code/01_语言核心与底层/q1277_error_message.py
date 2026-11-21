

def parse_port(raw):
    try:
        port = int(raw)
    except (TypeError, ValueError):
        raise ValueError(
            "invalid port %r: must be an integer in 1..65535" % (raw,)
        ) from None                        # 转换失败:链路无信息价值
    if not 1 <= port <= 65535:
        raise ValueError("port out of range: got %d, expected 1..65535" % port)
    return port


if __name__ == "__main__":
    print(parse_port("8080"))
    for bad in ("abc", None, "99999"):
        try:
            parse_port(bad)
        except ValueError as e:
            print(type(e).__name__, "->", e)
