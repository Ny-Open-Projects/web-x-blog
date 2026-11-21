---
title: [Q1290] gc 与 __del__ 交互:半析构状态里的兄弟对象
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1290 · gc 与 __del__ 交互:半析构状态里的兄弟对象

> 难度:★★★☆☆ | 标签:gc, __del__, 循环引用

**问**:两个对象互相引用、各自有 __del__,终结时在 __del__ 里访问对方,能看到什么?顺序可靠吗?

**答**:PEP 442(3.4+)让带 __del__ 的循环引用可以被回收(不再进 gc.garbage 滞留,Q403),但回收器对这批对象的终结顺序是「实现细节」:A 的 __del__ 执行时,B 可能还没终结(属性完好)、也可能已终结(属性被清成 None 或直接消失),任何依赖顺序的逻辑都不可靠。因此 __del__ 的纪律是:只碰 self 自己的字段与明确存活的全局,绝不访问「同批死亡」的关联对象——要通知对方,用 weakref(回调时序见 Q1289)或让二者共享一个 finalize 钩子。可实测的安全结论:回收后 gc.garbage 为空(正常路径),说明 PEP 442 的两轮终结方案有效;「__del__ 里访问 peer」的代码在 CPython 上碰巧常能跑通,换版本/换实现就炸,这正是「看起来对」的陷阱。

```python
# file: code/01_语言核心与底层/q1290_del_half_dead.py
import gc


class Node:
    def __init__(self, name):
        self.name = name
        self.peer = None

    def __del__(self):
        # 危险示范:peer 可能已终结,getattr 兜底只是防炸不是防错
        peer_name = getattr(self.peer, "name", "<gone>")
        print("__del__ of", self.name, "sees peer as", peer_name)


if __name__ == "__main__":
    a, b = Node("a"), Node("b")
    a.peer, b.peer = b, a               # 循环引用
    del a, b
    gc.collect()
    print("gc.garbage:", gc.garbage, "<- PEP 442 后循环垃圾不滞留")
```

**追问**:1) 3.4 之前这段代码会怎样?——带 __del__ 的循环会被丢进 gc.garbage 永不回收,泄漏;PEP 442 用「先执行终结器、再检查复活、再安全拆除」的两轮方案解决了它。2) 「半析构状态」指什么?——终结阶段兄弟对象可能已终结、属性可能被清;__del__ 里访问其他对象要做防御(判 None);这也是「终结器只做日志」的理由。3) 顺序保证?——引用计数路径确定性(单链归零即调);GC 循环路径顺序未定义——跨对象资源释放不能依赖 __del__ 顺序。4) 生产陷阱?——__del__ 里做 IO/网络清理(时机与顺序都不可靠);依赖析构顺序的资源链;正确姿势是显式生命周期(with/close)+ finalize 兜底。
