"""检索结果的引用定位:把答案里的 [1] 引用还原为原文档的精确偏移与高亮片段。"""
import re

CORPUS = {
    "d1": {"title": "退货政策", "text": "商品签收后 7 天内可无理由退货。退货需保持包装完好。"},
    "d2": {"title": "运费说明", "text": "普通订单满 99 元包邮。偏远地区另计运费。"},
}
CHUNKS = [
    {"id": "c1", "doc": "d1", "start": 0, "end": 16},
    {"id": "c2", "doc": "d2", "start": 0, "end": 12},
]
INDEX = {1: "c1", 2: "c2"}
MARK_RE = re.compile(r"\[(\d+)\]")


def locate(marker, index, chunks, corpus):
    cid = index.get(marker)
    if cid is None:
        raise KeyError("引用 [%d] 没有对应的检索块" % marker)
    chunk = next(c for c in chunks if c["id"] == cid)
    doc = corpus[chunk["doc"]]
    highlight = doc["text"][chunk["start"]:chunk["end"]]
    if not highlight:
        raise ValueError("引用 [%d] 偏移区间为空,索引可能过期" % marker)
    return {"marker": marker, "doc": chunk["doc"], "title": doc["title"],
            "start": chunk["start"], "end": chunk["end"], "highlight": highlight}


def resolve_answer(answer, index, chunks, corpus):
    """抽取答案中的全部引用并逐一定位,供前端高亮与溯源展示。"""
    markers = []
    for m in MARK_RE.findall(answer):
        n = int(m)
        if n not in markers:
            markers.append(n)
    return [locate(n, index, chunks, corpus) for n in markers]


if __name__ == "__main__":
    answer = "7 天内可无理由退货[1],满 99 元包邮[2]。"
    refs = resolve_answer(answer, INDEX, CHUNKS, CORPUS)
    assert len(refs) == 2
    assert refs[0]["doc"] == "d1" and refs[0]["highlight"] == "商品签收后 7 天内可无理由退货"
    assert refs[1]["doc"] == "d2" and refs[1]["highlight"] == "普通订单满 99 元包邮"
    assert refs[0]["start"] == 0 and refs[0]["end"] == 16

    # 重复引用只定位一次
    refs2 = resolve_answer("同一段[1]再说一遍[1]", INDEX, CHUNKS, CORPUS)
    assert len(refs2) == 1

    # 引号不存在或偏移过期都要显式报错而不是静默给错位置
    for bad_answer, frag in [("无引用标记", "没"), ("悬空引用[9]", "没有对应")]:
        if bad_answer == "无引用标记":
            assert resolve_answer(bad_answer, INDEX, CHUNKS, CORPUS) == []
        else:
            try:
                resolve_answer(bad_answer, INDEX, CHUNKS, CORPUS)
                raise AssertionError("应当报错")
            except KeyError as e:
                assert "没有对应" in str(e)
    print("引用定位通过:[1][2] 还原为文档偏移与高亮,悬空引用显式报错")
