---
title: [Q7519] Agent 全链路追踪：Span 结构与成本归因
date: 2026-11-19
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7519 · Agent 全链路追踪与成本归因

> 难度:★★☆ | 标签:可观测性, trace, 成本

**问**：一次 Agent 运行调了 6 次 LLM、8 个工具——「这次为什么答错」怎么查（span 树怎么组织：llm/tool/decision 三类节点），token 成本怎么归因到「哪一步最烧钱、哪个工具最贵」，追踪数据里哪些字段是事后复盘的刚需（prompt/响应全文要不要存）？

**答**：① Span 树结构：根 span = 一次会话运行，子节点三类——`llm.call`（记录 model/messages/usage/finish_reason）、`tool.call`（工具名/参数/返回摘要/耗时）、`decision`（ReAct 步骤的 thought 摘要，文本节点）——树形让「失败的那次调用」在上下文里被看见（它的父节点是哪个决策、兄弟调用是什么）。② 成本归因：每个 llm span 记录 `prompt_tokens/completion_tokens` × 模型单价 → 汇总出**按工具/按步骤/按会话**三个维度的成本透视——「检索工具平均一次烧 8k prompt token（因为塞了全文）」这类优化点只有归因后才看得见。③ 必存字段：请求参数（脱敏后）、响应全文（复盘必须——「答错」要看模型真的输出了什么，摘要复盘不了）、错误与重试链、版本号（prompt 版本/模型版本/代码版本——不可版本化的 trace 无法对比优化）。合规面：全文存储要做脱敏与保留期（Q6015 分层同构）。

```python
# 全部标准库；demo 实现 span 树 + 成本归因透视
import time, json

class Trace:
    """span 树：root -> (llm | tool | decision)*。"""
    def __init__(self, run_id: str):
        self.run_id = run_id
        self.spans: list[dict] = []
        self._parent = None
    def span(self, kind: str, name: str, **meta):
        s = {"kind": kind, "name": name, "parent": self._parent,
             "t": time.monotonic(), **meta}
        self.spans.append(s)
        return s
    def cost_report(self, prices: dict[str, tuple[float, float]]) -> dict:
        """成本归因：按模型计费，按工具聚合。"""
        by_model, by_tool = {}, {}
        for s in self.spans:
            if s["kind"] == "llm":
                in_p, out_p = prices[s["model"]]
                cost = s["usage"][0] / 1e6 * in_p + s["usage"][1] / 1e6 * out_p
                by_model[s["model"]] = by_model.get(s["model"], 0) + cost
            elif s["kind"] == "tool":
                by_tool[s["name"]] = by_tool.get(s["name"], 0) + s.get("cost", 0)
        return {"by_model": by_model, "by_tool": by_tool,
                "total": sum(by_model.values()) + sum(by_tool.values())}
    def find_failure_chain(self) -> list[str]:
        """失败复盘：找到最后一个 error span 及其父链。"""
        chain, cur = [], next((s for s in self.spans if s.get("error")), None)
        while cur:
            chain.append(f"{cur['kind']}:{cur['name']}" + ("[ERR]" if cur.get("error") else ""))
            cur = next((s for s in self.spans if s is cur["parent"]), None) \
                  if isinstance(cur.get("parent"), dict) else None
        return chain

def run_agent_demo(tr: Trace):
    root = tr.span("decision", "root", thought="用户要查订单状态")
    tr._parent = root
    tr.span("llm", "plan", model="gpt-4o", usage=(3200, 120))       # 塞了全文 → 烧钱点
    tool_span = tr.span("tool", "search_orders", cost=0.0, error="timeout")
    tr._parent = tool_span
    tr.span("llm", "retry", model="gpt-4o-mini", usage=(3100, 90))
    tr._parent = root
    tr.span("tool", "get_order", cost=0.001)

if __name__ == "__main__":
    tr = Trace("run-1")
    run_agent_demo(tr)
    prices = {"gpt-4o": (2.5, 10.0), "gpt-4o-mini": (0.15, 0.6)}
    report = tr.cost_report(prices)
    print("成本归因:", {k: round(v, 4) for k, v in report["by_model"].items()},
          "| total:", round(report["total"], 4))
    # 归因可见的优化点：plan 调用 3200 prompt tokens（全文塞上下文）→ 摘要化省 60%
    print("失败链:", tr.find_failure_chain())
    # 必存字段口径：参数+响应全文（脱敏）+版本号（prompt/模型/代码）；
    # 保留期分层：错误 trace 90 天、成功 trace 采样保留 7 天（Q6015 尾部采样同构）。
```

**追问**：1) 为什么 decision 节点要存 thought 摘要而不是全文？——thought 是模型内部推理，全文存储成本高且多为冗余；摘要（首句/关键意图）足够复盘「当时想干什么」，全文只对错误 trace 保留。2) 成本归因怎么发现「工具最贵」？——tool span 记 cost（外部 API 计费）+ 关联的 llm span token（每次工具调用的上下文构建成本）——「便宜的工具 + 贵的上下文」组合是隐形烧钱大户。3) trace 的采样策略？——错误/超预算全量、成功按比例（Q6015 tail-based 同构）；但 Agent 场景「成功也可能有价值」（用户点踩的成功 trace）——反馈信号关联的 trace 强制保留。

## 背诵要点
1. Span 三类节点：llm（usage/finish_reason）/ tool（参数/耗时/成本）/ decision（thought 摘要），树形组织看上下文。
2. 成本归因三透视：按模型/按步骤/按工具——「全文塞上下文」的烧钱点只有归因后可见。
3. 必存：响应全文（脱敏）+ 三层版本号（prompt/模型/代码）；保留期分层，错误全量。

## 复盘追问
1. 「同 prompt 版本同输入，两次运行结果不同」怎么解释给非技术方？（提示：采样温度与模型非确定性——trace 记录 finish_reason 与随机种子（若 API 支持）+ 排除服务端缓存因素）
2. Agent 成本翻倍了，排查顺序？（提示：归因报表先看是模型单价变了（升级）、步数多了（任务变复杂）、还是单次 token 涨了（上下文膨胀）——三个维度拆开各自有解法）
