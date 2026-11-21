---
title: [Q2295] Agent 输出的多语言一致性:语言锁定与术语表
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2295 · Agent 输出的多语言一致性:语言锁定与术语表

> 难度:★☆☆☆ | 标签:Agent, 输出质量, 国际化

**问**:中文客服 Agent 偶尔冒出一句日语或满屏英文术语,用户截图投诉,怎么系统性防住?

**答**:三层防线。第一层语言检测:按假名、谚文、汉字、拉丁的字符区间判语种,顺序很关键——日语含汉字,必须先查假名再查汉字,否则日文回复会被误判成中文。第二层术语表:会话锁定语言后,把必须用目标语言表述的术语强制替换,比如 vector database 替成向量数据库,这类"夹杂英文"不算漂移,是专业表述。第三层漂移告警:检测语种与会话语言不一致就打标,拦截或重生成由策略定,而不是静默发给用户。检测是纯函数,单测成本极低,上线前把三类漂移案例跑一遍即可。

```python
# file: code/06_Agent与LLM及系统设计/q2295_lang_guard.py
"""Agent 多语言一致性:检测回复语言 锁定会话语言 术语表强制翻译 漂移告警。"""
import re

LANG_HINT = [
    ("ja", re.compile(r"[\u3040-\u30ff]")),
    ("ko", re.compile(r"[\uac00-\ud7af]")),
    ("zh", re.compile(r"[\u4e00-\u9fff]")),
]


def detect_lang(text):
    for lang, pat in LANG_HINT:
        if pat.search(text):
            return lang
    if re.search(r"[A-Za-z]", text):
        return "en"
    return "unknown"


class LangGuard:
    def __init__(self, glossary):
        self.glossary = glossary

    def enforce(self, reply, session_lang):
        lang = detect_lang(reply)
        if lang == "unknown":
            lang = session_lang
        fixed = reply
        for src, dst in self.glossary.get(session_lang, {}).items():
            if src in fixed:
                fixed = fixed.replace(src, dst)
        return {"lang": lang, "fixed_text": fixed, "drifted": lang != session_lang}


if __name__ == "__main__":
    guard = LangGuard({"zh": {"vector database": "向量数据库", "RAG": "检索增强生成"}})
    ok = guard.enforce("退货流程如下,请查收。", "zh")
    assert ok["lang"] == "zh" and not ok["drifted"]
    term = guard.enforce("我们用 vector database 存文档。", "zh")
    assert "向量数据库" in term["fixed_text"], "术语表强制翻译"
    assert not term["drifted"], "夹杂英文术语不算语言漂移"
    drift = guard.enforce("返品の手続きをご案内します。", "zh")
    assert drift["drifted"] and drift["lang"] == "ja", "检测到语言漂移"
    en = guard.enforce("Sorry, I cannot help with that.", "zh")
    assert en["drifted"] and en["lang"] == "en", "英文漂移同样告警"
    print("多语言一致性通过:语言检测 术语表替换 漂移告警")
```

**追问**:
- 用户自己切了语言怎么办? 答:会话语言是状态,用户消息语种连续两轮变化就更新锁定,而非每轮独立判断
- 检测对混合文本可靠吗? 答:以占比最大的文字系统为准,纯标点或 emoji 归 unknown 回退会话语言
