import struct

if __name__ == "__main__":
    payload = bytearray(b"\x00" * 8)
    view = memoryview(payload)
    view[0:4] = b"\x01\x02\x03\x04"       # 写穿到底层缓冲
    print("payload:", payload.hex())

    struct.pack_into(">I", payload, 4, 1024)
    print("parsed:", struct.unpack_from(">I", payload, 4))

    mv = view[0:4]                        # 切片不拷贝,共享同一块内存
    mv[0] = 9
    print("after view write, payload[0]:", payload[0])

    ro = bytes(payload)                   # 真正的拷贝在这里才发生
    print("snapshot:", ro.hex(), len(ro))
    mv.release()                          # 先释放子视图
    view.release()                        # 再释放父视图,底层才可 resize
