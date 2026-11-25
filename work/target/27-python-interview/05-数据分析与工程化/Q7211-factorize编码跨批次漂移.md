---
title: "[Q7211] factorize 编码跨批次漂移：模型特征错位"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7211 · factorize 编码跨批次漂移：模型特征错位

难度：P6 ｜ 标签：factorize、类别编码、特征一致性、训练/推理偏斜

基线：Python 3.12；pandas `factorize` 语义；纯 Python 模拟跨批次编码。

**问**：训练时用 `pd.factorize(df["city"])` 把城市转成整数编码，模型效果正常。上线后推理服务对每个请求单独 `factorize` 一次，同一个"杭州"有时编码成 0、有时编码成 3，预测结果乱跳。`factorize` 不是确定性的吗？为什么换个批次就变了？

**答**：
- **结论**：`factorize` 的编码是**按当前数组里类别首次出现的顺序**分配的，不是全局固定映射。训练集里"杭州"第一次出现排第 0，就编码 0；推理请求里如果只有"上海、杭州"，"上海"先出现就占 0，"杭州"变成 1。跨批次、跨请求的编码空间不一致，模型学到的"0=杭州"就失效了。
- **取舍**：正确做法是训练时**固化类别映射**（`categories_` 或 `CategoricalDtype`），推理时用同一份映射做 `reindex`/`map`，未见类别落到统一的 `unknown` 编码。`factorize` 适合"单批次内临时编码"，不适合作为跨批次的持久特征；`sklearn` 的 `OrdinalEncoder`/`OneHotEncoder` 也是同样要求 `fit` 一次、`transform` 多次。
- **实战**：① 把类别映射作为模型工件一起版本化保存；② 推理时未见类别显式映射到 unknown，并监控 unknown 比例；③ 训练/推理用同一套预处理代码，禁止各写一份；④ 上线前做"同一条样本分别走训练管道与推理管道"的对拍，编码必须一致。

```python
def factorize(values: list[str]) -> tuple[list[int], list[str]]:
    mapping: dict[str, int] = {}
    codes = []
    for v in values:
        if v not in mapping:
            mapping[v] = len(mapping)
        codes.append(mapping[v])
    return codes, list(mapping)


def encode_with(values: list[str], categories: list[str]) -> list[int]:
    mapping = {c: i for i, c in enumerate(categories)}
    return [mapping.get(v, -1) for v in values]      # -1 = unknown


if __name__ == "__main__":
    train = ["杭州", "上海", "北京", "杭州"]
    codes_train, categories = factorize(train)
    print("训练编码:", dict(zip(train, codes_train)), "类别:", categories)

    batch = ["上海", "杭州"]
    codes_batch, _ = factorize(batch)
    print("推理单独 factorize:", dict(zip(batch, codes_batch)), "-> 与训练错位")

    fixed = encode_with(batch, categories)
    print("固定映射编码:", dict(zip(batch, fixed)), "-> 与训练一致")
    print("未见类别:", encode_with(["广州"], categories))
```

**追问一**：为什么"训练和推理都调用同一个 `factorize` 函数"仍然会错位？
→ 解析：函数相同不代表**输入集合相同**。编码依赖当前批次的类别出现顺序与集合，训练集和单条请求的集合不同，映射自然不同。一致性要求的是"同一份映射表"，不是"同一个函数"。

**追问二**：未见类别直接映射成 0 会有什么后果？
→ 解析：0 通常对应训练集第一个类别，等于把"广州"误判成"杭州"，模型会给出有偏预测且没有任何异常信号。应该用独立的 unknown 编码（或全零向量），并监控 unknown 比例，超过阈值说明线上分布漂移。
