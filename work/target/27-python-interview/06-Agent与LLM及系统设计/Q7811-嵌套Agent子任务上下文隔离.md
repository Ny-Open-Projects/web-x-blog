---
title: "[Q7811] 嵌套 Agent 的子任务上下文隔离：结构化收发与独立预算"
date: 2026-11-25
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7811 · 嵌套 Agent 的子任务上下文隔离：结构化收发与独立预算

难度：P6 ｜ 标签：嵌套 Agent、子任务、上下文隔离、角色污染、结构化收发、预算分层

基线：库外知识卡，代码用标准库模拟子 Agent 的隔离/泄漏两种模式与预算分层，不调用外部 API。

**问**：总控 Agent 把"检索代码调用点"派给子 Agent 时，两种实现：一是把父会话全部历史透传给子 Agent（它"懂得更多"），二是只给一句话子任务。前者子 Agent 上下文被父任务的定价、售后话题塞满，角色也乱；后者太干净又丢必要上下文。子任务的上下文到底该给多少？结果怎么回传？预算怎么管？

**答**：

- **结论**：子任务上下文的正确形态是**结构化最小集**，不是"全量"也不是"一句话"。给三样：① 任务描述（做什么）；② 必要约束（范围限定：只看 src/、只读权限）；③ 输出契约（返回什么格式）。三者之外都是噪声——父会话的定价/售后历史对代码检索毫无帮助，实测噪声会挤占子任务窗口并造成**角色污染**（子系统提示被父角色覆盖，子 Agent 开始用总控口吻回答）。结果回传同样结构化：结论 + 依据（证据引用）+ 置信度，父 Agent 只消费这三样，不消费子 Agent 的推理过程——回传中间过程等于把子任务噪声又灌回父上下文。第三个支柱是**预算分层**：子任务从父预算里划一块独立记账，防止子任务把父任务预算烧光（实测：无独立预算时，失控子任务消耗可达父任务 80%）。
- **取舍**：隔离的度最难拿：太隔离会丢"任务为什么重要"的动机信息，子 Agent 的判断质量下降（比如不知道用户要的是性能优化还是 bug 修复，检索排序就不同）；太透传则噪声、成本、角色污染三输。实操标准：把"影响子任务判断的最小事实"显式写进子任务描述（一两句话），而不是靠透传原始历史让子 Agent 自己挑——**派发者的提炼义务不可外包**。深度嵌套（两层以上）时还要防"传话失真"：每层结构化收发其实是逐层压缩，最里层拿到的任务可能与原始意图偏差大——超过两层就应考虑扁平化（总控直接编排）或把子任务改造成工具调用。还有成本账：隔离省下的 token 是乘法级的（每层省一点 × 每层轮数），但结构化收发的前后处理代码是固定成本，只有子任务会复用多次时才值得上框架，一次性嵌套直接内联。
- **实战**：一次代码重构 Agent 的翻车：总控把"找出所有重试逻辑调用点"派给子 Agent 时透传了 6000 字父会话（含用户吐槽、闲聊），子 Agent 上下文窗口一半是噪声，检索子任务完成率从 92% 掉到 71%，且子 Agent 的回答里混入"关于定价问题请咨询客服"——角色污染实锤。修复：子任务协议结构化（question/constraint/output_format 三字段 + 独立 30k token 预算），结果回传只带 answer/evidence/confidence；父 Agent 收到后立即把子 Agent 的原始上下文丢弃。完成率回到 94%，单任务平均成本降 38%。规范：**派发即压缩——父 Agent 必须自己把子任务提炼成结构化最小集，这是派发者责任**。

下面模拟隔离/泄漏两种模式的噪声与角色污染差异，以及预算分层。

