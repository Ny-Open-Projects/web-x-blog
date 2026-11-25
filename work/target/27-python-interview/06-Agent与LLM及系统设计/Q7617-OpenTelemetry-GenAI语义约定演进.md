---
title: [Q7617] OpenTelemetry GenAI 语义约定演进与 LLM 可观测迁移
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7617 · OpenTelemetry GenAI 语义约定的演进与 LLM 可观测迁移

难度：P6 ｜ 标签：版本演进 / OpenTelemetry / 可观测性

**问**：团队的 LLM 可观测是自己定的 span 命名与属性（`llm.prompt_tokens` 之类）。OpenTelemetry 的 GenAI 语义约定从 experimental 持续演进（属性名改版、Agent/工具 span 规范化）。要不要迁？迁移的破坏点与收益是什么？

**答**：
- **结论**：GenAI 语义约定（`gen_ai.*` 属性族）正在标准化 LLM 可观测的合同：span 名（如 `chat {model}`）、属性 `gen_ai.system/provider`、`gen_ai.request.temperature`、`gen_ai.usage.input_tokens`（早期是 `prompt_tokens`/`completion_tokens`，后来更名并加了 reasoning/cache token 细分）、`gen_ai.tool.name`/`gen_ai.tool.call.arguments` 等。演进期的破坏点：① **属性更名**——早期 adopter 存的数据在新口径下查询失效，看板/告警按旧属性名写就要迁移；② **实验性无稳定承诺**——版本间可能继续破坏（schema 变更标记 `development`/`stable` 状态，迁前要查当前状态）；③ **instrumentation 库追赶滞后**——openllmetry/opentelemetry-instrumentation-openai 等库的实现常落后于约定。收益：迁到标准属性后，仪表盘/告警/采样规则与厂商无关，Langfuse/Jaeger/Grafana 等工具原生识别 `gen_ai.*`，跨库（不同供应商 instrumentation）属性一致，自研面板不用为每家 SDK 写一套。
- **取舍**：迁移策略：① **双写过渡**：新代码 emit `gen_ai.*` 标准属性 + 保留旧属性 3 个月，看板逐个切换，切换期用属性别名查询；② **约定状态分级对待**：`stable` 属性直接绑定，`experimental/development` 属性做映射层（自研 adapter 把标准属性转成内部规范），下游只依赖内部规范——把上游演进隔离在 adapter 一层；③ **自研 span 命名收敛**：`agent.run`/`agent.tool.call`/`llm.chat` 层级按约定对齐，trace 树跨团队可读；④ token 细分属性（cache read/write、reasoning）跟上新口径，成本归因才能细到 Q7574/Q7576 的维度。
- **实战**：落地步骤：① 盘点现有自研属性 → 约定属性映射表（一页纸契约）；② instrumentation 库升级 + 自研 emit 改造（双写）；③ 看板/告警/采样规则按映射表批量迁移，用属性存在率监控迁移进度；④ 与供应商 trace 方案（Langfuse 等）对拍一轮属性完整性；⑤ 复盘项：把"GenAI 约定版本"纳入依赖清单，约定破坏性变更（更名/删除）走变更评审，和 MCP/SDK 版本治理同级（呼应 Q7506/Q7578）。

```python
# GenAI 语义约定迁移：属性映射 + 双写 + 迁移进度监控（标准库模拟）
# 基线：Python 3.9+；真实实现 opentelemetry-sdk 1.28+ + instrumentation-openai

from dataclasses import dataclass, field

# 旧自研属性 -> GenAI 约定属性（示例映射；以当前约定文档为准）
ATTR_MAP = {
    "llm.prompt_tokens": "gen_ai.usage.input_tokens",
    "llm.completion_tokens": "gen_ai.usage.output_tokens",
    "llm.model": "gen_ai.request.model",
    "llm.temperature": "gen_ai.request.temperature",
    "tool.name": "gen_ai.tool.name",
}
STABLE_ATTRS = {v for v in ATTR_MAP.values()}


@dataclass
class SpanEmitter:
    emit_legacy: bool = True      # 双写开关
    emitted: dict[str, dict] = field(default_factory=dict)

    def emit(self, span_id: str, attrs: dict[str, object]) -> None:
        out = dict(attrs)
        if self.emit_legacy:
            for old, new in ATTR_MAP.items():
                if new in attrs and old not in out:
                    out[old] = attrs[new]          # 旧名兼容写
        self.emitted[span_id] = out

    def migrate_progress(self, spans: list[str]) -> float:
        """迁移进度 = 新约定属性覆盖率"""
        hits = sum(1 for s in spans if any(k.startswith("gen_ai.") for k in self.emitted[s]))
        return hits / len(spans)


def normalize_attrs(raw: dict) -> dict:
    """自研 adapter：标准属性 → 内部规范（隔离上游实验性属性演进）"""
    inner = {}
    for k, v in raw.items():
        if k.startswith("gen_ai."):
            inner[k] = v           # stable 约定直接透传
        else:
            inner[f"custom.{k}"] = v
    return inner


def main() -> None:
    e = SpanEmitter()
    e.emit("s1", {"gen_ai.request.model": "gpt-4o", "gen_ai.usage.input_tokens": 1200,
                  "gen_ai.request.temperature": 0.0})
    assert e.emitted["s1"]["llm.prompt_tokens"] == 1200, "双写期旧看板仍可查询"
    assert e.emitted["s1"]["gen_ai.usage.input_tokens"] == 1200

    progress = e.migrate_progress(["s1"])
    e.emit("s2", {"gen_ai.tool.name": "web_search"})
    progress = e.migrate_progress(["s1", "s2"])
    assert progress == 1.0
    print(f"双写期迁移进度 {progress:.0%}")

    inner = normalize_attrs(e.emitted["s1"])
    assert inner["gen_ai.request.model"] == "gpt-4o"
    print("OK: 属性映射双写 + adapter 隔离实验性演进，下游只依赖内部规范")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"全部透传标准属性"反而是反模式？
→ 一句话提示：`gen_ai.*` 里大量属性仍是 experimental，直接作为下游（看板/告警）依赖会把上游演进变成你的生产事故；正确姿势是 stable 属性透传、experimental 属性过 adapter 映射，下游只认内部规范。

**追问 2**：GenAI trace 里 token 计费属性为什么值得跟进细分演进？
→ 一句话提示：新口径区分 input/output/cache-read/cache-write/reasoning tokens，成本归因从"总 token"细化到"缓存策略是否有效、reasoning 是否失控"（Q7574/Q7576 的账都依赖这些细分），旧口径二分法撑不起成本分析。

## 背诵要点
- GenAI 约定是 LLM 可观测的标准合同：`gen_ai.*` 属性族 + span 命名（chat/tool call），迁移收益是与工具链解耦、跨供应商一致。
- 迁移手法：属性映射表 + 双写 3 个月 + 覆盖率监控；stable 属性直透、experimental 属性过 adapter，下游只依赖内部规范。
- token 细分属性（cache/reasoning）跟进是成本归因的前提；约定版本纳入依赖治理，破坏性变更走评审。

## 复盘追问
- 双写期怎么验证"新属性真的被下游正确消费"？提示：对拍查询——同一 span 用旧属性名与新属性名各查一遍指标，数值一致才算迁移点通过；抽样 trace 级校验树结构（parent/child）也一致。
- instrumentation 库版本与约定版本错配会出什么问题？提示：库 emit 的属性名落后或超前于看板期望，出现"半新半旧"混合数据；治理上把 instrumentation 升级与看板迁移绑定成一个变更单，而不是各自独立发布。
