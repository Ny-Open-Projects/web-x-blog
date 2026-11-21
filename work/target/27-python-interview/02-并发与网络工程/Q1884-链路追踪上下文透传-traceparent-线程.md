---
title: [Q1884] 链路追踪上下文透传:traceparent、线程不继承的坑
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1884 · 链路追踪上下文透传:traceparent、线程不继承的坑

> 难度:★★★★ | 标签:链路追踪, contextvars, 透传

**问**:trace_id 怎么在整条调用链上保持一致?为什么线程里读不到 contextvars 的值?

**答**:W3C Trace Context 用 traceparent 头承载:'版本-32位traceid-16位spanid-标志位',全链共享 trace_id、每跳换 span_id,下游解析后生成子 span。

- 第一坑:contextvars 在新线程是全新上下文,直接 get 拿到 None——context 随任务/协程继承,不随线程继承;

- 跨线程修复:contextvars.copy_context() 显式注入;跨进程只有一条路:traceparent 当数据传递(HTTP 头、消息属性),演示里子 span 的 trace_id 与父一致、span_id 不同;

- 畸形 traceparent 必须拒绝:段数、版本、十六进制长度都要校验,追踪头是外部输入,不校验就会变成注入面。

日志与 trace 的绑定同理:trace_id 作为字段打进结构化日志,而不是拼进消息字符串。

```python
# file: code/02_并发与网络工程/q1884_trace_context.py
# -*- coding: utf-8 -*-
"""链路追踪上下文透传: traceparent 格式、线程不继承的坑与显式传递。

- traceparent 格式: 版本-32位traceid-16位spanid-标志位, 全链共享 traceid;
- contextvars 在新线程里是全新上下文: 直接 get 拿到 None, 这是分布式追踪第一坑;
- 跨线程要么显式 copy_context 注入, 要么把 traceparent 当数据传递(如 HTTP 头)。
"""
import contextvars
import secrets
import threading

trace_var = contextvars.ContextVar("traceparent", default=None)


def new_traceparent():
    return "00-%s-%s-01" % (secrets.token_hex(16), secrets.token_hex(8))


def parse_traceparent(tp):
    parts = tp.split("-")
    if len(parts) != 4:
        raise ValueError("traceparent 段数错误")
    version, trace_id, span_id, flags = parts
    if version != "00":
        raise ValueError("不支持的版本")
    if len(trace_id) != 32 or any(c not in "0123456789abcdef" for c in trace_id):
        raise ValueError("trace_id 必须是 32 位十六进制")
    if len(span_id) != 16 or any(c not in "0123456789abcdef" for c in span_id):
        raise ValueError("span_id 必须是 16 位十六进制")
    return {"trace_id": trace_id, "span_id": span_id, "flags": flags}


def child_span(tp):
    ctx = parse_traceparent(tp)                # 子 span 共享 trace_id, 换 span_id
    return "00-%s-%s-01" % (ctx["trace_id"], secrets.token_hex(8))


def downstream(headers):
    """模拟下游服务: 从头里读 traceparent, 生成子 span。"""
    tp = headers["traceparent"]
    child = child_span(tp)
    return parse_traceparent(tp)["trace_id"], parse_traceparent(child)["span_id"]


def main():
    tp = new_traceparent()
    trace_var.set(tp)

    # 坑: 新线程不继承 contextvars
    box = {}

    def naive_reader():
        box["in_thread"] = trace_var.get()

    t = threading.Thread(target=naive_reader)
    t.start()
    t.join()
    print("线程内直接读 trace_var:", box["in_thread"])
    assert box["in_thread"] is None, "新线程不继承上下文, 必然是 None"

    # 修复一: 显式注入 context
    ctx = contextvars.copy_context()

    def ctx_reader():
        box["via_ctx"] = ctx.run(trace_var.get)

    t2 = threading.Thread(target=ctx_reader)
    t2.start()
    t2.join()
    print("copy_context 注入后读到:", box["via_ctx"] == tp)
    assert box["via_ctx"] == tp

    # 修复二(跨进程唯一可行): traceparent 当数据传, 例如 HTTP 头
    headers = {"traceparent": tp}
    trace_id, child_span_id = downstream(headers)
    parent_span_id = parse_traceparent(tp)["span_id"]
    print("父 span %s, 子 span %s, trace_id 一致: %s"
          % (parent_span_id, child_span_id, True))
    assert trace_id == parse_traceparent(tp)["trace_id"]
    assert child_span_id != parent_span_id, "子 span 换 id"

    # 畸形 traceparent 必须拒绝
    bad = ["00-xyz-abc-01",                       # 长度不对
           "02-%s-%s-01" % ("a" * 32, "b" * 16),  # 版本不支持
           "00-%s-%s-01" % ("g" * 32, "b" * 16)]  # 非十六进制
    for b in bad:
        try:
            parse_traceparent(b)
            raise AssertionError("畸形 %s 不应通过" % b)
        except ValueError as e:
            print("拒绝畸形 traceparent:", e)

    print("结论: 追踪上下文是显式契约, 跨线程跨进程都要亲手交棒")


if __name__ == "__main__":
    main()
```

**追问**:1) 异步任务链里 context 自动传播吗?——asyncio.create_task 会快照当前 context,任务内修改互不影响,这是 task 的语义;跨线程池(to_thread/run_in_executor)就回到了显式传递的范畴。2) contextvars 的继承语义边界?——Task 创建时快照 Context(协程内 set 互不影响);新线程全新空 Context(get 拿 None);to_thread/run_in_executor 不自动传播(要 copy_context)——三句话覆盖全部「值去哪了」的问题(Q1575 同源)。3) traceparent 的校验清单?——段数(4 段)、版本字节、traceid 32hex/spanid 16hex、flags 合法;畸形拒绝(置为无效不透传)——追踪头是外部输入,校验缺失就是注入面(头注入 Q1610 的近亲)。4) 生产陷阱?——跨线程读 contextvars 拿 None(见原问);trace_id 在 MQ 边界断链(消息属性没带 traceparent);畸形 traceparent 直接用(注入);span_id 全链相同(没换);采样标志(flags)丢失导致全量追踪风暴。


---
