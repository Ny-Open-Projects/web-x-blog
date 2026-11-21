"""Q2585 跨语料的实体消歧:同名实体按上下文特征归属。

苹果 在科技库与美食库里是两个实体;消歧打分 = 上下文特征词
命中数 + 语料先验,无上下文时先验兜底,而不是随机选一个。
"""

ENTITIES = {
    "苹果-公司": {"corpus": "tech", "hints": {"发布", "iphone", "市值", "库克"}},
    "苹果-水果": {"corpus": "food", "hints": {"维生素", "甜", "果园", "削皮"}},
}


def disambiguate(mention, context, corpus_prior):
    assert mention in ("苹果",), "示例只处理 苹果"
    best, best_score = None, -1.0
    for name, ent in ENTITIES.items():
        overlap = len(set(context) & ent["hints"])
        prior = 1.0 if ent["corpus"] == corpus_prior else 0.5
        s = overlap + prior
        if s > best_score:
            best, best_score = name, s
    return best, best_score


def main():
    m1 = disambiguate("苹果", {"发布", "iphone", "发布会"}, "tech")
    m2 = disambiguate("苹果", {"削皮", "维生素", "甜"}, "food")
    assert m1[0] == "苹果-公司" and m1[1] == 3.0, m1   # 两个特征命中 加 先验
    assert m2[0] == "苹果-水果" and m2[1] == 4.0, m2
    m3 = disambiguate("苹果", set(), "food")   # 无上下文,靠语料先验兜底
    assert m3[0] == "苹果-水果", m3
    m4 = disambiguate("苹果", {"甜", "库克"}, "tech")  # 特征冲突,先验定夺
    assert m4[0] == "苹果-公司", m4
    print("科技语料命中:", m1)
    print("美食语料命中:", m2)
    print("无上下文先验兜底:", m3, "特征冲突先验定夺:", m4)


if __name__ == "__main__":
    main()
