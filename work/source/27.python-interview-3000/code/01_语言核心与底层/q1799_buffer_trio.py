"""bytes/bytearray/memoryview 三态转换矩阵与只读边界。"""
import struct


def conversion_matrix():
    b = bytes([72, 105])       # bytes:不可变
    ba = bytearray(b)          # bytes -> bytearray:拷贝
    mv = memoryview(ba)        # bytearray -> memoryview:零拷贝视图
    snap = bytes(mv)           # 视图 -> bytes:拷贝出快照
    ba2 = bytearray(mv)        # 视图 -> bytearray:拷贝
    return b, ba, snap, bytes(ba2), snap == bytes(ba)


def view_write_through():
    ba = bytearray(b"hello")
    mv = memoryview(ba)
    mv[0] = ord("H")           # 写视图,写穿到底层
    return ba


def readonly_boundary():
    mv = memoryview(b"immutable")   # bytes 的视图只读
    try:
        mv[0] = 88
    except TypeError as e:
        return "只读视图被拦截: " + str(e)[:30]
    return "写成功了?不可能"


def resize_block():
    ba = bytearray(b"12345")
    mv = memoryview(ba)
    result = None
    try:
        ba.extend(b"678")      # 有活动视图时禁止 resize
    except BufferError as e:
        result = "有视图时禁止 resize: " + str(e)[:22]
    finally:
        mv.release()           # 释放视图后恢复可变
        ba.extend(b"678")
    return result, ba


def struct_view():
    raw = bytearray(struct.pack("<2h", 7, -9))
    shorts = memoryview(raw).cast("h")   # 视图重解释,不拷贝
    return list(shorts), bytes(raw)


if __name__ == "__main__":
    b, ba, snap, snap2, eq = conversion_matrix()
    print("转换矩阵:", b, ba, snap, snap2, "快照相等:", eq)
    print("视图写穿:", view_write_through())
    print(readonly_boundary())
    print(resize_block())
    print("cast 重解释:", struct_view())
