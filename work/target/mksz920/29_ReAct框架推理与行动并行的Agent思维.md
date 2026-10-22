# 29. ReAct 框架：推理与行动并行的 Agent 思维

## 纲要

- **ReAct = Reason + Act（推理 + 行动）**：将推理与行动结合——在推理指导下行动，行动提供额外信息支撑更好推理。
- **解决的两类偏颇**：只推理无外部信息辅助 → 效果差；只行动不推理 → 行动本身可能错、结果错。ReAct 让二者互补。
- **对比四种回答过程**：直接回答（错）→ 仅思考推理（无效）→ 调外部搜索但用错方式（无效）→ **ReAct**（Thought→Action→Observation 循环，多次迭代找到正确答案）。
- **ReAct 提示词三要素**：**Thought**（思考下一步做什么并给理由）、**Action**（执行动作）、**Observation**（观察执行结果，反馈给 Thought 重复），直到 Final Answer。
- **一次迭代 = Thought → Action → Observation**：Thought 决定动作及理由；Action 执行；Observation 观察结果再喂回 Thought，循环至答案。
- **提示词结构**：① 列出可用工具（功能 + 参数说明）；② 给出 ReAct 步骤（Thought/Action/Action Input/Observation）；③ 强调可多轮迭代；④ 遇 Final Answer 即终止。
- 本章按课程口径重构；产品名已规范化（ReAct）；剥离营销与课程群引流。

## 一、ReAct 的核心思想

ReAct 是一种思维模式，名字即 **Reason（推理）+ Act（行动）**。它针对两个常见问题：

- **只推理不行动**：没有外部信息辅助，推理凭空进行，效果差；
- **只行动不推理**：采取的行动本身可能不正确，结果跟着错。

ReAct 把二者结合：**推理指导行动，行动产生的观察反哺推理**，形成闭环，逐步逼近正确答案。

## 二、四种回答过程对比

| 方式 | 做法 | 结果 |
| --- | --- | --- |
| 直接回答 | 无思考直接给答案 | 错误 |
| 仅推理 | 思考后作答，无外部信息 | 无效 |
| 调外部工具但用错 | 调搜索但方式不对 | 无效 |
| **ReAct** | Thought→Action→Observation 循环迭代 | 多次迭代找到正确答案 |

ReAct 通过「先短思考（Thought）→ 据思考采取 Action → 得到 Observation → 再 Thought」的循环，经两次迭代、第三次命中正确答案。

## 三、ReAct 提示词三要素

一次 ReAct 迭代由三段组成：

1. **Thought（思考）**：经过思考决定下一步做什么动作，并给出理由。
2. **Action（行动）**：执行该动作。
3. **Observation（观察）**：观察 Action 的结果，将其反馈给 Thought，重复迭代直到找到答案。

> 完整循环：`Thought → Action → Observation → (Thought → Action → Observation) ... → Final Answer`。

## 四、ReAct 提示词结构

```
1. 可用工具列表（功能说明 + 参数说明）
   - 工具A：做X，参数：name(类型), content(类型)
   - 工具B：做Y，参数：...
2. 回答步骤（ReAct 模式）：
   Thought: 思考并给理由
   Action: 动作名
   Action Input: 参数
   Observation: 动作结果
3. 强调：迭代可重复多次
4. 终止条件：遇到 Final Answer 即得到正确答案
```

**关键点**：工具描述必须详细（功能 + 参数），模型才能据此判断调哪个、传什么；提示词写法需实测调优。

## 五、FAQ

**Q1：ReAct 和普通 Chain 比强在哪？**
普通 Chain 一次性推理；ReAct 允许「思考-行动-观察」多轮迭代，能借助工具纠错、逐步逼近，适合需外部信息的复杂任务。

**Q2：Action 和 Observation 必须成对吗？**
是的，一次 Action 必产生 Observation，Observation 又驱动下一轮 Thought，构成闭环。

**Q3：ReAct 一定会多轮吗？**
不一定，简单问题可能一轮到 Final Answer；复杂问题才需多次迭代，提示词强调「可重复多次」。

**Q4：Final Answer 的作用？**
作为终止信号，模型输出 Final Answer 即代表已得出最终答案，停止迭代。

## 六、面试高频问答

**1. ReAct 是什么？**
Reason + Act，推理指导行动、行动观察反哺推理的循环思维框架。

**2. ReAct 三要素？**
Thought（思考+理由）、Action（执行）、Observation（观察结果反馈）。

**3. 为什么需要 ReAct？**
弥补「只推理无信息」与「只行动不推理」的偏颇，借助工具迭代逼近正确答案。

**4. ReAct 提示词结构？**
工具列表（功能+参数）+ ReAct 步骤（Thought/Action/Action Input/Observation）+ 多轮迭代 + Final Answer 终止。

## 七、ops 提示（增效）

> **工具描述是 ReAct 命门**：功能与参数写得含糊，模型 Action 必选错；先在小样本上把工具描述调到稳。
>
> **迭代上限要设**：防止 Thought/Action 死循环烧 token，实战常设 2~3 轮上限。
>
> **Observation 解析要鲁棒**：从模型输出里正则提取 Action/Input/Observation，模型格式偶发漂移需兜底解析。

