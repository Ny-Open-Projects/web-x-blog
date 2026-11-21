"""分区完整性对账:分块校验和比对,二分定位第一个不一致块"""

import hashlib

SOURCE = [f"row-{i:04d}" for i in range(20)]
# 模拟下游第 12 行丢了
TARGET = [r for i, r in enumerate(SOURCE) if i != 12]


def block_hash(rows):
    return hashlib.md5("\n".join(rows).encode()).hexdigest()


def chunked_compare(src, dst, chunk=4):
    mismatch = []
    for i in range(0, max(len(src), len(dst)), chunk):
        hs = block_hash(src[i:i + chunk])
        hd = block_hash(dst[i:i + chunk])
        if hs != hd:
            mismatch.append((i, i + chunk))
    return mismatch


def binary_locate(src, dst, lo, hi):
    """在不一致块内二分到第一处差异的行号"""
    while lo < hi:
        mid = (lo + hi) // 2
        if block_hash(src[lo:mid + 1]) == block_hash(dst[lo:mid + 1]):
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    print(f"上游 {len(SOURCE)} 行, 下游 {len(TARGET)} 行")
    blocks = chunked_compare(SOURCE, TARGET)
    print("不一致块:", blocks)
    lo, hi = blocks[0]
    row = binary_locate(SOURCE, TARGET, lo, hi)
    print(f"定位到首处差异在第 {row} 行: 上游 {SOURCE[row]!r} 下游缺失")
    print("要点:先比分块校验和缩小范围,再在坏块内二分,避免全表逐行比对")
