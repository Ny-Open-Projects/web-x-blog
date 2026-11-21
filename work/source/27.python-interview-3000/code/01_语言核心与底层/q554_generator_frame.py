import sys

def read_big(n):
    for i in range(n):
        yield i                           # 挂起:整条流水线只保留一个帧

if __name__ == "__main__":
    n = 1_000_000
    gen = read_big(n)
    print("generator object:", sys.getsizeof(gen), "bytes")
    print("suspended frame exists:", gen.gi_frame is not None)

    lst = list(range(n))
    print("materialized list:", sys.getsizeof(lst) // 1024, "KB (pointers only)")

    print("first item:", next(gen))
    print("after next, still one frame:", sys.getsizeof(gen))
    del lst                               # 释放物化列表
