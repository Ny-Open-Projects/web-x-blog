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
