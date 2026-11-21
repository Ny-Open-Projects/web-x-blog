"""Q2578 切块的语义边界检测:相邻句相似度断崖处下刀。

固定长度切块会把一个完整论述拦腰截断;把句子嵌入后算相邻句
余弦,相似度跌破阈值即为主题断崖,在断崖处切块,块内主题完整。
嵌入用确定性词哈希假向量,离线可复现。
"""
import math
import re

DIM = 64


def embed(text):
    """确定性假嵌入:词哈希入桶后归一化,仅用于离线实验。"""
    v = [0.0] * DIM
    for w in re.findall(r"[a-z0-9]+", text.lower()):
        h = 0
        for ch in w:
            h = (h * 31 + ord(ch)) % DIM
        v[h] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


def adjacent_sims(sentences):
    embs = [embed(s) for s in sentences]
    return [cosine(embs[i], embs[i + 1]) for i in range(len(embs) - 1)]


def detect_boundaries(sentences, threshold):
    return [i + 1 for i, s in enumerate(adjacent_sims(sentences)) if s < threshold]


def chunk(sentences, bounds):
    chunks, prev = [], 0
    for b in bounds + [len(sentences)]:
        chunks.append(sentences[prev:b])
        prev = b
    return chunks


SENTS = ["cat eats fish", "cat likes fish", "fish feeds cat",
         "database stores rows", "database stores rows fast", "rows live in database"]


def main():
    sims = adjacent_sims(SENTS)
    in_group = [sims[0], sims[1], sims[3], sims[4]]
    across = sims[2]
    assert min(in_group) > 0.3, in_group          # 组内相似度高
    assert across < 0.1, across                    # 跨主题断崖低
    bounds = detect_boundaries(SENTS, threshold=0.15)
    assert bounds == [3], bounds
    cs = chunk(SENTS, bounds)
    assert len(cs) == 2 and cs[0][0] == "cat eats fish" and cs[1][0] == "database stores rows"
    print("相邻相似度:", [round(s, 3) for s in sims])
    print("边界句索引:", bounds, "块数:", len(cs))


if __name__ == "__main__":
    main()
