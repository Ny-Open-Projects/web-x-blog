---
title: [Q2317] Prompt 仓库的不可变性:内容寻址与引用解析
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2317 · Prompt 仓库的不可变性:内容寻址与引用解析

> 难度:★★★★ | 标签:LLM 运维, Prompt, 工程化

**问**:Q1140 讲了 Prompt 版本注册表,更进一步的"不可变仓库"解决什么问题?

**答**:注册表管的是"现在用哪版",不可变仓库管的是"过去那版永远还在、一字不差"。机制是内容寻址:prompt 正文加元数据算哈希作为对象 id,同内容发布幂等返回同一 id;修改永远产出新对象,旧对象原样保留,物理上就没有"改历史"这个操作。别名(stable、canary)只是指向对象的引用,切换别名是显式动作,历史引用不受影响。请求级审计记录"这次调用用了哪个 cid",复现一个历史请求时按 cid 取回当时的 prompt,精确到字符——这对事故复盘和模型行为对比是决定性的。仓库对象只增不删,清理靠标记归档不靠物理删除。

```python
# file: code/06_Agent与LLM及系统设计/q2317_prompt_repo_immutable.py
"""Prompt 仓库不可变:版本按内容哈希寻址,发布后禁改,引用记录可追溯到请求级。"""
import hashlib, json


def cid_of(text, meta):
    return hashlib.sha256(json.dumps({"t": text, "m": meta}, sort_keys=True,
                                     ensure_ascii=False).encode("utf-8")).hexdigest()[:12]


class PromptRepo:
    def __init__(self):
        self.objects = {}
        self.refs = {}

    def publish(self, text, meta, alias):
        cid = cid_of(text, meta)
        self.objects[cid] = {"text": text, "meta": dict(meta)}
        self.refs[alias] = cid
        return cid

    def resolve(self, alias):
        if alias not in self.refs:
            raise KeyError("未注册别名 %s" % alias)
        cid = self.refs[alias]
        return cid, self.objects[cid]

    def audit_ref(self, alias, request_id):
        cid, _ = self.resolve(alias)
        return {"request": request_id, "alias": alias, "cid": cid}

    def mutate(self, cid, new_text):
        old = self.objects[cid]
        new_cid = cid_of(new_text, old["meta"])
        if new_cid != cid:
            self.objects[new_cid] = {"text": new_text, "meta": old["meta"]}
        return new_cid


if __name__ == "__main__":
    repo = PromptRepo()
    c1 = repo.publish("你是客服,只答退货。", {"lang": "zh"}, "stable")
    c1b = repo.publish("你是客服,只答退货。", {"lang": "zh"}, "stable")
    assert c1 == c1b, "同内容幂等 内容寻址唯一"
    c2 = repo.mutate(c1, "你是客服,只答退款。")
    assert c2 != c1, "改动产出新对象"
    assert repo.objects[c1]["text"] == "你是客服,只答退货。", "旧对象原样保留 不可变"
    assert repo.resolve("stable")[0] == c1, "别名仍指旧版 切换是显式动作"
    repo.refs["stable"] = c2
    assert repo.resolve("stable")[0] == c2
    rec = repo.audit_ref("stable", "req-42")
    assert rec == {"request": "req-42", "alias": "stable", "cid": c2}, "请求级可追溯"
    try:
        repo.resolve("canary")
        raise SystemExit("未注册别名应报错")
    except KeyError:
        pass
    print("Prompt 仓库通过:内容寻址 幂等发布 不可变对象 请求级追溯")
```

**追问**:
- 元数据变了对 cid 有什么影响? 答:meta 参与哈希,元数据调整也是新对象,保证"prompt 加上下文"整体可复现
- 仓库和注册表怎么分工? 答:仓库存不可变对象,注册表管别名与灰度规则,前者是事实后者是决策
