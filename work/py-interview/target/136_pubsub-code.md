# 136. 实战：发布订阅（Publisher/Subscriber + setter 触发 notify）

> 分类：编程范式/设计模式 | 难度：L3 | 题型：代码题 | 频率：中 | 关键词：**发布者** / **订阅者** / **notify** / **setter 触发**
> 原文锚点：第 30~42 段「Publisher 持观察者列表，add/remove/notify；Subscriber 有 notify_by；数据被 set 时触发通知」

## 一句话总述
源里的完整例子：发布者持有订阅者列表，提供 `add/remove/notify`；订阅者实现 `notify_by(publisher, data)`；当发布者的数据**被赋值（setter）**时自动调用 `notify`，逐个触发订阅者的回调——这就是发布订阅的落地。

## 面试官视角
- **考察意图**：考你能否**动手实现**一个可运行的发布订阅，并讲清"事件如何触发"与"如何取消"。
- **P5** 能写出 Publisher 的 add/notify + Subscriber 的回调 / **P6** 能说明**setter 触发**机制（属性赋值即事件点）与 `remove` 取消订阅 / **P7** 能指出硬编码 `notify_by` 方法名、**同步阻塞通知**（一个订阅者慢会拖住所有人）的局限，并给出改进（事件名分发、`asyncio`） `[经验]`。
- **红旗**：① 通知时直接 `subscriber.update` 却方法名对不上；② 忘记在 add 时判重导致重复通知；③ 没说怎么停止订阅。
- **惊艳点**：源中"set 数据时调用 notify"——用 **property setter** 把"状态变更"变成"事件源"，比手动调 `notify()` 更优雅。验证：赋值即打印订阅者输出 `[实测]`。

## 主问答
**Q：写个发布订阅，数据被设置时自动通知所有订阅者？**
**A：**
1. **结论**：发布者维护订阅者列表，订阅者各自有回调；用 **property setter** 在数据被赋值时自动 `notify`。
2. **机制**：`add` 时判重避免重复，`notify` 遍历调用每个订阅者的 `notify_by(publisher, data)`；`remove` 把订阅者移出列表即停止接收。
3. **边界**：源里通知是**同步**的——任一订阅者抛异常或慢都会阻塞发布者；生产上应隔离或异步化。
**加分层**：更通用的写法是按**事件名**分发（`on(event, cb)` / `emit(event, data)`），而非单一 `notify`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 谁通知谁 | 概念 | 发布者→订阅者 | 换题 → 不及格 |
| L2 | add/remove 干嘛 | 机制 | 注册/取消 | 判 P5 |
| L3 | 怎么触发通知 | 机制 | setter 赋值 | 判 P6 |
| L4 | 同步通知局限 | 风险 | 阻塞/异常传播 | 判 P6+ |
| L5 | 事件名分发 | 深入 | on/emit 总线 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 全版本 | property setter 稳定 | 用 setter 触发 notify |
| Py3.7+ | dataclass + property | 可简化 |
| 异步 | asyncio 解阻塞 | 通知放事件循环 |

## 关键代码
```python
class Publisher:
    def __init__(self, name):
        self.name = name; self._subs = []; self._data = None
    def subscribe(self, s):
        if s not in self._subs: self._subs.append(s)   # 判重
    def remove(self, s):    self._subs.remove(s)
    @property
    def data(self): return self._data
    @data.setter
    def data(self, v):
        self._data = v; self.notify(v)                 # 赋值即事件
    def notify(self, v):
        for s in self._subs: s.notify_by(self, v)

class Subscriber:
    def __init__(self, name): self.name = name
    def notify_by(self, pub, data):
        print(f"{self.name} 收到 {pub.name} 的数据: {data}")

p = Publisher("订单"); f = Subscriber("格式化器")
p.subscribe(f); p.data = "新订单"      # 自动通知 -> 打印
```

## ⚠️ 原文纠错
原文代码示例逻辑正确（发布者 add/remove/notify，订阅者 notify_by，数据 set 时触发通知，"bannerformatter/formatter"为两个**订阅者类名**，"setnodify"指 **setter 触发 notify**，"poparation"=**publisher**，"nodify/notiffy/notilefy"=**notify**，"notifyingby/noto翻译by"=**notify_by**）。卡面补充了"add 判重""同步阻塞局限""事件名分发改进"等工程要点 `[经验]`。原文"formatter 传名称 formatter"表述略绕，按语义整理。无事实错误，仅术语音译需还原。

## 总结与追问预判
- 发布者列表 + property setter 触发 notify = 发布订阅落地。
- 下一题：**策略模式**（137）、**观察者本质**（135）。
