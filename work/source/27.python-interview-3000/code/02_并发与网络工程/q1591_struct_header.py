"""struct 打包实战: 网络头的编解码与对齐陷阱。

- "!HBBIQ": ! 是网络字节序(大端)且无填充, 字段紧挨着, 跨机协议的标准选择;
- "@": 本机对齐, 编译器会在字段间塞 padding —— "@BH" 占 4 字节而 "!BH" 占 3,
  解析方用错前缀就会错位;
- unpack_from + calcsize 是帧处理标准姿势: 头长定 payload 起点, 偏移解析不切片。
"""
import struct

HEADER_FMT = "!HBBIQ"     # magic(H) version(B) msg_type(B) length(I) ts(Q)


def pack_header(magic, version, msg_type, payload_len, ts):
    return struct.pack(HEADER_FMT, magic, version, msg_type, payload_len, ts)


def main():
    payload = b"hello-frame"
    head = pack_header(0xC0DE, 1, 7, len(payload), 1700000000)
    print("打包后的头:", head.hex())
    print("网络序头长:", struct.calcsize(HEADER_FMT), "字节")

    # 对齐陷阱: 同样的字段, 本机对齐会塞 padding
    print("!BH 紧凑 3 字节 | @BH 本机对齐",
          struct.calcsize("@BH"), "字节(中间塞了 1 字节 padding)")

    # 标准帧解析: 头在偏移 0, payload 紧随其后
    frame = head + payload
    magic, version, msg_type, plen, ts = struct.unpack_from(HEADER_FMT, frame, 0)
    body = frame[struct.calcsize(HEADER_FMT):struct.calcsize(HEADER_FMT) + plen]
    print("解出头: magic=%#x ver=%d type=%d len=%d ts=%d"
          % (magic, version, msg_type, plen, ts))
    print("解出 payload:", body)
    assert (magic, version, msg_type, plen, ts) == (0xC0DE, 1, 7, len(payload), 1700000000)
    assert body == payload, "payload 应原样解出"

    # 边界防护: 截断的帧必须显式报错而不是解出垃圾
    try:
        struct.unpack_from(HEADER_FMT, frame[:9], 0)
        raise AssertionError("截断帧不应解包成功")
    except struct.error as e:
        print("截断帧被拒绝:", e)

    print("结论: 协议头用 ! 前缀定死字节布局; calcsize + unpack_from 管'从哪切'")


if __name__ == "__main__":
    main()
