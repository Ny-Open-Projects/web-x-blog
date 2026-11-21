---
title: [Q1091] 测试替身光谱:dummy、stub、spy、mock
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1091 · 测试替身光谱:dummy、stub、spy、mock

> 难度:★★★☆ | 标签:测试替身, mock

**问**:mock、stub、spy 到底差在哪?面试时怎么讲清楚?

**答**:按"替身知道多少、被问什么"分四档:dummy 只为满足签名占位,从不被使用;stub 提供固定返回值,让被测代码能跑;spy 是记录型替身,真实或固定行为之外把调用存下来供事后断言(调用了谁、几次、什么参数);mock 事前声明期望交互,调用不符合期望即失败。状态验证(stub 后断言返回值)优先于交互验证(spy/mock 断言调用),过度 mock 会把测试锁死在实现细节上,重构就红。

```python
# file: code/05_数据分析与工程化/q1091_test_doubles.py

class Mailer:
    def send(self, to, body):
        raise RuntimeError("真实 IO")

class StubMailer(Mailer):
    def send(self, to, body):
        return True                      # stub:固定返回,让流程走通

class SpyMailer(Mailer):
    def __init__(self):
        self.sent = []

    def send(self, to, body):
        self.sent.append((to, body))     # spy:记录交互供事后断言
        return True

def notify(mailer, user, message):
    return mailer.send(user["email"], message)

if __name__ == "__main__":
    user = {"email": "a@b.c"}
    assert notify(StubMailer(), user, "hi") is True          # 状态验证
    spy = SpyMailer()
    notify(spy, user, "hi")
    assert spy.sent == [("a@b.c", "hi")]                     # 交互验证
    print("stub 验证状态,spy 验证交互,mock 事前期望,dummy 纯占位")
```

**追问**:
- 追问 1:什么信号说明 mock 用过度了?—— 断言全是 called_with,改一次内部实现红一片测试,行为没变测试却坏。
- 追问 2:fake 和 stub 的区别?—— fake 是轻量可用实现(内存数据库、假仓库),有真实行为逻辑,适合状态机类依赖。
