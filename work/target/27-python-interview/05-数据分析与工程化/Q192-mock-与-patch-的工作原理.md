---
title: [Q192] mock 与 patch 的工作原理
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q192 · mock 与 patch 的工作原理

> 难度:★★★ | 标签:mock, unittest.mock, patch

**问**:Mock 是怎么"替换掉"一个函数的?MagicMock 和普通 Mock 的区别?

**答**:`patch` 的本质是**运行期属性替换**:用 `with patch("module.attr")` 或装饰器,在进入作用域时把目标对象上的属性指向 Mock 对象,退出时恢复原值(底层就是 getattr/setattr 包一层 try/finally)。两个关键点:一,patch 的是**被使用处的引用查找路径**,不是"定义处"(见 Q193);二,`MagicMock` 预配置了 dunder 方法(`__call__`、`__enter__`、`__iter__` 等),所以能当函数、上下文管理器、迭代器用,而普通 Mock 调用 dunder 会报错,因此 patch 默认返回 MagicMock。断言主要靠 `assert_called_once_with` 等方法验证交互。

```python
# file: code/05_数据分析与工程化/q192_mock_basics.py
from unittest.mock import MagicMock

class EmailClient:
    def send(self, to, subject):
        raise RuntimeError("真实实现不会在测试中被调用")

def notify(client: EmailClient, user):
    return client.send(to=user["email"], subject="welcome")

def test_notify_called_once():
    client = MagicMock(spec=EmailClient)  # spec 限制只能 mock 真实存在的方法
    notify(client, {"email": "a@b.com"})
    client.send.assert_called_once_with(to="a@b.com", subject="welcome")

def test_return_value():
    client = MagicMock()
    client.send.return_value = True
    assert notify(client, {"email": "x@y.com"}) is True
```

**追问**:
- spec 有什么用?——限制 Mock 只能访问真实对象的属性,防止被测代码改名后测试仍然通过(假阳性)。
- MagicMock 和 Mock 的区别?——MagicMock 预配置了魔术方法(call/enter/iter);需要 mock 上下文管理器、迭代器时必须用它。
- 怎么断言调用参数?——`mock.assert_called_once_with(...)`,call_args 检查任意次调用;断言调用而非断言内部实现,否则测试脆弱。
- autospec=True 有什么好处?——按真实对象签名生成 mock,调用签名错了会报错,防 mock 与实现漂移。
