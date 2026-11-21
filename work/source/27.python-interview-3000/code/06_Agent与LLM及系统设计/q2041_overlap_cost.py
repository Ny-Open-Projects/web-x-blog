"""重叠率的索引放大核算:重叠换召回的代价是存储与索引 token 的放大。"""


def amplification(size, overlap):
    """理论放大率:块长除以前进步长。"""
    assert 0 <= overlap < size
    return size / float(size - overlap)


def measured_amplification(text, size, overlap):
    """实测放大率:切块后总字符数除以原文长度。"""
    step = size - overlap
    chunks = []
    i = 0
    while i < len(text):
        c = text[i:i + size]
        chunks.append(c)
        if i + size >= len(text):
            break
        i += step
    return sum(len(c) for c in chunks) / float(len(text))


if __name__ == "__main__":
    text = "语料" * 500                       # 1000 字
    for size, overlap in [(100, 0), (100, 25), (100, 30), (200, 50)]:
        theo = amplification(size, overlap)
        real = measured_amplification(text, size, overlap)
        assert abs(theo - real) < 0.05, (size, overlap, theo, real)

    assert amplification(100, 0) == 1.0, "零重叠无放大"
    assert abs(amplification(100, 25) - 1.333) < 0.01
    assert amplification(100, 50) == 2.0, "一半重叠就是双倍索引"

    # 收益视角:q2040 实验里重叠 4 达到满召回,这里算出它的代价
    cost = amplification(12, 4)
    assert abs(cost - 1.5) < 1e-9, "块长 12 重叠 4 索引放大 1.5 倍"
    assert cost < amplification(12, 8), "达标前提下选小重叠就是省钱"
    print("放大核算通过:理论 1.0/1.33/2.0 与实测吻合,重叠 4 的代价是 1.5 倍索引")
