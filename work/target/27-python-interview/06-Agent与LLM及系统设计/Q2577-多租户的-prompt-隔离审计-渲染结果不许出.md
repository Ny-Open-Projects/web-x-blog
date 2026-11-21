---
title: [Q2577] 多租户的 prompt 隔离审计:渲染结果不许出现别家密文
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2577 · 多租户的 prompt 隔离审计:渲染结果不许出现别家密文

> 难度:★★★★ | 标签:Agent, 多租户, 安全审计

**问**:多租户系统最怕串号,怎么系统性地发现 prompt 里的跨租户泄漏?

**答**:防线是渲染后审计:每条渲染完成的 prompt 落审计库,扫描器逐条检查是否包含其他租户的敏感令牌——账号、密钥片段、专属词表,命中即拦截发送并升级告警。它抓的是集成期错误:模板变量写错、缓存键没带租户、全局单例被并发污染,这类 bug 单测难覆盖,审计是最后一道网。扫描必须零误报才可自动拦截,所以敏感令牌要设计成唯一且不可能出现在正常文案里的形式,比如带前缀的账号号段。审计要双向:既查本租户 prompt 里的别家令牌,也查别家令牌有没有经本租户的响应回流。干净的审计通过率要进安全周报,沉默的防线最容易被不知不觉拆掉。

```python
# file: code/06_Agent与LLM及系统设计/q2577_prompt_isolation.py
"""Q2577 多租户的 prompt 隔离审计:渲染结果里不许出现别家密文。

模板渲染后的 prompt 落审计库,离线扫描器逐条检查是否包含其他
租户的敏感令牌;命中即拦截发送并升级告警。用注入的坏模板演示
一次真实泄漏被审计逮住,干净模板必须零误报。
"""

TENANT_SECRET = {"t1": "ACCT-111", "t2": "ACCT-222"}


def render_prompt_ok(tenant):
    return "你是助手,服务对象账号 " + TENANT_SECRET[tenant]


def render_prompt_buggy(tenant):
    """事故模板:误用了全局最近租户的状态,跨租户串号。"""
    return "你是助手,服务对象账号 " + TENANT_SECRET["t2"]


def audit(prompt, tenant):
    leaks = []
    for other, secret in TENANT_SECRET.items():
        if other != tenant and secret in prompt:
            leaks.append(other)
    return leaks


def main():
    clean = render_prompt_ok("t1")
    assert audit(clean, "t1") == []
    dirty = render_prompt_buggy("t1")
    leaks = audit(dirty, "t1")
    assert leaks == ["t2"], leaks
    print("干净 prompt 审计通过:零泄漏零误报")
    print("泄漏 prompt 命中租户:", leaks, "→ 拦截发送并升级告警")


if __name__ == "__main__":
    main()
```

**追问**:
- 追问一:扫描离线跑还是在线跑?答:在线拦高危,离线全量兜底,在线只查精确令牌控制时延,离线可以上模糊匹配。
- 追问二:命中后先拦还是先报?答:先拦再报,泄漏的代价不对称,误拦的代价是体验,泄漏的代价是事故。
