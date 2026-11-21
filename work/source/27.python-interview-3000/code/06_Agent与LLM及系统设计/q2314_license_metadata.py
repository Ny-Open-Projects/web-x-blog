"""语料许可标记:块级 license 元数据随引用透出,受限来源只摘要不逐字,缺标记默认受限。"""
LICENSE_POLICY = {
    "cc-by": {"quote": True, "attr": True},
    "internal": {"quote": True, "attr": False},
    "restricted": {"quote": False, "attr": True},
    "unknown": {"quote": False, "attr": True},
}


def cite_block(store, bid, mode="full"):
    blk = store.get(bid)
    lic = LICENSE_POLICY.get(blk.get("license", "unknown"))
    out = {"bid": bid, "quote": None, "attribution": None, "mode": mode}
    if lic["quote"] and mode == "full":
        out["quote"] = blk["text"]
    else:
        out["quote"] = "摘要:" + blk["text"][:6] + "等"
        out["mode"] = "summary-only"
    if lic["attr"]:
        out["attribution"] = blk["source"]
    return out


if __name__ == "__main__":
    store = {
        "b1": {"text": "退货窗口为三十天整", "source": "公开百科", "license": "cc-by"},
        "b2": {"text": "内部结算规则第七条", "source": "内部wiki", "license": "internal"},
        "b3": {"text": "签约客户专属折扣表", "source": "合作伙伴协议", "license": "restricted"},
        "b4": {"text": "来历不明的转贴文本", "source": " Unknown"},
    }
    c1 = cite_block(store, "b1")
    assert c1["quote"] == "退货窗口为三十天整" and c1["attribution"] == "公开百科", "宽松许可全文加署名"
    c2 = cite_block(store, "b2")
    assert c2["quote"] == "内部结算规则第七条" and c2["attribution"] is None, "内部料可引用但不外署名"
    c3 = cite_block(store, "b3")
    assert c3["mode"] == "summary-only" and "折扣表" not in c3["quote"], "受限来源只给摘要"
    assert c3["attribution"] == "合作伙伴协议", "受限但仍需标注出处"
    c4 = cite_block(store, "b4")
    assert c4["mode"] == "summary-only", "缺 license 标记按最保守处理"
    print("许可标记通过:分级引用 署名策略 缺标记保守降级")
