"""RAG 免责声明策略:按话题风险分级,高风险答案自动附加声明,声明只加一次。"""
POLICY = {
    "legal": "本回答引自公开文档,不构成法律意见,重大决策请咨询执业律师。",
    "medical": "健康信息仅供参考,用药请遵医嘱。",
    "finance": "以下内容不构成投资建议,市场有风险。",
    "product": "信息以最新官方文档为准。",
}
HIGH_RISK = ("legal", "medical", "finance")


def classify(topic):
    if topic in POLICY:
        return topic, "high" if topic in HIGH_RISK else "low"
    return "general", "low"


def attach(answer, topic):
    name, level = classify(topic)
    text = POLICY.get(name, "")
    if not text or text in answer:
        return {"answer": answer, "disclaimer": None, "topic": name, "level": level}
    sep = "" if answer.endswith(("。", "!", "?")) else "。"
    return {"answer": answer + sep + text, "disclaimer": text,
            "topic": name, "level": level}


if __name__ == "__main__":
    r1 = attach("根据《劳动合同法》第八十二条,你可以主张二倍工资。", "legal")
    assert r1["disclaimer"] and r1["level"] == "high", "法律话题必须带声明"
    r2 = attach(r1["answer"], "legal")
    assert r2["answer"] == r1["answer"] and r2["disclaimer"] is None, "声明幂等 不重复追加"
    r3 = attach("我们的退货窗口是 30 天。", "product")
    assert r3["disclaimer"] and r3["level"] == "low"
    r4 = attach("今天天气不错。", "general")
    assert r4["disclaimer"] is None and r4["topic"] == "general"
    r5 = attach("先协商再仲裁。", "legal2")
    assert r5["disclaimer"] is None, "未知话题按 general 不乱加"
    print("免责声明通过:话题分级 幂等追加 未知话题不误伤")
