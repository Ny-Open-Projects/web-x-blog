# 32. 怎么自定义业务异常

> 分类：语言基础/异常 | 难度：L2 | 题型：工程题 | 频率：高 | 关键词：**继承 Exception** / **附加上下文** / **异常分层**
> 原文锚点：第 30~42 段「通过继承 Exception 作为基类来定义自己的异常…还可以给它加上一些附加的信息」

## 一句话总述
自定义异常 = **继承 `Exception`** + 在 `__init__` 里挂业务字段；抛出用 `raise BizError(...)`，捕获时靠**父类兜住子类**实现一处收口。

## 面试官视角
- **考察意图**：只会 `class X(Exception): pass`，还是会设计一套能支撑排查与统一处理的异常体系。
- **P5** 会定义异常类 / **P6** 会带上下文字段并知道保留原始异常 / **P7** 会做**分层设计**并在系统边界统一转成响应码。
- **红旗**：① `raise "字符串"`（Python 3 直接 TypeError）；② 异常消息只有"失败"两个字；③ 捕获后 print 了事、丢掉上下文。
- **惊艳点**：`except BizError` 能一次兜住全部子类，所以**先建基类再细分**能让调用方一处收口。验证：`issubclass(OrderClosedError, BizError)` → True `[实测]`

## 主问答
**Q：业务里需要自己的异常类型，你会怎么定义？**
**A：**
1. **先给结论**：`class BizError(Exception)`，需要附加信息就在 `__init__` 里加字段（错误码、订单号等）并调用 `super().__init__(msg)`。
2. **再给机制**：捕获**父类**即可命中所有子类，因此通常设计 `BizError` 作根，下面挂 `OrderClosedError`、`StockNotEnoughError` 等细分类型。
3. **最后给边界**：异常不是返回值，别拿它做流程控制；把底层异常翻译成业务异常时要用 `raise ... from e` 保留因果链（见 15 卡）。
**加分层**：消息里带上**可定位字段**（订单号、用户 id），排查效率差别极大——"订单已关闭 order_id=123" 远胜"操作失败"。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 自定义异常继承谁 | 术语 | Exception | 换题 → 不及格 |
| L2 | 怎么带上业务信息 | 机制 | 自定义 `__init__` 挂字段 | 判 P5 |
| L3 | 为什么要先建一个基类 | 设计 | 父类一处兜底 | 判 P6 |
| L4 | 翻译底层异常要注意什么 | 边界 | `raise ... from e` 保留链 | 判 P6+ |
| L5 | 边界层怎么统一处理 | 架构判断 | 捕获基类 → 转 HTTP 码 + 日志 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 3.x | 2.x 允许 `raise "str"`，Python 3 起必须抛 BaseException 实例 | 一律抛异常实例 |

## 关键代码
```python
class BizError(Exception):
    def __init__(self, msg, code=400, **ctx):
        super().__init__(msg)
        self.code, self.ctx = code, ctx
class OrderClosedError(BizError):
    pass
try:
    raise OrderClosedError("订单已关闭", code=409, order_id=123)
except BizError as e:                  # 父类兜住子类
    print(type(e).__name__, e.code, e.ctx)   # OrderClosedError 409 {'order_id': 123}
print(issubclass(OrderClosedError, BizError))  # True
```

## ⚠️ 原文纠错
原文「捕获一个父类的异常，它所有的子类异常都在捕获范围之内」正确；原文中的音译类名已还原为标准写法。原文未提"捕获后应保留原始异常链"，见 15 卡。

## 总结与追问预判
- 先有基类再细分，消息带可定位字段，边界层统一收口。
- 下一题：见 30（继承体系）、15（异常链）。
