---
title: [Q2314] 语料许可标记:license 元数据与引用透出
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2314 · 语料许可标记:license 元数据与引用透出

> 难度:★★★☆ | 标签:RAG, 合规, 元数据

**问**:知识库混着公开百科、内部 wiki、签约协议,引用输出时的权限规则不一样,怎么管?

**答**:把许可做成块级元数据,检索引用出口按策略执行:宽松许可(如 cc-by)全文引用加署名;内部语料可引用但不外露来源署名;受限语料只给摘要不逐字;缺 license 标记的一律按最保守策略处理——缺标记不是"默认可用"而是"默认受限",这是合规的第一原则。策略表驱动,新增许可类型是加配置不是改代码。引用透出时 attribution 字段与引用模式一起进响应元数据,审计能对上"这句话到底用了谁的什么权限"。入库环节强制 license 字段校验,没标的语料进隔离区等待补标,而不是默默混进检索池。

```python
# file: code/06_Agent与LLM及系统设计/q2314_license_metadata.py
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
```

**追问**:
- 摘要也是衍生内容,受限语料给摘要合规吗? 答:按协议约定,多数场景事实性摘要可行,合同类语料干脆不入库或只入元数据
- 许可标记会不会拖慢检索? 答:标记随块存储随路返回,只在引用出口做策略判断,检索路径零额外开销
