from __future__ import annotations  # Python 3.9 兼容: 让 bytes | None 注解延迟求值


def encode_simple(s: str) -> bytes:
    return f"+{s}\r\n".encode()


def encode_error(s: str) -> bytes:
    return f"-{s}\r\n".encode()


def encode_int(n: int) -> bytes:
    return f":{n}\r\n".encode()


def encode_bulk(data: bytes | None) -> bytes:
    if data is None:
        return b"$-1\r\n"          # NULL bulk string
    return b"$" + str(len(data)).encode() + b"\r\n" + data + b"\r\n"


def encode_array(items: list) -> bytes:
    out = b"*" + str(len(items)).encode() + b"\r\n"
    for item in items:
        out += encode_bulk(item)
    return out


def encode_command(*args: str) -> bytes:
    """客户端发送命令: 批量字符串数组。"""
    return encode_array([a.encode() for a in args])


if __name__ == "__main__":
    print("简单字符串:", encode_simple("OK"))
    print("错误:      ", encode_error("WRONGTYPE Operation against a key"))
    print("整数:      ", encode_int(1000))
    print("批量字符串:", encode_bulk(b"hello"))
    print("NULL bulk: ", encode_bulk(None))
    print("数组:      ", encode_array([b"a", b"b"]))
    print()
    print("GET key 命令的实际报文:")
    cmd = encode_command("GET", "user:42")
    print("  原始字节:", cmd)
    print("  可读形式:", cmd.decode().replace("\r\n", "\\r\\n"))
    # 二进制安全验证: 值里含 \r\n 也不会破坏协议
    tricky = encode_bulk(b"line1\r\nline2")
    assert tricky.startswith(b"$12\r\n")
    print("含 CRLF 的值:", tricky, "→ 长度前缀保证二进制安全")
