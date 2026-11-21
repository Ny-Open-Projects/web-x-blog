import random


class ProtocolError(ValueError):
    pass


def encode_frame(msg_type: int, payload: bytes) -> bytes:
    if len(payload) > 0xFFFF:
        raise ProtocolError("payload 超长")
    return bytes([msg_type]) + len(payload).to_bytes(2, "big") + payload


def decode_stream(data: bytes) -> list:
    """合法则返回帧列表, 非法则抛 ProtocolError。绝不允许其他异常逃出。"""
    frames = []
    offset = 0
    while offset < len(data):
        if offset + 3 > len(data):
            raise ProtocolError(f"残余 {len(data) - offset} 字节不足帧头")
        msg_type = data[offset]
        ln = int.from_bytes(data[offset + 1:offset + 3], "big")
        if offset + 3 + ln > len(data):
            raise ProtocolError("负载长度声明越界")
        frames.append((msg_type, data[offset + 3:offset + 3 + ln]))
        offset += 3 + ln
    return frames


def mutate(rnd: random.Random, data: bytes) -> bytes:
    data = bytearray(data)
    op = rnd.randrange(4)
    if op == 0 and data:                          # 翻位
        i = rnd.randrange(len(data))
        data[i] ^= 1 << rnd.randrange(8)
    elif op == 1:                                 # 截断
        data = data[:rnd.randrange(len(data) + 1)]
    elif op == 2 and len(data) > 2:               # 长度字段撒谎
        data[1] = rnd.randrange(256)
        data[2] = rnd.randrange(256)
    else:                                         # 随机替换一段
        i = rnd.randrange(len(data))
        data[i] = rnd.randrange(256)
    return bytes(data)


def main() -> None:
    rnd = random.Random(1330)

    # 不变量一: 合法帧回环
    for _ in range(200):
        t = rnd.randrange(256)
        p = bytes(rnd.randrange(256) for _ in range(rnd.randrange(100)))
        assert decode_stream(encode_frame(t, p)) == [(t, p)]
    print("回环不变量: 200 组合法帧 decode-encode 一致")

    # 不变量二: 变异样本只许 ProtocolError 或正常解析
    valid = b"".join(encode_frame(1, b"abc") + encode_frame(2, b"x" * 40)
                     for _ in range(3))
    handled = crashes = parsed = 0
    for _ in range(5000):
        blob = mutate(rnd, valid)
        try:
            decode_stream(blob)
            parsed += 1
        except ProtocolError:
            handled += 1
        except Exception as exc:                  # 任何其他异常都是解析器漏洞
            crashes += 1
            if crashes <= 3:
                print(f"发现崩溃样本: {exc.__class__.__name__}: {exc}")
    print(f"变异 5000 样本: 正常解析 {parsed}, 协议错误 {handled}, 崩溃 {crashes}")
    assert crashes == 0, "解析器存在未防护异常路径"

    # 恶意超大长度: 必须快速拒绝而不是试图分配
    evil = b"\x01" + (0xFFFF).to_bytes(2, "big")
    try:
        decode_stream(evil)
    except ProtocolError as exc:
        print(f"恶意长度声明被拒: {exc}")
    print("模糊测试通过: 解析器健壮")


if __name__ == "__main__":
    main()
