---
title: [Q7007] OpenTelemetry Python:手动 span 与 auto-instrumentation 的成本分层
date: 2026-11-18
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7007 · OpenTelemetry Python:手动 span 与自动埋点的成本分层

> 难度:★★★ | 标签:可观测性, OpenTelemetry, 性能

**问**：接 OTel 时团队吵起来了：运维要求全量 auto-instrumentation，开发嫌它慢、span 噪音大。手动 span 和自动埋点的真实成本差异是什么？生产上怎么分层取舍？

**答**：结论：两者的成本结构不同——**auto-instrumentation（opentelemetry-instrumentation 各框架插件）的成本在运行时开销与 span 噪音（一次请求几十个 span、采样压力大），手动 span 的成本在维护人力与覆盖盲区**。生产标准姿势是分层：入口/DB/HTTP 用自动埋点兜底（覆盖率换人力），关键业务节点（扣款、风控决策）用手动 span 补语义（业务属性、自定义指标），再靠采样器控制总量。

成本细节：
- 自动埋点的开销来源：框架 monkey-patch 在每次调用上包了一层（asyncpg/requests 的 wrapper 做 context 注入与属性采集），QPS 高的服务 CPU 开销可观测到 3-8%；span 导出默认批处理（BatchSpanProcessor）还好，但 span 属性过大（把请求体塞进 attribute）会打爆后端——这常是"上了 OTel 变慢"的真凶，而非埋点本身。
- 采样分层：ParentBased + TraceIdRatioBased 在入口定采样率（如 5%），错误强制采样（自定义 sampler：error span 100%）；头部采样省成本，尾部采样（延迟到达后按 P99 再筛）保关键样本，两者按预算混用。
- 事故复盘：某服务接入后 P99 涨 15ms，归因不是埋点而是把 64KB 请求体塞 span attribute，collector 内存爆、批处理阻塞。修复：attribute 白名单（只留 id/类型/尺寸），body 采指纹摘要；导出改 OTLP gRPC + 队列上限丢弃策略。教训：埋点数据是"数据工程"，要有 schema 约束与容量预算。

```python
# 基线:Python 3.10+ / opentelemetry-api+sdk 1.20+;缺库降级:用桩实现演示分层结构
try:
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
    trace.set_tracer_provider(TracerProvider())
    trace.get_tracer_provider().add_span_processor(          # type: ignore[attr-defined]
        BatchSpanProcessor(ConsoleSpanExporter()))
    HAS_OTEL = True
except ImportError:
    HAS_OTEL = False

from contextlib import contextmanager

@contextmanager
def span(name: str, attrs: dict | None = None):
    """手动 span 的分层包装:有 OTel 走真 span,缺库降级为 no-op。"""
    if HAS_OTEL:
        t = trace.get_tracer("biz")
        with t.start_as_current_span(name, attributes=attrs or {}):
            yield
    else:
        yield                                                # 降级:零开销 no-op

def place_order(user_id: int, amount: int) -> None:
    with span("biz.place_order", {"user_id": user_id, "amount": amount}):
        # auto-instrumentation 已覆盖 http/db;手动 span 只补业务语义
        with span("biz.risk_check"):
            pass                                             # 风控关键节点

if __name__ == "__main__":
    place_order(42, 199)
    print("span 分层:自动埋点兜底 + 手动业务语义")
```

**追问**：
- 一层追问：自动埋点的 monkey-patch 有什么坑？——打补丁时机（fork/gunicorn prefork 后补丁丢失、需 post_fork hook）、与框架版本的兼容矩阵、以及 patch 顺序冲突（多个 instrumentation 包争同一入口）；生产要求 patch 在进程启动早期、版本锁定。
- 二层追问：怎么度量"埋点本身的开销"？——对照实验：同一服务开/关 OTel 各压测一轮，比 P99 与 CPU；再细化到 processor 层（batch size、导出超时、队列丢弃计数）。开销异常时先查 attribute 体积与导出阻塞，再查采样。
- 三层追问：多团队接入怎么治理 span 语义一致性？——span 命名规范（`{域}.{动作}`）+ 公共属性包（公司库封装 tracer，强制带 service/version/env）+ CI 检查 span 命名；后端 collector 上再做 attribute 裁剪兜底。
