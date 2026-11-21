---
title: [Q1565] Seam 注入:测试接缝的最小改造
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1565 · Seam 注入:测试接缝的最小改造

> 难度:★★★☆☆ | 标签:可测试性, 依赖注入, seam

**问**:代码怎么留「接缝」让测试能替换依赖?monkeypatch 和注入比差在哪?

**答**:Seam(接缝)是不改调用代码就能替换实现的位置,最小姿势是把依赖做成构造参数:参数签名上写默认值(真实实现),测试传 fake——类型可见、IDE 可跳转、并发测试不互踩。三种常见接缝:① 依赖对象注入(sender、clock、rng);② 工厂参数注入(传可调用对象);③ 模块级间接层(调用模块函数而非绑死第三方符号)。与 monkeypatch 的分工:patch 是全局态,并发用例互踩、签名不可见,只适合「别人的库」的临时补丁;项目自己的代码一律注入。设计口诀:测试时想 mock 什么,就把它设计成参数——「测试难点驱动设计」。

```python
# file: code/01_语言核心与底层/q1565_seam_injection.py


def smtp_sender(recipient, text):
    """真实依赖:演示桩,不真发。"""
    return "smtp -> %s: %s" % (recipient, text)


def console_sender(recipient, text):
    return "console -> %s: %s" % (recipient, text)


class Notifier:
    """接缝设计:sender 是构造参数,默认真实实现。"""

    def __init__(self, sender=smtp_sender, max_len=140):
        self.sender = sender
        self.max_len = max_len

    def notify(self, recipient, text):
        if len(text) > self.max_len:
            raise ValueError("text 超过 %d 字符限制" % self.max_len)
        return self.sender(recipient, text)


def record_sink(recipient, text):
    """测试用 fake:记录而不发送。"""
    record_sink.calls.append((recipient, text))
    return "recorded"


record_sink.calls = []


def run_suite():
    results = []
    notifier = Notifier(sender=record_sink)          # 注入 fake
    results.append(notifier.notify("ops@x.io", "deploy done"))
    results.append(notifier.notify("ops@x.io", "deploy v2"))
    assert record_sink.calls == [("ops@x.io", "deploy done"),
                                 ("ops@x.io", "deploy v2")]
    return results


if __name__ == "__main__":
    print("default:", Notifier().notify("dev@x.io", "hello"))
    print("fake   :", run_suite())
    try:
        Notifier().notify("dev@x.io", "x" * 200)
    except ValueError as err:
        print("guard  :", err)
```

**追问**:1) 什么时候 monkeypatch 是更优解?——依赖属于第三方黑盒、又不想为此增加构造参数时;项目自己的代码一律走注入,patch 留给「别人的库」。2) Seam 的本质?——可替换依赖点:构造参数是最小接缝,其次模块级工厂函数、可覆写方法;注入让 fake 在不 patch 的前提下进入被测代码。3) 改造的最小化原则?——不为测试增加「只有测试用」的参数;依赖对象化时按生命周期分组(configuration vs request);接缝过多说明职责过载。4) 生产陷阱?——patch 忘还原污染其他测试(fixture 管理);注入面爆炸(十几个依赖参数);通过全局单例隐式取依赖,接缝消失,只能 patch。
