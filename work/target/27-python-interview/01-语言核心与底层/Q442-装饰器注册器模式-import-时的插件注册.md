---
title: [Q442] 装饰器注册器模式:import 时的插件注册
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q442 · 装饰器注册器模式:import 时的插件注册

> 难度:★★★☆ | 标签:装饰器, 设计模式

**问**:@register 装饰器是怎么实现「自动发现」的?注册顺序由什么决定,有什么坑?

**答**:装饰器在被 import 时立刻执行,register 闭包把被装饰函数写进模块级注册表,于是「定义即注册」,调用方只需 import 覆盖所有插件模块的包。顺序由 import 顺序决定:包内模块按 __init__.py 里的出现顺序注册,重复注册要显式报错或以先注册者为准,否则静默覆盖极难排查。注册表是全局可变状态,测试中要注意隔离(每个用例 reset)。

```python
# file: code/01_语言核心与底层/q442_decorator_registry.py
HANDLERS = {}

def register(event_type):
    def deco(func):
        if event_type in HANDLERS:
            raise ValueError(f"duplicate handler for {event_type}")
        HANDLERS[event_type] = func
        return func                   # 返回原函数:不改变调用方式
    return deco

@register("user.created")
def on_user_created(payload):
    return f"welcome {payload['name']}"

@register("user.deleted")
def on_user_deleted(payload):
    return f"bye {payload['name']}"

def dispatch(event_type, payload):
    return HANDLERS[event_type](payload)

if __name__ == "__main__":
    print(dispatch("user.created", {"name": "Alice"}))
    print(dispatch("user.deleted", {"name": "Bob"}))
    print("registry keys:", sorted(HANDLERS))
```

**追问**:1) 被注册的函数还能被直接 import 调用吗?——能,deco 返回原函数,注册与直接调用互不影响;若返回 wrapper 则要 functools.wraps 保住元信息。2) 注册顺序为什么危险?——顺序由 import 顺序决定,等价于 __init__.py 里的模块列表顺序;隐式顺序让路由结果依赖文件命名与导入路径,重构排序即改变行为,重复注册应显式报错。3) 装饰器在 import 期执行的机制?——def 创建函数对象后装饰器调用同步发生,注册表是模块全局 dict;import 由导入锁串行化,但运行期动态注册(插件热加载)就要自己加锁。4) 生产陷阱?——插件模块没有 import 路径就永不注册(靠 import 副作用很脆弱),要用 pkgutil/entry point 枚举;测试并行化后全局注册表互相污染,fixture 里快照-恢复隔离。
