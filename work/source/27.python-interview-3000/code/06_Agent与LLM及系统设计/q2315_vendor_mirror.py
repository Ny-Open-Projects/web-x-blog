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
