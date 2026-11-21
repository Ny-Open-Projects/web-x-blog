---
title: [Q2315] 多供应商镜像对比:同请求双发与响应 diff
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2315 · 多供应商镜像对比:同请求双发与响应 diff

> 难度:★★★☆ | 标签:LLM 运维, 供应商, 对比

**问**:要把主供应商切到备用家,怎么在不影响线上的前提下知道两家行为差异有多大?

**答**:镜像对比:抽样一部分线上请求,同一 prompt 双发两家,响应归一后逐字段 diff。归一是关键——标点、空白、同义措辞的差异不是分歧,"退货期限为 30 天"与"退货期限是30天"应判一致,归一函数把噪声滤掉,剩下的事实性分歧(一个说 30 天一个说 15 天)才是真差异。除文本外还要比 usage:输出 token 差距反映两家啰嗦程度,直接关系切换后的成本。产出物是迁移风险清单:分歧率、分歧样本分类、用量差,分歧率低的类目先切,高的类目缓切或不切。镜像流量要限速与打标,绝不能让对比流量翻倍成本。

```python
# file: code/06_Agent与LLM及系统设计/q2315_vendor_mirror.py
"""多供应商镜像对比:同一请求双发两家桩,响应归一后逐字段 diff,产出迁移风险清单。"""
import re


def vendor_a(prompt):
    return {"text": "退货期限为 30 天。", "usage": {"in": 10, "out": 8}}


def vendor_b(prompt):
    return {"text": "退货期限是30天", "usage": {"in": 11, "out": 7}}


def vendor_c(prompt):
    return {"text": "退货期限为 15 天。", "usage": {"in": 10, "out": 6}}


def normalize(text):
    t = re.sub(r"[\s。,，.!?!?]", "", text)
    return t.replace("是", "为")


def mirror_compare(prompt, vendors):
    outs = {name: fn(prompt) for name, fn in vendors.items()}
    normed = {n: normalize(o["text"]) for n, o in outs.items()}
    diff = [{"field": "text", "normalized": normed}] if len(set(normed.values())) > 1 else []
    out_tokens = [o["usage"]["out"] for o in outs.values()]
    return {"agree": not diff, "diff": diff,
            "usage_out_gap": max(out_tokens) - min(out_tokens)}


if __name__ == "__main__":
    vendors = {"a": vendor_a, "b": vendor_b}
    r = mirror_compare("退货多久?", vendors)
    assert r["agree"], "标点措辞差异归一后应判一致"
    assert r["usage_out_gap"] == 1
    r2 = mirror_compare("退货多久?", {"a": vendor_a, "b": vendor_b, "c": vendor_c})
    assert not r2["agree"] and r2["diff"][0]["normalized"]["c"] == "退货期限为15天", "事实分歧必须曝光"
    assert r2["usage_out_gap"] == 2
    print("镜像对比通过:归一化去噪 一致判定 分歧与用量差曝光")
```

**追问**:
- 归一判一致会不会把真差异也抹掉? 答:归一只处理标点空白与白名单同义词,数值与实体差异保留,归一规则本身要进评审
- 采样比例多少合适? 答:按供应商流量的小个位数百分比起步,分歧率高的类目再加密采样