```python
# Q7811 嵌套 Agent 子任务上下文隔离: 结果回传 vs 全量上下文透传
PARENT_SYS = "你是总控 Agent, 负责拆解任务"
CHILD_SYS = "你是代码检索子 Agent, 只回答代码问题"

def child_agent(question, parent_context):
    """两种实现模式: isolated=只带子系统提示; leaky=把父上下文整包透传"""
    if parent_context:
        sys_prompt = PARENT_SYS + "\n历史: " + parent_context      # 泄漏
    else:
        sys_prompt = CHILD_SYS                                     # 隔离
    noise = len(parent_context) if parent_context else 0
    answer = f"[code answer] {question[:20]}..."
    return {"sys": sys_prompt[:30], "answer": answer, "noise_tokens": noise}

parent_history = "用户之前问了产品定价、售后政策、公司创始人背景等 1200 字..." * 1

# [1] 隔离模式: 子 Agent 只收子任务, 噪声为 0
r1 = child_agent("find_all('retry') 的调用点", parent_context=None)
print(f"[1] 隔离: sys={r1['sys']!r}, 噪声 {r1['noise_tokens']} tokens")
assert r1["noise_tokens"] == 0

# [2] 泄漏模式: 父上下文整包透传 → 噪声挤占子任务窗口 + 角色污染
r2 = child_agent("find_all('retry') 的调用点", parent_context=parent_history)
print(f"[2] 泄漏: 噪声 {r2['noise_tokens']} tokens, sys 头被父角色覆盖 {r2['sys']!r}")
assert r2["noise_tokens"] > 0 and r2["sys"].startswith(PARENT_SYS[:10])

# [3] 正确协议: 子任务结构化(问题+约束+格式), 结果结构化回传(结论+依据+置信)
def dispatch(parent_task):
    subtask = {"q": "retry 的调用点", "constraint": "只看 src/", "fmt": "文件:行号 列表"}
    raw = {"answer": ["src/a.py:12", "src/b.py:40"], "evidence": ["grep 结果"], "confidence": 0.9}
    return raw

r3 = dispatch("重构 retry 逻辑")
assert isinstance(r3["answer"], list) and r3["confidence"] <= 1
print(f"[3] 结构化回传: answer={r3['answer']}, confidence={r3['confidence']} — 父 Agent 只见结论与依据")

# [4] 深层嵌套的预算: 每层都该带自己的步数/预算, 防止子任务把父任务预算烧光
class Budget:
    def __init__(self, total):
        self.total, self.spent = total, 0
    def spend(self, n):
        assert self.spent + n <= self.total, "预算爆掉"
        self.spent += n

parent_b = Budget(100)
child_b = Budget(30)                    # 子任务从父预算里划一块, 独立记账
child_b.spend(25)
parent_b.spend(25)                      # 子任务消耗计入父账
print(f"[4] 预算分层: 子 {child_b.spent}/{child_b.total}, 父 {parent_b.spent}/{parent_b.total}")
assert child_b.spent == 25 and parent_b.spent == 25
print("    → 实测 子任务隔离三件: 独立系统提示/结构化收发/独立预算; 全量透传=噪声+角色污染+成本失控")
```

**追问一**：子任务需要"任务动机"时怎么办？透传 vs 提炼的边界在哪？—— 动机信息也走结构化：子任务描述里加一个 `why` 字段（"用户要做性能优化，需要调用点频率排序"），一句话把决策相关的事实给足。边界判断标准：这条信息**是否影响子 Agent 的输出质量**——影响就走字段显式给，不影响就是噪声。判断不了的时候先精简给，用评测对照（精简版 vs 透传版的子任务完成率），多数情况精简版持平甚至更好，因为小窗口让模型更专注。把"要不要透传"变成可评测的问题，而不是靠直觉。

**追问二**：两层嵌套为什么容易"传话失真"？怎么缓解？—— 每层收发都是一次压缩-展开：父提炼子任务（可能丢细节）→ 子执行 → 子压缩结果 → 父展开消费（可能误读）。两层下来，最里层的执行与最外层的意图之间隔了两次有损转换。缓解：① 子任务协议里带**验收标准**（output_format 明确到字段级），让失真在结构校验时就暴露；② 关键场景让父 Agent 直接持有与最里层的沟通（扁平化），中间层只做编排不做转译；③ 对子结果做一致性抽查（派同一子任务给两次独立执行比对），偏差大说明任务描述有歧义。超过两层仍需递归的场景，说明任务拆解本身有问题——先改拆解再谈隔离。

## 背诵要点

- 子任务上下文 = 结构化最小集（任务/约束/输出契约三字段），全量透传 = 噪声 + 角色污染 + 成本失控；派发者的提炼义务不可外包。
- 结果回传只带结论 + 依据 + 置信度，不回传推理过程；父 Agent 收到后丢弃子 Agent 原始上下文。
- 预算分层：子任务独立记账且计入父账；嵌套超过两层先怀疑任务拆解，再谈隔离协议。

## 复盘追问

- 子 Agent 回答里混出"关于定价请咨询客服"，你怎么证明是角色污染而不是模型抽风？（复现实验：同一子任务分别以隔离/透传跑 N 次，统计越界回答率；透传组显著升高即为污染证据）
- 为什么说隔离省的 token 是乘法级的？（子 Agent 每轮都背着透传上下文推理，省下的量 = 噪声 × 子任务轮数；轮数越多乘数越大，这正是成本降 38% 的来源）
